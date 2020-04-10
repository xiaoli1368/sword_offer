#include <iostream>
#include <vector>

class Solution {
public:
    int FIndGreatestSumOfSubArray(std::vector<int> array) {
        if (array.empty()) {
            return 0;
        }
        
        int length = array.size();
        if (length == 1) {
            return array[0];
        }

        int curr_sum = array[0];
        int curr_max = array[0];
        for (int i = 1; i < length; i++) {
            if (curr_sum >= 0) {
                curr_sum += array[i];
            } else {
                curr_sum = array[i];
            }

            if (curr_sum > curr_max) {
                curr_max = curr_sum;
            }
        }

        return curr_max;
    }
};

int main(int argc, char* argv[])
{
    Solution s;
    std::vector<int> array = {6, -3, -2, 7, -15, 1, 2, 2};

    int result = s.FIndGreatestSumOfSubArray(array);
    std::cout << result << std::endl;

    return 0;
}