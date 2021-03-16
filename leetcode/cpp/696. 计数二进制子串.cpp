class Solution {
public:
    int countBinarySubstrings(string s) {
        int cnt = 0, n = s.size();
        for (int i = 0; i < n - 1; i++) {
            if (s[i] != s[i + 1]) {
                cnt += 1;
                int l = i, h = i + 1;
                while (l >= 1 && h <= n - 2 && s[l] == s[l - 1] && s[h] == s[h + 1]) {
                    l -= 1;
                    h += 1;
                    cnt += 1;
                }
            }
        }
        return cnt;
    }

    int countBinarySubstrings(string s) {
        int cnt = 0, same = 1, diff = 0;
        for (int i = 1; i < s.size(); i++) {
            if (s[i] == s[i - 1]) {
                same += 1;
            } else {
                diff = same;
                same = 1;
            }
            if (diff >= same) {
                cnt += 1;
            }
        }
        return cnt;
    }
};