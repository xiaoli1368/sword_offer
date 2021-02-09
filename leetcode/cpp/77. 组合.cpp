class Solution {
public:
    void dfs(vector<vector<int>>& ret, vector<int>& path, int n, int k, int i) {
        int size = path.size();
        if (size == k) {
            ret.push_back(path);
            return;
        }
        for (int j = i; j <= n + 1 + size - k; j++) {
            path.push_back(j);
            dfs(ret, path, n, k, j + 1);
            path.pop_back();
        }
        return;
    }

    vector<vector<int>> combine(int n, int k) {
        vector<int> path;
        vector<vector<int>> ret;
        if (n < 1 || k > n) {
            return ret;
        }
        dfs(ret, path, n, k, 1);
        return ret;
    }
};