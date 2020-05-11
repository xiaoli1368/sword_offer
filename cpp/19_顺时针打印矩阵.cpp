#include <iostream>
#include <vector>
#include <stdio.h>
#include <sys/time.h>

class Solution {
public:
    // 高效解法：将每圈打印分解为四次直线打印
    std::vector<int> printMatrix(std::vector<std::vector<int>> matrix) {
        if (matrix.empty()) {
            return std::vector<int>{};
        }

        int top = 0;
        int left = 0;
        int bottom = matrix.size() - 1;
        int right = matrix[0].size() - 1;
        std::vector<int> result;

        while (top <= bottom && left <= right) {
            for (int i = left; i <= right; i++) {
                result.push_back(matrix[top][i]);
            }
            for (int i = top+1; i <= bottom; i++) {
                result.push_back(matrix[i][right]);
            }
            if (top != bottom) {
                for (int i = right-1; i >= left; i--) {
                    result.push_back(matrix[bottom][i]);
                }
            }
            if (left != right) {
                for (int i = bottom-1; i > top; i--) {
                    result.push_back(matrix[i][left]);
                }
            }

            top++;
            bottom--;
            left++;
            right--;
        } 

        return result;
    }

   // 打印一维矩阵
   void print_1d_vec(std::vector<int>& vec) {
       if (vec.empty()) {
           return;
       }

       for (auto i : vec) {
           std::cout << i << " ";
       }
       std::cout << std::endl;
   }

    // 测试函数
    void test(std::vector<std::vector<int>>& array) {
        std::vector<int> result;
        struct timeval start, end; 
        
        gettimeofday(&start, 0);
        result = this->printMatrix(array);
        gettimeofday(&end, 0);
        
        printf("=====\n");
        printf("times(us): %ld, result: ", end.tv_usec - start.tv_usec);
        this->print_1d_vec(result);
    }
};

int main(int argc, char* argv[])
{
    std::vector<std::vector<int>> array = {{1, 2, 3, 4}};
    std::vector<std::vector<int>> array2 = {{1}, {5}, {9}, {13}};
    std::vector<std::vector<int>> array3 = {{1, 2, 3, 4},
                                           {5, 6, 7, 8},
                                           {9, 10, 11, 12},
                                           {13, 14, 15, 16}};
    
    Solution s;
    s.test(array);
    s.test(array2);
    s.test(array3);

    return 0;
}