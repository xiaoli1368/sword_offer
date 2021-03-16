class Solution {
public:
    bool isIsomorphic(string s, string t) {
        if (s.size() != t.size()) {
            return false;
        }

        std::unordered_map<char, char> d;
        std::unordered_set<char> visited;

        for (int i = 0; i < s.size(); i++) {
            char si = s[i], ti = t[i];
            if (d.count(si) == 0 && visited.count(ti) == 0) {
                d[si] = ti;
                visited.insert(ti);
            } else if (d.count(si) == 0 && visited.count(ti) > 0) {
                return false;
            } else if (d.count(si) > 0 && d[si] != ti) {
                return false;
            }
        }
        return true;
    }

	// ===== 更加高效的方法 =====
	// 判断两字符串对应位置的字符，在第一次出现的位置是否相同
	bool isIsomorphic(string s, string t) {
        if (s.size() != t.size()) {
            return false;
        }
        vector<int> s_first_index(256, -1), t_first_index(256, -1);
        for (int i = 0; i < s.size(); i++) {
            if (s_first_index[s[i]] != t_first_index[t[i]]) {
                return false;
            }
            s_first_index[s[i]] = t_first_index[t[i]] = i;
        }
        return true;
    }
};