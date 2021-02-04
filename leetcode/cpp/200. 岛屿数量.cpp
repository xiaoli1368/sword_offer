class Solution {
public:
    void dfs(vector<vector<char>>& grid, vector<vector<bool>>& flag, int row, int col, int i, int j) {
        if (i < 0 || j < 0 || i >= row || j >= col || grid[i][j] == '0' || flag[i][j] == true) {
            return;
        }
        flag[i][j] = true;
        dfs(grid, flag, row, col, i + 1, j);
        dfs(grid, flag, row, col, i - 1, j);
        dfs(grid, flag, row, col, i, j + 1);
        dfs(grid, flag, row, col, i, j - 1);
        return;
    }

    int numIslands(vector<vector<char>>& grid) {
        // 特殊情况
        if (grid.empty()) {
            return 0;
        }

        // 初始化
        int ret = 0;
        int row = grid.size();
        int col = grid[0].size();
        vector<vector<bool>> flag(row, vector<bool>(col, false));

        // 找打入口
        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                if (grid[i][j] == '1' && flag[i][j] == false) {
                    ret += 1;
                    dfs(grid, flag, row, col, i, j);
                }
            }
        }
        return ret;
    }
};