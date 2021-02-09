class Solution {
public:
    void dfs(vector<vector<int>>& ret, vector<int>& path, int n, int k, int i) {
        if (n == 0 && path.size() == k) {
            ret.push_back(path);
        } else if (n > 0 && i <= 9) {
            for (int j = i; j <= 9; j++) {
                path.push_back(j);
                dfs(ret, path, n - j, k, j + 1);
                path.pop_back();
            }
        }
        return;
    }

    vector<vector<int>> combinationSum3(int k, int n) {
        vector<int> path;
        vector<vector<int>> ret;
        if (k > 0 && n >= 1 && n <= 9 * k) {
            dfs(ret, path, n, k, 1);
        }
        return ret;
    }
};