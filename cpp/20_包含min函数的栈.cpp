#include <iostream>
#include <stack>

// 这种方式两个栈不是等长的
// 注意pop一些值之后min是否受到了影响
// 特殊情况是存在几个值相等，且都是最小值

class Solution {
private:
    std::stack<int> stack;
    std::stack<int> minStack;

public:
    void push(int value) {
        stack.push(value);
        if (minStack.empty() || minStack.top() >= value) {
            minStack.push(value);
        } 
    }

    void pop() {
        if (stack.empty() || minStack.empty()) {
            return;
        }
        if (minStack.top() == stack.top()) {
            minStack.pop();
        }
        stack.pop();
    }

    int top() {
        return stack.top();
    }

    int min() {
        return minStack.top();
    }
};

int main(int argc, char* argv[])
{
    Solution s;

    s.push(1);
    s.push(6);
    s.push(5);
    s.pop();
    s.push(8);
    s.push(0);
    s.push(3);

    std::cout << s.top() << std::endl;
    std::cout << s.min() << std::endl;
    
    return 0;
}