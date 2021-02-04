#include <vector>
using namespace std;

class Solution {
public:
    void dfs(vector<vector<int>>& grid, vector<vector<bool>>& flag, int& ret, int n, int m, int i, int j) {
        if (i < 0 || j < 0 || i >= n || j >= m || grid[i][j] == 0) {
            ret += 1;
            return;
        }
        if (flag[i][j] == true) {
            return;
        }
        flag[i][j] = true;
        dfs(grid, flag, ret, n, m, i - 1, j);
        dfs(grid, flag, ret, n, m, i + 1, j);
        dfs(grid, flag, ret, n, m, i, j - 1);
        dfs(grid, flag, ret, n, m, i, j + 1);
        return;
    }

    int islandPerimeter(vector<vector<int>>& grid) {
        int ret = 0;
        int n = grid.size();
        int m = grid[0].size();
        vector<vector<bool>> flag(n, vector<bool>(m, false));

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (grid[i][j] == 1) {
                    dfs(grid, flag, ret, n, m, i, j);
                    return ret;
                }
            }
        }
        return 0;
    }

	// ===== 二重循环方法 =====
	int islandPerimeter(vector<vector<int>>& grid) {
        if (grid.empty()) {
            return 0;
        }

        int ret = 0;
        int row = grid.size();
        int col = grid[0].size();
        vector<vector<int>> dires = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};

        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                // 保证当前位置为陆地
                if (grid[i][j] == 1) {
                    // 遍历四个方向判断是否为水域
                    for (const auto & d : dires) {
                        int x = i + d[0];
                        int y = j + d[1];
                        if (x < 0 || y < 0 || x >= row || y >= col || grid[x][y] == 0) {
                            ret += 1;
                        }
                    }
                }
            }
        }
        return ret;
    }
};