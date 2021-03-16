class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int ret = 0, l = 0;
        unordered_map<char, int> visited;
        for (int h = 0; h < s.size(); h++) {
            if (visited[s[h]] == 0) {
                ret = max(ret, h - l + 1);
            } else {
                while (visited[s[h]] > 0) {
                    visited[s[l++]] -= 1;
                }
            }
            visited[s[h]] += 1;
        }
        return ret;
    }
};