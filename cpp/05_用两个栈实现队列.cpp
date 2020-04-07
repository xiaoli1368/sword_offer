/*
 * 先实现一个栈
 * 然后再用两个栈实现一个队列
 */

#include <iostream>
#include <stack>

typedef struct stackNode {
    int val;
    stackNode* next;
    stackNode(int input) : val(input), next(nullptr) {};  
} stackNode;

class stackClass {
public:
    stackClass() {
        head_ = new stackNode(0);
        size_ = 0;
    }
    ~stackClass() {}
    
    int pop(void) {
        if (head_ != nullptr && size_ >= 1) {
            int tmp = head_->val;
            stackNode* tmpNode = head_;
            delete tmpNode;

            head_ = head_->next;
            size_ -= 1;
            return tmp;
        }
        std::cout << "Error: stack has been empty!" << std::endl;
    }

    void push(int node) {
        if (head_ == nullptr) {
            return;
        }
        stackNode* newStack = new stackNode(node);
        newStack->next = head_;
        head_ = newStack;
        size_ += 1;
    }

    int getSize(void) {
        return size_;
    }

private:
    stackNode* head_;
    int size_;
};

// 注意这里使用了STL中的堆栈
class twoStackFromQueue {
public:
    void push(int node) {
        stack1.push(node);
    }

    int pop(void) {
        if (stack2.size() != 0) {
            int tmp = stack2.top();
            stack2.pop();
            return tmp;
        } 

        int length1 = stack1.size();
        if (length1 != 0) {
            for (int i = 0; i < length1; i++) {
                int tmp = stack1.top();
                stack1.pop();
                stack2.push(tmp);
            }
            return pop();
        }
    }

private:
    std::stack<int> stack1;
    std::stack<int> stack2;
};


int main(int argc, char* argv[])
{
    int array[] = {1, 3, 5, 6, 7};
    int length = 5;

    // 测试单个栈　***********************************************
    stackClass my_stack;

    // 入栈
    for (int i = 0; i < length; i++) {
        my_stack.push(array[i]);
    }
    std::cout << "current stack size: " << my_stack.getSize() << std::endl;

    // 出栈并打印
    for (int i = 0; i < length; i++) {
        std::cout << my_stack.pop() << " ";
    }
    std::cout << "\ncurrent stack size: " << my_stack.getSize() << std::endl;

    // 测试两个栈组成队列　****************************************
    twoStackFromQueue my_queue;
    for (int i = 0; i < length; i++) {
        my_queue.push(array[i]);
    }
    std::cout << "queue output:" << std::endl;
    for (int i = 0; i < length; i++) {
        std::cout << my_queue.pop() << " ";
    }
    std::cout << std::endl;

    return 0;
}