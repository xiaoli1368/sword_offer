#include <iostream>
#include <vector>

class Solution {
public:
    std::vector<int> printMatrix(std::vector<std::vector<int>> matrix) {
        std::vector<int> result;

        if (matrix.size() == 0) {
            return result;
        }

        int top = 0;
        int bottom = matrix.size() - 1;
        int left = 0;
        int right = matrix[0].size() - 1;

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
};

int main(int argc, char* argv[])
{
    Solution s;
    std::vector<std::vector<int>> array = {{1, 2, 3, 4},
                                           {5, 6, 7, 8},
                                           {9, 10, 11, 12},
                                           {13, 14, 15, 16}};
    
    // 打印原始二维矩阵
    // 使用迭代器更加简单
    for (auto i : array) {
        for (auto j : i) {
            std::cout << j << " ";
        }
        std::cout << std::endl;
    }

    std::vector<int> result = s.printMatrix(array);
    for (auto i : result) {
        std::cout << i << " ";
    }
    std::cout << std::endl;

    return 0;
}