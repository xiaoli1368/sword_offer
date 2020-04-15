#include <iostream>
#include <vector>

class Solution {
public:
    std::vector<int> FindNumbersWithSum(std::vector<int> array, int sum) {
        std::vector<int> result;
        if (array.empty()) {
            return result;
        }

        int l = 0;
        int h = array.size() - 1;
        int currSum = 0;

        while (l < h) {
            currSum = array[l] + array[h];
            if (currSum == sum) {
                result.push_back(array[l]);
                result.push_back(array[h]);
                return result;
            } else if (currSum < sum) {
                l++;
            } else if (currSum > sum) {
                h--;
            }
        }

        return result;
    }
};

int main(int argc, char* argv[])
{
    Solution s;
    std::vector<int> array = {1, 2, 3, 4, 5, 6, 7}; 
    std::vector<int> result = s.FindNumbersWithSum(array, 6);

    std::cout << result[0] << " " << result[1] << std::endl;
    return 0;
}