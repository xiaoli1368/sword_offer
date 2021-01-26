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
};