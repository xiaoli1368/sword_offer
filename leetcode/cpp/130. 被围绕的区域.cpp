class Solution {
public:
    // 从遍历找到相连的O
    void dfs(const vector<vector<char>>& board, vector<vector<bool>>& flag, const vector<vector<int>>& dires, int row, int col, int i, int j) {
        // 没有越界，没有遍历过，是O才进行
        if (i >= 0 && j >= 0 && i < row && j < col && flag[i][j] == false && board[i][j] == 'O') {
            // 先进行标记
            flag[i][j] = true;
            // 遍历四个方向
            for (const auto & d : dires) {
                int x = i + d[0];
                int y = j + d[1];
                dfs(board, flag, dires, row, col, x, y);
            }
        }
        return;
    }

    void solve(vector<vector<char>>& board) {
        if (board.empty()) {
            return;
        }

        int row = board.size();
        int col = board[0].size();
        vector<vector<bool>> flag(row, vector<bool>(col, false));
        vector<vector<int>> dires = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};

        // 从边界开始比较连通的位置
        for (int i = 0; i < col; i++) {
            dfs(board, flag, dires, row, col, 0, i);
            dfs(board, flag, dires, row, col, row - 1, i);
        }
        for (int i = 0; i < row; i++) {
            dfs(board, flag, dires, row, col, i, 0);
            dfs(board, flag, dires, row, col, i, col - 1);
        }

        // 找到没有连通到边界的位置，进行填充
        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                if (flag[i][j] == false) {
                    board[i][j] = 'X';
                }
            }
        }
        return;
    }

	// ===== BFS的方式 =====
	void bfs(vector<vector<char>>& board, const vector<vector<int>>& dires, int row, int col, int i, int j) {
        if (board[i][j] != 'O') {
            return;
        }
        int x, y;
        board[i][j] = 'A';
        queue<int> queue;
        queue.push(i);
        queue.push(j);
        while (!queue.empty()) {
            i = queue.front();
            queue.pop();
            j = queue.front();
            queue.pop();
            for (const auto & d : dires) {
                x = i + d[0];
                y = j + d[1];
                if (x >= 0 && x < row && y >= 0 && y < col && board[x][y] == 'O') {
                    queue.push(x);
                    queue.push(y);
                    board[x][y] = 'A';
                }
            }
        }
        return;
    }

    void solve(vector<vector<char>>& board) {
        // 特殊情况
        if (board.empty()) {
            return;
        }

        // 初始化，从边界开始BFS
        int row = board.size(), col = board[0].size();
        vector<vector<int>> dires = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
        for (int i = 0; i < col; i++) {
            bfs(board, dires, row, col, 0, i);
            bfs(board, dires, row, col, row - 1, i);
        }
        for (int i = 0; i < row; i++) {
            bfs(board, dires, row, col, i, 0);
            bfs(board, dires, row, col, i, col - 1);
        }

        // 二重循环遍历，更新标记
        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                if (board[i][j] == 'A') {
                    board[i][j] = 'O';
                } else if (board[i][j] == 'O') {
                    board[i][j] = 'X';
                }
            }
        }
        return;
    }
};