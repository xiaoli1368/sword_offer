class Solution {
public:
    int minPathSum(vector<vector<int>>& grid) {
        if (grid.empty()) {
            return 0;
        }
        for (int i = 0; i < grid.size(); i++) {
            for (int j = 0; j < grid[0].size(); j++) {
                if (i == 0 && j == 0) continue;
                int top = (i >= 1 ? grid[i - 1][j] : INT_MAX);
                int lef = (j >= 1 ? grid[i][j - 1] : INT_MAX);
                grid[i][j] += min(top, lef);
            }
        }
        return grid.back().back();
    }
};