class Solution {
public:
    /* 思路：
     * 暴力枚举：先确定左上角，再确定右下角，然后判断这个矩形是否为全1
     * 思考动态规划，求解以(i,j)为右下角的最大矩形面积
     * 该面积和什么有关，area = width * height
     * height 应该是从第i行向上遍历，直到遇到0
     * width 为每当前高度范围内的最短宽度
     * 需要遍历所有的(height, width)组合，找到其中的最大值
     * 定义dp[i][j]表示(i,j)左侧连续1的个数，包含当前位置
     */
    int maximalRectangle(vector<vector<char>>& matrix) {
        if (matrix.empty() || matrix[0].empty()) {
            return 0;
        }

        int ret = 0;
        int row = matrix.size();
        int col = matrix[0].size();
        vector<vector<int>> dp(row, vector<int>(col, 0));

        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                // 仅需要考虑右下角为非0情况
                if (matrix[i][j] == '1') {
                    // 更新dp[i][j]
                    if (j == 0) {
                        dp[i][j] = 1;
                    } else {
                        dp[i][j] = dp[i][j - 1] + 1;
                    }
                    // 更新面积
                    int width = dp[i][j];
                    for (int h = i; h >= 0 && dp[h][j] > 0; h--) {
                        width = min(width, dp[h][j]);
                        ret = max(ret, width * (i - h + 1));
                    }
                }
            }
        }

        return ret;
    }
};