#include <iostream>
#include <vector>
#include <algorithm>

class Solution {
public:
    // 个人解法
    bool IsContinuous(std::vector<int> numbers) {
        if (numbers.size() != 5) {
            return false;
        }

        int min = 14;
        int max = 0;
        int zero_cnt = 0;

        for (auto i : numbers) {
            if (i < 0 && i > 13) {
                return false;
            } else if (i == 0) {
                zero_cnt++;
                continue;
            }
            
            // 位于[1, 13]
            if (i < min) {
                min = i;
            }
            if (i > max) {
                max = i;
            }
        }

        if (zero_cnt == 4 || (max - min <= 4 && min != max)) {
            return true;
        } else {
            return false;
        }
    }

    // 参考答案解法
    bool IsContinuous2(std::vector<int> numbers) {
        if (numbers.size() != 5) {
            return false;
        }
        sort(numbers.begin(), numbers.end());

        int cnt = 0;
        for (auto i : numbers) {
            if (i == 0) {
                cnt++;
            }
        }

        // 从没有癞子的地方开始，使用癞子去补全顺子
        for (int i = cnt; i < numbers.size() - 1; i++) {
            if (numbers[i] == numbers[i + 1]) {
                return false;
            }
            // 差值为n，则使用n个癞子进行补全
            cnt -= numbers[i + 1] - numbers[i] - 1;
        }

        return cnt >= 0;
    }
};

int main(int argc, char* argv[])
{
    Solution s;
    std::vector<int> numbers = {1, 3, 0, 0, 5};

    std::cout << s.IsContinuous(numbers) << std::endl;
    std::cout << s.IsContinuous2(numbers) << std::endl;
    return 0;
}