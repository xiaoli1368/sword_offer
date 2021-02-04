class Solution {
public:
    void dfs(vector<vector<int>>& grid, vector<vector<bool>>& flag, int row, int col, int i, int j, int& area) {
        if (i < 0 || j < 0 || i >= row || j >= col || grid[i][j] == 0 || flag[i][j] == true) {
            return;
        }
        area += 1;
        flag[i][j] = true;
        dfs(grid, flag, row, col, i + 1, j, area);
        dfs(grid, flag, row, col, i - 1, j, area);
        dfs(grid, flag, row, col, i, j + 1, area);
        dfs(grid, flag, row, col, i, j - 1, area);
        return;
    }

    int maxAreaOfIsland(vector<vector<int>>& grid) {
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
                if (grid[i][j] == 1 && flag[i][j] == false) {
                    int area = 0;
                    dfs(grid, flag, row, col, i, j, area);
                    ret = max(ret, area);
                }
            }
        }
        return ret;
    }
};