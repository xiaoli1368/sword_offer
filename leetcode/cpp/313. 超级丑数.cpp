class Solution {
public:
    int nthSuperUglyNumber(int n, vector<int>& primes) {
        if (n <= 1 || primes.empty()) {
            return 1;
        }

        int m = primes.size();
        vector<int> pointer(m, 0);
        vector<int> ret(n, INT_MAX);
        ret[0] = 1;

        for (int i = 1; i < n; i++) {
            for (int j = 0; j < m; j++) {
                ret[i] = min(ret[i], primes[j] * ret[pointer[j]]);
            }
            for (int j = 0; j < m; j++) {
                if (ret[i] == primes[j] * ret[pointer[j]]) {
                    pointer[j] += 1;
                }
            }
        }
        return ret.back();
    }
};