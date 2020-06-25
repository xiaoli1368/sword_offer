#include <iostream>
#include <vector>
#include <stack>
#include <stdio.h>
#include <sys/time.h>

#include "my_vector.h"

// 等长最小栈，存在数据冗余

class Solution {
private:
    std::stack<int> stack;
    std::stack<int> minStack;

public:
    void push(int value) {
        if (minStack.empty() || value <= minStack.top()) {
            minStack.push(value);
        } else {
            minStack.push(minStack.top());
        } 
        stack.push(value);
    }

    void pop() {
        minStack.pop();
        stack.pop();
    }

    int top() {
        return stack.top();
    }

    int min() {
        return minStack.top();
    }

    // 测试函数
    // push随机数据，中间获取最小值
    // pop随机数据，中间获取最小值
    void test(std::vector<int>& vec) {
        struct timeval start, end;
        std::vector<int> ret;
        
        printf("=====\n");
        gettimeofday(&start, nullptr);
        for (auto & i : vec) {
            push(i);
            ret.push_back(min());
        }
        for (auto & i : vec) {
            ret.push_back(min());
            pop();
        }
        gettimeofday(&end, nullptr);
        printf("times(us): %ld, result: ", end.tv_usec - start.tv_usec);
        printf_1d_vec(ret);
    }
};

int main(int argc, char* argv[])
{
    std::vector<int> vec = vector_CreatRandom(1, 20, 5);
    std::vector<int> vec2 = vector_CreatRandom(1, 1000, 100);

    Solution s;
    s.test(vec);
    s.test(vec2);

    return 0;
}