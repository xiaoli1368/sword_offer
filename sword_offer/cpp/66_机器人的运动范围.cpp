#include <iostream>
#include <cstring>
#include <vector>
#include <stdio.h>
#include <sys/time.h>

class Solution {
public:
    int cnt = 0; // 最终输出结果
    bool* flag;  // 类内变量，标记数组

    // ===== 第一次解法 =====
    // 回溯法，存在较大优化空间
    int movingCount1(int threshold, int rows, int cols) {
        // 合理性判断
        if (threshold < 0 || rows < 0 || cols < 0) {
            return 0;
        }
        
        this->cnt = 0; 
        this->flag = new bool[rows * cols];
        memset(this->flag, false, rows * cols);
        
        search(threshold, rows, cols, 0, 0);
        return this->cnt;
    }

    void search(int threshold, int rows, int cols, int i, int j) {
        int index = i * cols + j;
        
        // 出界或者已经遍历过了，返回
        if (i < 0 || i >= rows || j < 0 || j >= cols || flag[index] == true) {
            return;
        }
        
        // 大于门限返回
        if (sum(i) + sum(j) > threshold) {
            return;
        }
        
        // 当前格子可以进入
        flag[index] = true;
        cnt++;
        
        search(threshold, rows, cols, i + 1, j);
        search(threshold, rows, cols, i - 1, j);
        search(threshold, rows, cols, i, j - 1);
        search(threshold, rows, cols, i, j + 1);
        
    }

    // ===== 优化版回溯法 =====
    // 将遍历方向调整为只搜索右方和上方
    int movingCount(int threshold, int rows, int cols) {
        if (rows < 0 || cols < 0 || threshold < 0) {
            return 0;
        }

        this->cnt = 0;
        this->flag = new bool[rows * cols];
        memset(this->flag, false, rows * cols);

        checkPath(threshold, rows, cols, 0, 0);
        return this->cnt;
    }

    void checkPath(int threshold, int rows, int cols, int i, int j) {
        // 直接返回的条件：出界，当前方格已标记，当前方格不可进入
        int index = i * cols + j;
        if (i >= rows || j >= cols || this->flag[index] || sum(i) + sum(j) > threshold) {
            return;
        }

        // 此时当前方格可以进入
        this->flag[index] = true;
        this->cnt++;

        checkPath(threshold, rows, cols, i + 1, j); // 检测上方
        checkPath(threshold, rows, cols, i, j + 1); // 检测下方
        return;
    }

    // ===== 工具函数 =====

    // 获取a的数位之和
    int sum(int a) {
        int ret = 0;
        while (a != 0) {
            ret += a % 10;
            a /= 10;
        }
        return ret;
    }

    // 测试函数
    void test(int threshold, int rows, int cols) {
        int result = 0;
        struct timeval start, end;
        printf("=====\n");
        for (auto func : func_vec_) {
            gettimeofday(&start, nullptr);
            result = (this->*func)(threshold, rows, cols);
            gettimeofday(&end, nullptr);
            printf("result: %d, time(us): %ld\n", result, end.tv_usec - start.tv_usec);
        }
    }

    // ===== leetcode中的解法 =====
    int getVal(int x, int y) {
        int ret = 0;
        while (x || y) {
            ret += x % 10 + y % 10;
            x /= 10;
            y /= 10;
        }
        return ret;
    }

    void dfs(vector<vector<bool>>& flag, vector<vector<int>>& dires, int& ret, int row, int col, int k, int i, int j) {
        if (i >= 0 && i < row && j >= 0 && j < col && flag[i][j] == false) {
            flag[i][j] = true;
            if (getVal(i, j) <= k) {
                ret += 1;
                for (const auto & d : dires) {
                    int x = i + d[0];
                    int y = j + d[1];
                    dfs(flag, dires, ret, row, col, k, x, y);
                }
            }
        }
        return;
    }

    int movingCount(int m, int n, int k) {
        if (m <= 0 || n <= 0 || k < 0) {
            return 0;
        }
        int ret = 0;
        vector<vector<bool>> flag(m, vector<bool>(n, false));
        vector<vector<int>> dires = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
        dfs(flag, dires, ret, m, n, k, 0, 0);
        return ret;
    }

private:
    typedef int (Solution::*func_ptr)(int, int, int);
    std::vector<func_ptr> func_vec_ = {&Solution::movingCount1, &Solution::movingCount};
};

int main(int argc, char* argv[])
{
    Solution s;
    s.test(2, 2, 3);
    s.test(3, 1, 0);
    s.test(0, 3, 1);
    s.test(18, 40, 40);
    s.test(10, 40, 40);

    return 0;
}