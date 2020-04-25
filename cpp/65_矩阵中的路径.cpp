class Solution {
public:
    bool hasPath(char* matrix, int rows, int cols, char* str) {
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
                if (haha(matrix, rows, cols, i, j, str, 0, flag)) {
                    return true;
                }
            }
        }
        
        // 没有找到
        delete[] flag;
        return false;
    }
    
    bool haha(char* matrix, int rows, int cols, int i, int j, char* str, int k, bool* flag) {
        // 二维索引处理为一维索引
        int index = i * cols + j;
        
        // 递归的合法性判断，直接返回的情况（出界，不等，已经遍历过）
        if (i < 0 || i > rows || j < 0 || j > cols || matrix[index] != str[k] || flag[index] == true) {
            return false;
        }
        
        // 如果str已经到头了，之前的都找到了，则true
        if (str[k + 1] == '\0') {
            return true;
        }
        
        // 标记当前的位置已经遍历过
        flag[index] = true;
        
        // 递归从四个方向回溯
        if (   haha(matrix, rows, cols, i - 1, j, str, k + 1, flag)
            || haha(matrix, rows, cols, i + 1, j, str, k + 1, flag)
            || haha(matrix, rows, cols, i, j - 1, str, k + 1, flag)
            || haha(matrix, rows, cols, i, j + 1, str, k + 1, flag)) {
            return true;
        }
        
        // 如果没有找到，则标记为没有遍历过
        flag[index] = false;
        return false;
    }

};