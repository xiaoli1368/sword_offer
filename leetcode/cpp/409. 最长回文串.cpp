class Solution {
public:
    int longestPalindrome(string s) {
        int ret = 0, center = 0, cnt;
        unordered_map<char, int> d;
        for (const auto& chr : s) {
            d[chr] += 1;
        }
        for (const auto& p : d) {
            cnt = p.second;
            if (cnt % 2 == 0) {
                ret += cnt;
            } else {
                ret += cnt - 1;
                center = 1;
            }
        }
        return ret + center;
    }
};