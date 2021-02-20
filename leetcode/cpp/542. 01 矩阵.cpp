// 注意好像unordered_set不能直接使用pair作为key，需要传入额外的hash函数
// 但是set可以
#include <unordered_set>
class Solution {
public:
    vector<vector<int>> updateMatrix(vector<vector<int>>& matrix) {
        if (matrix.empty() || matrix[0].empty()) {
            return matrix;
        }

        int row = matrix.size();
        int col = matrix[0].size();
        queue<pair<int, int>> queue;
        set<pair<int, int>> visited;
        vector<vector<int>> ret(row, vector<int>(col, 0));
        vector<vector<int>> dires = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};

        // 找到第一级阶梯
        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                if (matrix[i][j] == 1) {
                    // 遍历四个方向，查看是否有0相邻
                    for (auto & d : dires) {
                        int x = i + d[0];
                        int y = j + d[1];
                        if (x >= 0 && x < row && y >= 0 && y < col && matrix[x][y] == 0) {
                            auto point = make_pair(i, j);
                            queue.push(point);
                            visited.insert(point);
                            break;
                        }
                    }
                }
            }
        }

        // 进行BFS
        int k = 0, size = 0;
        while (!queue.empty()) {
            k += 1;
            size = queue.size();
            for (int it = 0; it < size; it++) {
                int i = queue.front().first;
                int j = queue.front().second;
                queue.pop();
                ret[i][j] = k;
                // 遍历添加下一层
                for (auto & d : dires) {
                    int x = i + d[0];
                    int y = j + d[1];
                    auto point = make_pair(x, y);
                    if (x >= 0 && x < row && y >= 0 && y < col && matrix[x][y] == 1 && visited.count(point) == 0) {
                        queue.push(point);
                        visited.insert(point);
                    }
                }
            }
        }

        // 返回结果
        return ret;
    }

    // ===== 个人优化版本 =====
	typedef struct Point {
        int x;
        int y;
        Point(int x=0, int y=0) : x(x), y(y) {}
    } Point;

    vector<vector<int>> updateMatrix(vector<vector<int>>& matrix) {
        // 特殊情况
        if (matrix.empty()) {
            return vector<vector<int>>{};
        }

        // 初始化
        queue<Point> queue;
        int row = matrix.size(), col = matrix[0].size();
        vector<Point> dires = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
        vector<vector<int>> ret(row, vector<int>(col, 0));
        vector<vector<bool>> flag(row, vector<bool>(col, false));
        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                if (matrix[i][j] == 0) {
                    flag[i][j] = true;
                    queue.push(Point(i, j));
                }
            }
        }

        // BFS
        int step = 0, size, x, y;
        while (!queue.empty()) {
            step += 1;
            size = queue.size();
            for (int k = 0; k < size; k++) {
                auto node = queue.front();
                queue.pop();
                for (const auto & d : dires) {
                    x = node.x + d.x;
                    y = node.y + d.y;
                    if (x >= 0 && x < row && y >= 0 && y < col && flag[x][y] == false) {
                        ret[x][y] = step;
                        flag[x][y] = true;
                        queue.push(Point(x, y));
                    }
                }
            }
        }
        return ret;
    }

	// ===== 四个方向遍历 =====
    // 由于矩阵中至少含有一个0，因此所有元素初始化为最大值
    // 为了防止int越界，元素初始化最大值不选择INT_MAX，而选取row+col
    vector<vector<int>> updateMatrix(vector<vector<int>>& matrix) {
        if (matrix.empty()) {
            return matrix;
        }
        int row = matrix.size(), col = matrix[0].size();
        vector<vector<int>> dp(row, vector<int>(col, row + col));
        
        // 行
        for (int i = 0; i < row; i++) {
            // 从左到右
            for (int j = 0; j < col; j++) {
                if (matrix[i][j] == 0) {
                    dp[i][j] = 0;
                } else if (matrix[i][j] == 1 && j >= 1) {
                    dp[i][j] = 1 + dp[i][j - 1];
                }
            }
            // 从右到左
            for (int j = col - 2; j >= 0; j--) {
                if (matrix[i][j] == 1) {
                    dp[i][j] = min(dp[i][j], 1 + dp[i][j + 1]);
                }
            }
        }

        // 列
        for (int j = 0; j < col; j++) {
            // 从上到下
            for (int i = 1; i < row; i++) {
                if (matrix[i][j] == 1) {
                    dp[i][j] = min(dp[i][j], 1 + dp[i - 1][j]);
                }
            }
            // 从下到上
            for (int i = row - 2; i >= 0; i--) {
                if (matrix[i][j] == 1) {
                    dp[i][j] = min(dp[i][j], 1 + dp[i + 1][j]);
                }
            }
        }
        return dp;
    }

	// ===== 从对角线方向遍历 =====
    vector<vector<int>> updateMatrix(vector<vector<int>>& matrix) {
        if (matrix.empty()) {
            return matrix;
        }
        int row = matrix.size(), col = matrix[0].size();
        vector<vector<int>> dp(row, vector<int>(col, row + col));
        
        // 从左上到右下
        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                if (matrix[i][j] == 0) {
                    dp[i][j] = 0;
                    continue;
                }
                if (i >= 1) dp[i][j] = min(dp[i][j], 1 + dp[i - 1][j]);
                if (j >= 1) dp[i][j] = min(dp[i][j], 1 + dp[i][j - 1]);
            }
        }
        
        // 从右下到左上
        for (int i = row - 1; i >= 0; i--) {
            for (int j = col - 1; j >= 0; j--) {
                if (matrix[i][j] == 0) {
                    continue;
                }
                if (i <= row - 2) dp[i][j] = min(dp[i][j], 1 + dp[i + 1][j]);
                if (j <= col - 2) dp[i][j] = min(dp[i][j], 1 + dp[i][j + 1]);
            }
        }

        return dp;
    }
};