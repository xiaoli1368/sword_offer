class Solution {
public:
    void dfs(vector<vector<string>>& ret, vector<string>& path, const vector<vector<bool>>& dp, const string& s, const int& n, int i) {
        if (i >= n) {
            ret.push_back(path);
            return;
        }
        for (int j = i; j < n; j++) {
            if (dp[i][j] == true) {
                path.push_back(s.substr(i, j - i + 1));
                dfs(ret, path, dp, s, n, j + 1);
                path.pop_back();
            }
        }
        return;
    }

    vector<vector<string>> partition(string s) {
        vector<vector<string>> ret;
        if (s.empty()) {
            return ret;
        }

        int n = s.size();
        vector<vector<bool>> dp(n, vector<bool>(n, true));
        for (int i = n - 1; i >= 0; i--) {
            for (int j = i + 1; j < n; j++) {
                dp[i][j] = (s[i] == s[j] && dp[i + 1][j - 1]);
            }
        }

        vector<string> path;
        dfs(ret, path, dp, s, n, 0);
        return ret;
    }
};