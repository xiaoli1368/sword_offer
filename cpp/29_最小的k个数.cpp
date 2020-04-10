#include <iostream>
#include <vector>
#include <algorithm>

class Solution {
public:
    std::vector<int> GetLeastNumbers_Solution(std::vector<int> input, int k) {
        std::vector<int> result;
        if (input.empty() || k > input.size()) {
            return result;
        }

        sort(input.begin(), input.end());
        result.insert(result.begin(), input.begin(), input.begin() + k);
        return result;
    }

    // 打印一维向量
    void print_1d_vec(std::vector<int>& vec) {
        for (auto i : vec) {
            std::cout << i << " ";
        }
        std::cout << std::endl;
    }
};

int main(int argc, char* argv[])
{
    Solution s;
    std::vector<int> input = {4, 5, 1, 6, 2, 7, 3, 8};
    std::vector<int> result = s.GetLeastNumbers_Solution(input, 4);

    s.print_1d_vec(input);
    s.print_1d_vec(result);

    return 0;
}