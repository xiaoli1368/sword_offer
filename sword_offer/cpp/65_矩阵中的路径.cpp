#include <iostream>
#include <vector>
#include <cstring>
#include <stdio.h>
#include <sys/time.h>

class Solution {
public:
    // ===== 第一次的方式 =====
    bool hasPath1(char* matrix, int rows, int cols, char* str) {
        // 合法性判断
        if (matrix == nullptr || str == nullptr || rows <= 0 || cols <= 0) {
            return false;
        }
        
        // 标记是否遍历过的数组
        bool* flag = new bool[rows * cols];
        memset(flag, false, rows * cols);
        
        // 遍历整个数组，作为起点，haha判断是否找到路径
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (checkPath1(matrix, rows, cols, i, j, str, 0, flag)) {
                    return true;
                }
            }
        }
        
        // 没有找到
        delete[] flag;
        return false;
    }
    
    bool checkPath1(char* matrix, int rows, int cols, int i, int j, char* str, int k, bool* flag) {
        // 二维索引处理为一维索引
        int index = i * cols + j;
        
        // 递归的合法性判断，直接返回的情况（出界，不等，已经遍历过）
        if (i < 0 || i >= rows || j < 0 || j >= cols || matrix[index] != str[k] || flag[index] == true) {
            return false;
        }
        
        // 如果str已经到头了，之前的都找到了，则true
        if (str[k + 1] == '\0') {
            return true;
        }
        
        // 标记当前的位置已经遍历过
        flag[index] = true;
        
        // 递归从四个方向回溯
        if (   checkPath1(matrix, rows, cols, i - 1, j, str, k + 1, flag)
            || checkPath1(matrix, rows, cols, i + 1, j, str, k + 1, flag)
            || checkPath1(matrix, rows, cols, i, j - 1, str, k + 1, flag)
            || checkPath1(matrix, rows, cols, i, j + 1, str, k + 1, flag)) {
            return true;
        }
        
        // 如果没有找到，则标记为没有遍历过
        flag[index] = false;
        return false;
    }

    // ===== 第二次，优化版 =====
    bool hasPath(char* matrix, int rows, int cols, char* str) {
        if (matrix == nullptr || str == nullptr || rows <= 0 || cols <= 0) {
            return false;
        }

        bool* flag = new bool[rows * cols];
        memset(flag, false, rows * cols);

        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (checkPath(matrix, str, flag, rows, cols, i, j, 0)) {
                    return true;
                }
            }
        }

        // 注意delete
        delete [] flag;
        return false;
    }

    bool checkPath(char* matrix, char* str, bool* flag, int rows, int cols, int i, int j, int k) {
        // 找到路径的判断
        if (str[k] == '\0') {
            return true;
        }

        // 各处错误判断
        int index = i * cols + j;
        if (i < 0 || i >= rows || j < 0 || j > cols || flag[index] == true || str[k] != matrix[index]) {
            return false;
        }

        // 此时：str[k] == maxtrix[index]
        flag[index] = true;
        if (checkPath(matrix, str, flag, rows, cols, i + 1, j, k + 1) ||
            checkPath(matrix, str, flag, rows, cols, i - 1, j, k + 1) ||
            checkPath(matrix, str, flag, rows, cols, i, j + 1, k + 1) ||
            checkPath(matrix, str, flag, rows, cols, i, j - 1, k + 1)) {
            return true;         // 从四个方向递归回溯，找到了路径
        } else {
            flag[index] = false; // 注意这里要恢复flag
            return false;        // 四个方向都没有找到
        }
    }

    // 测试函数
    void test(char* matrix, int rows, int cols, char* str) {
        bool result = false;
        struct timeval start, end;
        printf("=====\n");
        for (auto func : this->func_vec_) {
            gettimeofday(&start, nullptr);
            result = (this->*func)(matrix, rows, cols, str);
            gettimeofday(&end, nullptr);
            printf("result: %d, time(us): %ld\n", result, end.tv_usec - start.tv_usec);
        }
    }

	// ===== leetcode中的解法 =====
	bool dfs(const vector<vector<char>>& board, const string& word, vector<vector<bool>>& flag, const vector<vector<int>>& dires, int row, int col, int n, int i, int j, int index) {
        if (index >= n) {
            return true;
        }
        if (i < 0 || j < 0 || i >= row || j >= col || flag[i][j] == true || board[i][j] != word[index]) {
            return false;
        }
        flag[i][j] = true;
        for (const auto & d : dires) {
            int x = i + d[0];
            int y = j + d[1];
            if (dfs(board, word, flag, dires, row, col, n, x, y, index + 1)) {
                return true;
            }
        }
        flag[i][j] = false;
        return false;
    }

    bool exist(vector<vector<char>>& board, string word) {
        if (word.empty()) {
            return true;
        }
        if (board.empty()) {
            return false;
        }
        int n = word.size();
        int row = board.size();
        int col = board[0].size();
        vector<vector<bool>> flag(row, vector<bool>(col, false));
        vector<vector<int>> dires = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                if (dfs(board, word, flag, dires, row, col, n, i, j, 0)) {
                    return true;
                }
            }
        }
        return false;
    }

private:
    typedef bool (Solution::*func_ptr)(char*, int, int, char*);
    std::vector<func_ptr> func_vec_ = {&Solution::hasPath1, &Solution::hasPath};

};

int main(int argc, char* argv[])
{
    char* matrix = (char*)"aa";
    char* str = (char*)"aaa";

    char* matrix2 = (char*)"ABCESFCSADEE";
    char* str2 = (char*)"ABCCED";

    char* matrix3 = (char*)"abcd";
    char* str3 = (char*)"abcd";

    char* matrix4 = (char*)"abcesfcsadee";
    char* str4 = (char*)"fcsecbasadee";

    Solution s;
    s.test(matrix, 1, 2, str);
    s.test(matrix2, 3, 4, str2);
    s.test(matrix3, 2, 2, str3);
    s.test(matrix4, 3, 4, str4);

    return 0;
}