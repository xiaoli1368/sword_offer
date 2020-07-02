#include <iostream>
#include <vector>
#include <stdio.h>
#include <sys/time.h>

class Solution {
public:
    // 第一次的个人解法，比较麻烦
    bool IsPopOrder1(std::vector<int> pushV, std::vector<int> popV) {
        if (pushV.size() == 0 || popV.size() == 0) {
            return false;
        }

        int length = pushV.size();
        int pair = 0;
        std::vector<int> tmp;
        tmp.push_back(pushV.front());

        while (pair < length) {
            if (tmp.back() != popV.front()) {
                if (pushV.size() > 0) {
                    tmp.push_back(pushV.front());
                    pushV.erase(pushV.begin());
                } else {
                    return false;
                }
            } else {
                tmp.pop_back();
                popV.erase(popV.begin());
                pair++;
            }
        }

        return true;
    }

    // 高效答案，模拟实际的删除
    bool IsPopOrder2(std::vector<int> pushV, std::vector<int> popV) {
        if (pushV.size() == 0 || popV.size() == 0) {
            return false;
        }

        std::vector<int> stack;
        for (auto i : pushV) {
            stack.push_back(i);
            while (stack.size() > 0 && stack.back() == popV.front()) {
                // 删除尾部元素的时候使用迭代器会失效
                // 删除首部元素好像就可以
                //stack.erase(std::end(stack));
                stack.pop_back();
                popV.erase(std::begin(popV));
            }
        }

        if (stack.size() == 0) {
            return true;
        } else {
            return false;
        }
    }

    // 高效答案，小细节：使用计数代替出栈
    bool IsPopOrder3(std::vector<int> pushV, std::vector<int> popV) {
        if (pushV.empty() || popV.empty()) {
            return false;
        }

        int i = 0;
        std::vector<int> stack;
        for (auto num : pushV) {
            stack.push_back(num);
            while (!stack.empty() && stack.back() == popV[i]) {
                i++;
                stack.pop_back();
            }
        }

        return stack.empty();
    }

    // 测试函数
    void test(std::vector<int>& pushV, std::vector<int>& popV) {
        bool result;
        struct timeval start, end;

        printf("=====\n");
        for (auto & func : this->func_vec_) {
            gettimeofday(&start, nullptr);
            result = (this->*func)(pushV, popV);
            gettimeofday(&end, nullptr);

            printf("result: %d, time(us): %ld\n", result, end.tv_usec - start.tv_usec);
        }
    }

private:
    typedef bool (Solution::*func_ptr)(std::vector<int>, std::vector<int>);
    std::vector<func_ptr> func_vec_ = {&Solution::IsPopOrder1,
                                       &Solution::IsPopOrder2,
                                       &Solution::IsPopOrder3};
};

int main(int argc, char* argv[])
{
    std::vector<int> pushV = {1, 2, 3, 4, 5};
    std::vector<int> popV = {4, 5, 3, 2, 1};
    std::vector<int> popV2 = {4, 3, 5, 1, 2};

    Solution s;
    s.test(pushV, popV);
    s.test(pushV, popV2);

    return 0;
}