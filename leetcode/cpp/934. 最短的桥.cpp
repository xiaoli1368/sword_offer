class Solution {
public:
    typedef struct Point {
        int x;
        int y;
        Point(int x=0, int y=0) : x(x), y(y) {}
    } Point;

    void dfs(const vector<vector<int>>& vec, vector<vector<bool>>& flag, const vector<vector<int>>& dires, queue<Point>& queue, int row, int col, int i, int j) {
        if (i >= 0 && i < row && j >= 0 && j < col && flag[i][j] == false && vec[i][j] == 1) {
            flag[i][j] = true;
            queue.push(Point(i, j));
            for (const auto & d : dires) {
                int x = i + d[0], y = j + d[1];
                dfs(vec, flag, dires, queue, row, col, x, y);
            }
        }
        return;
    }

    int bfs(const vector<vector<int>>& vec, vector<vector<bool>>& flag, const vector<vector<int>>& dires, queue<Point>& queue, int row, int col) {
        int step = 0, size, x, y;
        while (!queue.empty()) {
            size = queue.size();
            for (int i = 0; i < size; i++) {
                auto p = queue.front();
                queue.pop();
                for (const auto & d : dires) {
                    x = p.x + d[0];
                    y = p.y + d[1];
                    if (x >= 0 && x < row && y >= 0 && y < col && flag[x][y] == false) {
                        if (vec[x][y] == 1) {
                            return step;
                        } else {
                            flag[x][y] = true;
                            queue.push(Point(x, y));
                        }
                    }
                }
            }
            step += 1;
        }
        return step;
    }

    int shortestBridge(vector<vector<int>>& A) {
        // 特殊情况
        if (A.empty()) {
            return 0;
        }
        // 初始化
        queue<Point> queue;
        int row = A.size(), col = A[0].size();
        vector<vector<bool>> flag(row, vector<bool>(col, false));
        vector<vector<int>> dires = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
        // 找到第一个岛屿，并进行DFS/BFS
        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                if (A[i][j] == 1) {
                    dfs(A, flag, dires, queue, row, col, i, j);
                    return bfs(A, flag, dires, queue, row, col);
                }
            }
        }
        return 0;
    }
};