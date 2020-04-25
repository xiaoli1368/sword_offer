class Solution {
public:
    int cnt = 0;
    bool* flag;
    
    // 获取a的数位之和
    int sum(int a) {
        int ret = 0;
        while (a != 0) {
            ret += a % 10;
            a /= 10;
        }
        return ret;
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
    
    int movingCount(int threshold, int rows, int cols) {
        // 合理性判断
        if (threshold <= 0 || rows <= 0 || cols <= 0) {
            return cnt;
        }
        
        flag = new bool[rows * cols];
        memset(flag, false, rows * cols);
        
        search(threshold, rows, cols, 0, 0);
        return cnt;
    }
};