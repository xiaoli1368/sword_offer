class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        if (s1.empty()) {
            return true;
        }
        if (s2.empty()) {
            return false;
        }

        int n1 = s1.size(), n2 = s2.size();
        vector<char> d1(26), d2(26);
        for (const auto & c : s1) {
            d1[c - 'a'] += 1;
        }

        for (int h = 0; h < n2; h++) {
            d2[s2[h] - 'a'] += 1;
            if (h >= n1) {
                d2[s2[h - n1] - 'a'] -= 1;
            }
            if (d1 == d2) {
                return true;
            }
        }
        return false;
    }
};