class Solution {
public:
    vector<vector<int>> dires = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

	// ===== DFS的方式 =====

    void dfs(vector<vector<int>>& matrix, vector<vector<vector<bool>>>& flag, int row, int col, int index, int i, int j) {
        flag[i][j][index] = 1;
        for (const auto & d : dires) {
            int x = i + d[0];
            int y = j + d[1];
            if (x >= 0 && y >= 0 && x < row && y < col && matrix[x][y] >= matrix[i][j] && flag[x][y][index] == false) {
                dfs(matrix, flag, row, col, index, x, y);
            }
        }
        return;
    }

    vector<vector<int>> pacificAtlantic(vector<vector<int>>& matrix) {
        // 特殊情况
        if (matrix.empty()) {
            return matrix;
        }

        // 初始化
        int row = matrix.size();
        int col = matrix[0].size();
        vector<vector<int>> ret;
        vector<vector<vector<bool>>> flag(row, vector<vector<bool>>(col, vector<bool>(2, false)));

        // 按行水漫金山
        for (int i = 0; i < row; i++) {
            dfs(matrix, flag, row, col, 0, i, 0);
            dfs(matrix, flag, row, col, 1, i, col - 1);
        }

        // 按列水漫金山
        for (int j = 0; j < col; j++) {
            dfs(matrix, flag, row, col, 0, 0, j);
            dfs(matrix, flag, row, col, 1, row - 1, j);
        }

        // 二维遍历
        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                if (flag[i][j][0] && flag[i][j][1]) {
                    ret.push_back(vector<int>{i, j});
                }
            }
        }
        return ret;
    }

	// ===== BFS的方式 =====
    void bfs(vector<vector<int>>& matrix, vector<vector<vector<bool>>>& flag, int row, int col, queue<pair<int, int>>& queue, int index) {
        int i, j, x, y;
        while (!queue.empty()) {
            auto curr = queue.front();
            queue.pop();
            i = curr.first;
            j = curr.second;
            flag[i][j][index] = 1;
            for (const auto & d : dires) {
                x = i + d[0];
                y = j + d[1];
                if (x >= 0 && y >= 0 && x < row && y < col && matrix[x][y] >= matrix[i][j] && flag[x][y][index] == false) {
                    queue.push(make_pair(x, y));
                }
            }
        }
        return;
    }

    vector<vector<int>> pacificAtlantic(vector<vector<int>>& matrix) {
        // 特殊情况
        if (matrix.empty()) {
            return matrix;
        }

        // 初始化
        int row = matrix.size();
        int col = matrix[0].size();
        vector<vector<int>> ret;
        vector<vector<vector<bool>>> flag(row, vector<vector<bool>>(col, vector<bool>(2, false)));
        queue<pair<int, int>> queueP, queueA;

        // 统计水漫金山的两个队列，然后bfs
        for (int i = 0; i < row; i++) {
            queueP.push(make_pair(i, 0));
            queueA.push(make_pair(i, col - 1));
        }
        for (int j = 0; j < col; j++) {
            queueP.push(make_pair(0, j));
            queueA.push(make_pair(row - 1, j));
        }
        bfs(matrix, flag, row, col, queueP, 0);
        bfs(matrix, flag, row, col, queueA, 1);

        // 二维遍历
        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                if (flag[i][j][0] && flag[i][j][1]) {
                    ret.push_back(vector<int>{i, j});
                }
            }
        }
        return ret;
    }
};