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

	// ===== 堆 =====
    int nthSuperUglyNumber(int n, vector<int>& primes) {
        priority_queue<int, vector<int>, greater<int>> q;
        q.push(1);
        for (int curr, i = 1; i < n; i++) {
            curr = q.top(), q.pop();
            while (!q.empty() && curr == q.top()) {
                q.pop();
            }
            for (const int& p : primes) {
                if (p <= INT_MAX / curr) {
                    q.push(curr * p);
                }
            }
        }
        return q.top();
    }
};