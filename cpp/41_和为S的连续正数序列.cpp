#include <iostream>
#include <vector>

class Solution {
public:
    // 用于添加的函数
    void add_vec(std::vector<std::vector<int>>& vec, int l, int h) {
        if (l <= 0) {
            return;
        }

        std::vector<int> tmp;
        for (int i = l; i <= h; i++) {
            tmp.push_back(i);
        }
        vec.push_back(tmp);
    }

    // 高效解法
    std::vector<std::vector<int>> FindContinuousSequence(int sum) {
        std::vector<std::vector<int>> result;
        if (sum < 3) {
            return result;
        }

        int l = 1;
        int h = 2;
        int currSum = 3;

        while (h <= sum / 2 + 1) {
            if (currSum > sum) {
                currSum -= l;
                l++;
            } else if (currSum < sum) {
                h++;
                currSum += h;
            } else {
                // 此时相等
                add_vec(result, l, h);
                currSum -= l;
                l++;
            }
        }
        
        return result;
    }

    // 常规解法（个人）
    std::vector<std::vector<int>> FindContinuousSequence2(int sum) {
        std::vector<std::vector<int>> result;
        if (sum < 3) {
            return result;
        }

        int l = 0;
        int h = 0;
        int midTwice = 0;
        int num = sum / 2 + 1;

        while (num >= 2) {
            if ((sum * 2) % num == 0) { // 存在约数
                midTwice = (sum * 2) / num;
                if (num % 2 == 1 && midTwice % 2 == 0) {
                    l = midTwice / 2 - num / 2;
                    h = midTwice / 2 + num / 2;
                    add_vec(result, l, h);
                } else if (num % 2 == 0 && midTwice % 2 == 1) {
                    l = midTwice / 2 - num / 2 + 1;
                    h = midTwice / 2 + num / 2;
                    add_vec(result, l, h);
                }
            }
            num--;
        }
        return result;
    }

    // 打印二维数组
    void print_2d_vec(std::vector<std::vector<int>>& vec) {
        for (auto i : vec) {
            for (auto j : i) {
                std::cout << j << " ";
            }
            std::cout << std::endl;
        }
    }
};

int main(int argc, char* argv[])
{
    Solution s;
    std::vector<std::vector<int>> result;
    
    result = s.FindContinuousSequence(100);
    s.print_2d_vec(result);
    std::cout << "===== this is a compare line =====" << std::endl;
    result = s.FindContinuousSequence2(100);
    s.print_2d_vec(result);

    return 0;

}