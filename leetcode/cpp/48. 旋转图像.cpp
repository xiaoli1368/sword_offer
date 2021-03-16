class Solution {
public:
    void rotate(vector<vector<int>>& m) {
        if (m.empty()) {
            return;
        }

        int n = m.size() - 1;
        for (int k = 0; k <= m.size() / 2; k++) {
            for (int i = 0; i <= n - 2 * k - 1; i++) {
                int tmp = m[k][k + i];
                m[k][k + i] = m[n - k - i][k];
                m[n - k - i][k] = m[n - k][n - k - i]; 
                m[n - k][n - k - i] = m[k + i][n - k];
                m[k + i][n - k] = tmp;
            }
        }

        return;
    }
};