class Solution {
public:
    vector<bool> prefixesDivBy5(vector<int>& a) {
        int n = 0;
        vector<bool> ret(a.size());
        for (int i = 0; i < a.size(); i++) {
            n = (n * 2 + a[i]) % 5;
            ret[i] = (n == 0);
        }
        return ret;
    }
};