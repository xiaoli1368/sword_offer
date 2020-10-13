#include <stdio.h>
#include <vector>
#include <algorithm>

class Solution {
public:
    // 使用API建堆
    std::vector<int> getAllTopk(std::vector<int>& num, int k) {

    }

    // 建立大顶堆
    void heapify(std::vector<int>& num, int n, int i) {

    }

    // 自行构建堆
    std::vector<int> getAllTopk2(std::vector<int>& num, int k) {

    }

    // 打印一维数组
    void printf_1d_vec(std::vector<int>& vec) {
        for (auto & i : vec) {
            printf("%d, ", i);
        }
        printf("\n");
    }
};

int main(int argc, char* argv[])
{
    int k = 5;
    std::vector<int> num = {3, 0, 5, 8, 3, 3, 4, 9, 1};
    Solution s;
    s.printf_1d_vec(s.getAllTopk(num, k));
    s.printf_1d_vec(s.getAllTopk2(num, k));
    return 0;
}