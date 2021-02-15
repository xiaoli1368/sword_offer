class Solution {
public:
    bool isValid(vector<vector<char>>& board, int i, int j, char k) {
        for (int p = 0; p < 9; p++) {
            if (board[i][p] == k ||
                board[p][j] == k ||
                board[i/3*3 + p/3][j/3*3 + p%3] == k) {
                return false;
            }
        }
        return true;
    }

    bool perm(vector<vector<char>>& board, vector<vector<int>>& lst, int cnt) {
        if (cnt >= lst.size()) {
            return true;
        }
        for (int index = cnt; index < lst.size(); index++) {
            int x = lst[index][0];
            int y = lst[index][1];
            for (int k = '1'; k <= '9'; k++) {
                if (isValid(board, x, y, k)) {
                    board[x][y] = k;
                    if (perm(board, lst, cnt + 1)) {
                        return true;
                    }
                    board[x][y] = '.';
                }
            }
            if (board[x][y] == '.') {
                break;
            }
        }
        return false;
    }

    void solveSudoku(vector<vector<char>>& board) {
        if (board.empty()) {
            return;
        }

        vector<vector<int>> lst;
        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                if (board[i][j] == '.') {
                    lst.push_back(vector<int>{i, j});
                }
            }
        }

        perm(board, lst, 0);
    }

	// ===== 其它优化方法 =====
	bool dfs(vector<vector<char>>& board, const vector<vector<int>>& pos, vector<vector<bool>>& rows, vector<vector<bool>>& cols, vector<vector<bool>>& grids, int index) {
        if (index >= pos.size()) {
            return true;
        }
        int i = pos[index][0], j = pos[index][1];
        int ind = i / 3 * 3 + j / 3;
        for (int val = 1; val <= 9; val++) {
            if (!rows[i][val] && !cols[j][val] && !grids[ind][val]) {
                board[i][j] = '0' + val;
                rows[i][val] = cols[j][val] = grids[ind][val] = true;
                if (dfs(board, pos, rows, cols, grids, index + 1)) {
                    return true;
                }
                rows[i][val] = cols[j][val] = grids[ind][val] = false;
                board[i][j] = '.';
            }
        }
        return false;
    }

    void solveSudoku(vector<vector<char>>& board) {
        // 特殊情况
        if (board.empty()) {
            return;
        }
        // 初始化
        vector<vector<int>> pos;
        vector<bool> tmp(10, false);
        vector<vector<bool>> rows(9, tmp), cols(9, tmp), grids(9, tmp);
        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                if (board[i][j] == '.') {
                    pos.push_back(vector<int>{i, j});
                } else {
                    int val = board[i][j] - '0';
                    int ind = i / 3 * 3 + j / 3;
                    rows[i][val] = cols[j][val] = grids[ind][val] = true;
                }
            }
        }
        // 正式遍历
        dfs(board, pos, rows, cols, grids, 0);
        return;
    }
};