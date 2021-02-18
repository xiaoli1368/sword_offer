class Solution {
public:
    typedef struct Point {
        int x;
        int y;
        Point(int x=0, int y=0) : x(x), y(y) {}
    } Point;

    int orangesRotting(vector<vector<int>>& grid) {
        // 特殊情况
        if (grid.empty()) {
            return 0;
        }

        // 初始化
        queue<Point> queue;
        int newOrange = 0;
        int row = grid.size(), col = grid[0].size();
        vector<Point> dires = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};

        // 遍历更新腐烂/新鲜的橘子信息
        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                if (grid[i][j] == 1) {
                    newOrange += 1;
                } else if (grid[i][j] == 2) {
                    queue.push(Point(i, j));
                }
            }
        }
        if (newOrange == 0) {
            return 0;
        }

        // BFS
        int time = -1, x, y, size;
        while (!queue.empty()) {
            time += 1;
            size = queue.size();
            for (int i = 0; i < size; i++) {
                auto node = queue.front();
                queue.pop();
                for (const auto & d : dires) {
                    x = node.x + d.x;
                    y = node.y + d.y;
                    if (x >= 0 && x < row && y >= 0 && y < col && grid[x][y] == 1) {
                        newOrange -= 1;
                        grid[x][y] = 2;
                        queue.push(Point(x, y));
                    }
                }
            }
        }

        // 返回结果
        return (newOrange == 0 ? time : -1);
    }
};