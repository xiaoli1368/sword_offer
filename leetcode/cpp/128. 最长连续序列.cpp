class Solution {
public:
	// 哈希存储，然后遍历
    int longestConsecutive(vector<int>& nums) {
        if (nums.empty()) {
            return 0;
        }

        int max = 0x80000000;
        int min = 0x7fffffff;
        for (auto & i : nums) {
            if (i < min) min = i;
            if (i > max) max = i;
        }

        if (min == max) {
            return 1;
        }

        std::vector<int> tmp(max-min+1);
        for (auto & i : nums) {
            tmp[i-min]++;
        }

        int cnt = 0;
        int ret = 0;
        for (int i = 0; i <= max - min; i++) {
            if (tmp[i] > 0) {
                cnt++;
                if (cnt > ret) {
                    ret = cnt;
                }
            } else {
                cnt = 0;
            }
        }

        return ret;
    }

    // 哈希存储当前区间长度
    int longestConsecutive(vector<int>& nums) {
        if (nums.empty()) {
            return 0;
        }

        int ret = 0;
        std::map<int, int> d;

        for (auto & i : nums) {
            if (d.count(i) == 0) {
                int left = (d.count(i - 1) > 0 ? d[i - 1] : 0);
                int right = (d.count(i + 1) > 0 ? d[i + 1] : 0);
                int length = 1 + left + right;
                ret = max(ret, length);
                // 更新字典
                d[i] = d[i - left] = d[i + right] = length;
            }
        }
        return ret;
    }

	// 究极优化版
    int longestConsecutive(vector<int>& nums) {
        int ret = 0, left, right;
        unordered_map<int, int> d;
        for (const int& num : nums) {
            if (d.count(num) == 0) {
                left = (d.count(num - 1) == 0 ? 0 : d[num - 1]);
                right = (d.count(num + 1) == 0 ? 0 : d[num + 1]);
                ret = max(ret, 1 + left + right);
                d[num] = d[num - left] = d[num + right] = 1 + left + right;
            }
        }
        return ret;
    }

    // set遍历
    int longestConsecutive(vector<int>& nums) {
        if (nums.empty()) {
            return 0;
        }

        int ret = 0;
        std::unordered_set<int> d(nums.begin(), nums.end());

        for (auto it = d.begin(); it != d.end(); it++) {
            int curr = *it, length = 1;
            if (d.count(curr - 1) == 0) { // 保证从首端开始遍历
                while (d.count(curr + 1) > 0) {
                    curr += 1;
                    length += 1;
                }
                ret = max(ret, length);
            }
        }
        return ret;
    }
};