#include <stdio.h>
#include <vector>
#include <string>
#include <map>

#define abs(x) ((x) > 0 ? (x) : (-(x)))

class Solution {
private:
    std::vector<std::vector<std::string>> ret;
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
			this->ret.push_back(board);
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
	std::vector<std::vector<std::string>> solveNQueens(int n) {
		if (n <= 0) {
			return ret;
		}
		this->ret.clear();
		std::string tmp(n, '.');
		std::vector<std::string> board(n, tmp);
		std::vector<std::pair<int, int>> chess;
		backTracking(board, chess, n, 0);
		return this->ret;
	}

	// 打印结果
	void printf_2d_board(std::vector<std::vector<std::string>> ret) {
		for (auto & board : ret) {
			printf("=====\n");
			for (auto & line : board) {
				printf("%s\n", line.c_str());
			}
		}
	}
};

int main(int argc, char* argv[])
{
	Solution s;
	s.printf_2d_board(s.solveNQueens(4));
	//s.printf_2d_board(s.solveNQueens(8));
	return 0;
}