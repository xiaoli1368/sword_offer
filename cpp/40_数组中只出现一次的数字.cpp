#include <iostream>
#include <vector>

class Solution {
public:
    void FindNumsAppearOnce(std::vector<int> data, int* num1, int* num2) {
        if (data.empty()) {
            return;
        }

        int diff = 0;
        for (auto i : data) {
            diff ^= i;
        }
        diff &= -diff;

        *num1 = 0;
        *num2 = 0;
        for (auto i : data) {
            if ((i & diff) == 0) {
                *num1 ^= i;
            } else {
                *num2 ^= i;
            }
        }
    }
};

int main(int argc, char* argv[])
{
    Solution s;
    int* num1 = new int;
    int* num2 = new int;
    std::vector<int> data = {2, 4, 3, 6, 3, 2, 5, 5};
    s.FindNumsAppearOnce(data, num1, num2);

    std::cout << *num1 << " " << *num2 << std::endl;
    return 0;
}