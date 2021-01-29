class Solution {
public:
	// 来自labuladong的参考解法
    string minWindow(string s, string t) {
        int start = 0;
        int minLen = INT_MAX;
        int left = 0, right = 0, valid = 0;
        std::unordered_map<char, int> need, window;
        for (auto & i : t) {
            need[i]++;
        }

        while (right < s.size()) {
            char c = s[right++];
            if (need.count(c)) {
                window[c]++;
                if (window[c] == need[c]) {
                    valid++;
                }
            }

            while (valid == need.size()) {
                if (right - left < minLen) {
                    minLen = right - left;
                    start = left;
                }
                char c = s[left++];
                if (need.count(c)) {
                    if (need[c] == window[c]) {
                        valid--;
                    }
                    window[c]--;
                }
            }
        }

        if (minLen == INT_MAX) {
            return std::string();
        } else {
            return s.substr(start, minLen);
        }
    }

    // 来自leetcode-101的参考解法
    // 注意同样时把update的过程放到了缩窗的内部
    string minWindow(string s, string t) {
        // 初始化
        vector<int> chars(128, 0); // 统计窗口内的hash，表示当前字符需求
        vector<int> flag(128, false); // 表示每个字符是否在T中出现 

        // 统计T中的字符情况
        for (auto & chr : t) {
            chars[chr]++;
            flag[chr] = true;
        }

        // 滑动窗口，不断更改统计数据
        int cnt = 0, l = 0, min_l = 0, min_size = s.size() + 1;
        for (int r = 0; r < s.size(); r++) { // 移动右指针
            // 如果当前字符处在目前范围内
            if (flag[s[r]]) {
                // 更新当前已匹配的字符个数
                if (--chars[s[r]] >= 0) {
                    ++cnt;
                }
                // 如果已经满足要求
                // 则尝试移动左指针，在不影响结果的情况下，获取最短字符串
                while (cnt == t.size()) {
                    // 更新结果
                    if (r - l + 1 < min_size) {
                        min_l = l;
                        min_size = r - l + 1;
                    }
                    // 更新左指针
                    if (flag[s[l]] && ++chars[s[l]] > 0) {
                        --cnt;
                    }
                    ++l;
                }
            }
        }
        return min_size > s.size() ? "" : s.substr(min_l, min_size);
    }
};