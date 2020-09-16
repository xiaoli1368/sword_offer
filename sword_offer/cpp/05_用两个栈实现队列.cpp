#include <iostream>
#include <vector>
#include <stack>
#include <stdio.h>
#include <sys/time.h>

#include "StackNode.h"
#include "my_vector.h"

/*
typedef struct StackNode {
    int val;
    StackNode* next;
    StackNode(int input) : val(input), next(nullptr) {};  
} StackNode;
*/

void printf_stack(std::stack<int>);

class Solution {
public:
    // ===== 使用stl定义的栈 =====
    std::stack<int> s1;
    std::stack<int> s2;

    void push(int node) {
        s1.push(node);
    }

    int pop(void) {
        if (s1.empty() && s2.empty()) {
            return 0;
        }

        if (!s2.empty()) {
            int tmp = s2.top();
            s2.pop();
            return tmp;
        } 

        while (!s1.empty()) {
            s2.push(s1.top());
            s1.pop();
        }
        return pop();
    }

    // ===== 使用自定义的栈 =====
    StackNode* h1;
    StackNode* h2;

    void push2(int node) {
        StackNode_push(h1, node);
    }

    int pop2(void) {
        if (h1 == nullptr && h2 == nullptr) {
            return 0;
        }

        if (h2 != nullptr) {
            int tmp = StackNode_top(h2);
            StackNode_pop(h2);
            return tmp;
        }

        while (h1 != nullptr) {
            StackNode_push(h2, StackNode_top(h1));
            StackNode_pop(h1);
        }
        return pop2();
    }

    // ===== 构造函数以及析构函数 =====
    Solution() {
        h1 = nullptr;
        h2 = nullptr;
    }

    ~Solution() {};

    // ===== 测试函数 =====
    // 输入vec，全部push，然后全部pop
    void test(std::vector<int>& vec) {
        struct timeval start, end;
        
        printf("=====\n");
        gettimeofday(&start, nullptr);
        for (auto & i : vec) {
            push(i);
        }
        for (auto & i : vec) {
            printf("%d, ", pop());
        }
        gettimeofday(&end, nullptr);
        printf("times(us):%ld\n", end.tv_usec - start.tv_usec);

        gettimeofday(&start, nullptr);
        for (auto & i : vec) {
            push2(i);
        }
        for (auto & i : vec) {
            printf("%d, ", pop2());
        }
        gettimeofday(&end, nullptr);
        printf("times(us):%ld\n", end.tv_usec - start.tv_usec);
    }
};

int main(int argc, char* argv[])
{
    std::vector<int> vec = {1, 3, 5, 6, 7};
    std::vector<int> vec2 = vector_CreatRandom(1, 20, 20);
    std::vector<int> vec3 = vector_CreatRange(1, 100, 1);

    Solution s;
    s.test(vec);
    s.test(vec2);
    s.test(vec3);

    return 0;
}