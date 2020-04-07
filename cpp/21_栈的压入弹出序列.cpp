#include <iostream>
#include <vector>

class Solution {
public:
    // 参考答案
    bool IsPopOrder(std::vector<int> pushV, std::vector<int> popV) {
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

    // 自行解法
    bool IsPopOrder2(std::vector<int> pushV, std::vector<int> popV) {
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
};

int main(int argc, char* argv[])
{
    Solution s;
    std::vector<int> pushV = {1, 2, 3, 4, 5};
    std::vector<int> popV = {4, 5, 3, 2, 1};
    std::vector<int> popV2 = {4, 3, 5, 1, 2};

    std::cout << s.IsPopOrder(pushV, popV) << std::endl;
    std::cout << s.IsPopOrder(pushV, popV2) << std::endl;
    std::cout << s.IsPopOrder2(pushV, popV) << std::endl;
    std::cout << s.IsPopOrder2(pushV, popV2) << std::endl;

    return 0;
}