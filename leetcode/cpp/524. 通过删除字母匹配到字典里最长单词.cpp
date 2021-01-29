class Solution {
public:
    // 判断字符串s是否可以通过删除字符的方式与ss匹配
    bool check(string s, string ss) {
        int i = 0, j = 0;
        int m = s.size(), n = ss.size();
        if (m < n) {
            return false;
        }
        while (i < m && j < n) {
            if (s[i] == ss[j]) {
                j += 1;
            }
            i += 1;
        }
        return j == n;
    }

    string findLongestWord(string s, vector<string>& d) {
        if (s.empty() || d.empty()) {
            return "";
        }

        sort(d.begin(), d.end(), [](string x, string y) -> bool {return x.size() > y.size() || (x.size() == y.size() && x < y);});

        for (auto & ss : d) {
            if (check(s, ss)) {
                return ss;
            }
        }
        return "";
    }
};