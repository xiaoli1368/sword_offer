#include <iostream>
#include <vector>
#include <algorithm>

class Solution {
public:
    int MoreThanHalfNum_Solution(std::vector<int> numbers) {
        sort(numbers.begin(), numbers.end());

        int length = numbers.size();
        int first = 0;
        int end = first + length / 2;

        while (end < length) {
            if (numbers[first] == numbers[end]) {
                return numbers[first];
            }
            first++;
            end++;
        }
        return 0;
    }
};

int main(int argc, char* argv[])
{
    Solution s;
    std::vector<int> numbers = {1, 2, 3, 2, 2, 2, 5, 4, 2};
    
    int result = s.MoreThanHalfNum_Solution(numbers);
    std::cout << result << std::endl;

    return 0;
}