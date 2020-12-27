class Solution {
public:
    bool isIsomorphic(string s, string t) {
        if (s.size() != t.size()) {
            return false;
        }

        std::unordered_map<char, char> d;
        std::unordered_set<char> visited;

        for (int i = 0; i < s.size(); i++) {
            char si = s[i];
            char ti = t[i];
            if (d.count(si) == 0) {
                if (visited.count(ti) == 1) {
                    return false;
                } else {
                    visited.insert(ti);
                    d[si] = ti;
                }
            } else {
                if (d[si] != ti) {
                    return false;
                }
            }
        }

        return true;
    }
};