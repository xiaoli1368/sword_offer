class Solution {
public:
    int uniquePathsWithObstacles(vector<vector<int>>& grid) {
        if (grid.empty()) {
            return 0;
        }
        for (int i = 0; i < grid.size(); i++) {
            for (int j = 0; j < grid[0].size(); j++) {
                grid[i][j] = 1 - grid[i][j];
                if (grid[i][j] == 0 || (i == 0 && j == 0)) {
                    continue;
                }
                int top = (i >= 1 ? grid[i - 1][j] : 0);
                int lef = (j >= 1 ? grid[i][j - 1] : 0);
                grid[i][j] = top + lef;
            }
        }
        return grid.back().back();
    }
};