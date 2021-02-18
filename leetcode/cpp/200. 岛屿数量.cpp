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

	// ===== BFS的方式 =====
    void bfs(vector<vector<char>>& grid, const vector<vector<int>>& dires, int row, int col, int i, int j) {
        grid[i][j] = '2';
        queue<int> queue;
        queue.push(i);
        queue.push(j);
        while (!queue.empty()) {
            i = queue.front();
            queue.pop();
            j = queue.front();
            queue.pop();
            for (const auto & d : dires) {
                int x = i + d[0], y = j + d[1];
                if (x >= 0 && x < row && y >= 0 && y < col && grid[x][y] == '1') {
                    grid[x][y] = '2';
                    queue.push(x);
                    queue.push(y);
                }
            }
        }
        return;
    }

    int numIslands(vector<vector<char>>& grid) {
        // 特殊情况
        if (grid.empty()) {
            return 0;
        }

        // 初始化
        int cnt = 0;
        int row = grid.size(), col = grid[0].size();
        vector<vector<int>> dires = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};

        // 二重循环并进行BFS
        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                if (grid[i][j] == '1') {
                    cnt += 1;
                    bfs(grid, dires, row, col, i, j);
                }
            }
        }
        return cnt;
    }
};