#include <stdio.h>
#include <vector>
#include <string>
#include <map>

#define abs(x) ((x) > 0 ? (x) : (-(x)))

class Solution {
private:
    int cnt = 0;
public:
    // 能否放置棋子
	bool canSet(std::vector<std::pair<int, int>>& chess, int i, int j) {
		for (auto & che : chess) {
			int x = che.first, y = che.second;
			if (x == i || y == j || abs(x-i) == abs(y-j)) {
				return false;
			}
		}
		return true;
	}

	// 回溯法
	void backTracking(std::vector<std::string>& board, std::vector<std::pair<int, int>>& chess, int n, int i) {
		if (i >= n) {
			this->cnt += 1;
			return;
		}
		for (int j = 0; j < n; j++) {
			if (canSet(chess, i, j)) {
				board[i][j] = 'Q';
				chess.push_back(std::pair<int, int>(i, j));
				backTracking(board, chess, n, i + 1);
				board[i][j] = '.';
				chess.pop_back();
			}
		}
	}

    // 外部接口
    int totalNQueens(int n) {
		if (n <= 0) {
			return 0;
		}
		this->cnt = 0;
		std::string tmp(n, '.');
		std::vector<std::string> board(n, tmp);
		std::vector<std::pair<int, int>> chess;
		backTracking(board, chess, n, 0);
		return this->cnt;
	}

	// ===== 更加高效的方式 =====
    void dfs(vector<bool>& cols, vector<bool>& ldiags, vector<bool>& rdiags, int& ret, int n, int i) {
        if (i >= n) {
            ret += 1;
            return;
        }
        for (int j = 0; j < n; j++) {
            int l = n - 1 - i + j, r = i + j;
            if (!cols[j] && !ldiags[l] && !rdiags[r]) {
                cols[j] = ldiags[l] = rdiags[r] = true;
                dfs(cols, ldiags, rdiags, ret, n, i + 1);
                cols[j] = ldiags[l] = rdiags[r] = false;
            }
        }
        return;
    }

    int totalNQueens(int n) {
        if (n <= 0) {
            return 0;
        }
        int ret = 0;
        vector<bool> cols(n, false);
        vector<bool> ldiags(2 * n - 1, false);
        vector<bool> rdiags(2 * n - 1, false);
        dfs(cols, ldiags, rdiags, ret, n, 0);
        return ret;
    }
};

int main(int argc, char* argv[])
{
	Solution s;
	printf("%d\n", s.totalNQueens(4));
	printf("%d\n", s.totalNQueens(8));
	return 0;
}