class Solution {
public:
    bool checkExist(const char& val, unordered_set<int>& s) {
        if (val != '.' && s.count(val) > 0) {
            return true;
        }
        s.insert(val);
        return false;
    }

    bool isValidSudoku(vector<vector<char>>& board) {
        // 特殊情况
        if (board.size() != 9) {
            return false;
        }

        // 二重循环遍历
        unordered_set<int> rows, cols, grids;
        for (int i = 0; i < 9; i++) {
            rows.clear(), cols.clear(), grids.clear();
            for (int j = 0; j < 9; j++) {
                if (checkExist(board[i][j], rows) || checkExist(board[j][i], cols) || checkExist(board[i/3*3+j/3][i%3*3+j%3], grids)) {
                    return false;
                }
            }
        }
        return true;
    }
};