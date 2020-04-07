#include <iostream>
#include <vector>

class Solution {
public:
    // 递归的方式
    int Fibonacci(int n) {
        if (n < 2) {
            return n;
        }
        return Fibonacci(n-1) + Fibonacci(n-2);
    }

    // 数组存储的方式
    int Fibonacci2(int n) {
        if (n < 2) {
            return n;
        }
        std::vector<int> vec = {0, 1};
        for (int i = 0; i < n-1; i++) {
            vec.push_back(vec.back() + vec.at(vec.size() - 2));
        }
        return vec.back();
    }

    // 更为高效的方式
    int Fibonacci3(int n) {
        if (n < 2) {
            return n;
        }
        int a = 0, b = 1, c = 0;
        for (int i = 0; i < n-1; i++) {
            c = a + b;
            a = b;
            b = c;
        }
        return c;
    }
};

int main(int argc, char* argv[])
{
    Solution s;
    std::cout << s.Fibonacci3(39) << std::endl;

    return 0;
}