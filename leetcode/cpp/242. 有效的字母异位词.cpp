class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size()) {
            return false;
        }
        std::map<char, int> map;
        for (auto & c : s) {
            map[c] += 1;
        }
        for (auto & c : t) {
            map[c] -= 1;
            if (map[c] == -1) {
                return false;
            }
        }
        return true;
    }
};