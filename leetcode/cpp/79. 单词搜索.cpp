class Solution {
public:
    bool dfs(const vector<vector<char>>& board, const string& word, const vector<vector<int>>& dires, vector<vector<bool>>& flag, int row, int col, int i, int j, int index) {
        // 如果index越界则说明找到了
        if (index >= word.size()) {
            return true;
        }

        // 如果越界，已经遍历，没有匹配上则没有找到
        if (i < 0 || j < 0 || i >= row || j >= col || flag[i][j] == true || board[i][j] != word[index]) {
            return false;
        }

        // 如果没有越界，没有遍历过，已经匹配，则回溯下一层
        flag[i][j] = true;
        for (const auto & d : dires) {
            int x = i + d[0];
            int y = j + d[1];
            if (dfs(board, word, dires, flag, row, col, x, y, index + 1)) {
                return true;
            }
        }
        flag[i][j] = false;
        return false;
    }

    bool exist(vector<vector<char>>& board, string word) {
        // 特殊情况
        if (board.empty() || word.empty()) {
            return false;
        }

        // 初始化
        int row = board.size();
        int col = board[0].size();
        vector<vector<bool>> flag(row, vector<bool>(col, false));
        vector<vector<int>> dires = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};

        // 找到入口并开始回溯
        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                if (dfs(board, word, dires, flag, row, col, i, j, 0)) {
                    return true;
                }
            }
        }
        return false;
    }
};