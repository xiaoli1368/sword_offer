#include <iostream>
#include <vector>
#include <stack>
#include <stdio.h>
#include <sys/time.h>

#include "ListNode.h"

/* 定义的结构体
typedef struct ListNode {
    int val;
    ListNode* next;
    ListNode (int x, ListNode* ptr) : val(x), next(ptr) {}
} ListNode;
*/

class Solution {
private:
    std::vector<int> vec_;
public:
    // 1. 递归法
    // 递归时间复杂度O(n)，空间复杂度O(1)
    void printListFromTailToHead1(ListNode* head) {
        if (head == nullptr) {
            return;
        } else {
            printListFromTailToHead1(head->next);
            vec_.push_back(head->val);
        }
    }

    // 2. 使用堆栈，递归就是堆栈实现的
    // 时间复杂度O(2n)，空间复杂度O(n)
    void printListFromTailToHead2(ListNode* head) {
        if (head == nullptr) {
            return;
        }

        std::stack<int> stack;
        while (head != nullptr) {
            stack.push(head->val);
            head = head->next;
        }

        while (!stack.empty()) {
            this->vec_.push_back(stack.top());
            stack.pop();
        }
    }

    // 3. 头插法形成新的反向链表，然后顺序输出
    // 时间复杂度O(2n)，空间复杂度O(n)
    void printListFromTailToHead3(ListNode* head) {
        if (head == nullptr) {
            return;
        }

        ListNode* newhead = new ListNode(0);
        while (head != nullptr) {
            ListNode_insertHead(newhead, head->val);
            head = head->next;
        }

        while (newhead->next != nullptr) {
            this->vec_.push_back(newhead->next->val);
            newhead = newhead->next;
        }

        // 清除申请的空间
        ListNode_clear(newhead);
    }

    // 4. 两次遍历，vec尾部添加
    // 时间复杂度O(2n)，空间复杂度O(1)
    void printListFromTailToHead4(ListNode* head) {
        if (head == nullptr) {
            return;
        }

        int length = 0;
        ListNode* currhead = head;
        while (currhead != nullptr) {
            length++;
            currhead = currhead->next;
        }

        this->vec_ = std::vector<int>(length);
        for (int i = 1; head != nullptr; i++) {
            this->vec_[length - i] = head->val;
            head = head->next;
        }
    }

    // 5. 一次遍历，vec头部添加
    // 时间复杂度O(n)，空间复杂度O(1)，需要调用insert
    void printListFromTailToHead5(ListNode* head) {
        if (head == nullptr) {
            return;
        }

        while (head != nullptr) {
            this->vec_.insert(this->vec_.begin(), head->val);
            head = head->next;
        }
    }

    // 6. 原链表基础上直接反转，然后顺序输出
    // 其实就是翻转链表了，注意会破坏原有链表
    // 时间复杂度O(2n)，空间复杂度O(1)
    void printListFromTailToHead6(ListNode * head) {
        if (head == nullptr) {
            return;
        }

        // 翻转链表
        ListNode* p = head;
        ListNode* q = head->next;
        head->next = nullptr;
        while (q != nullptr) {
            ListNode* tmp = q->next;
            q->next = p;
            p = q;
            q = tmp;
        }

        while (p != nullptr) {
            this->vec_.push_back(p->val);
            p = p->next;
        }
    }
    
    // ===== 工具函数 =====

    // 打印一维vec
    void printf_1d_vec() {
        for (auto & i : this->vec_) {
            printf("%d, ", i);
        }
    }

    // 测试函数
    void test(ListNode* head) {
        struct timeval start, end;
        printf("=====\n");
        for (auto func : this->func_vec_) {
            this->vec_.clear(); // 注意清理缓存
            gettimeofday(&start, nullptr);
            (this->*func)(head);
            gettimeofday(&end, nullptr);

            printf("time(us): %4ld, result: ", end.tv_usec - start.tv_usec);
            if (this->vec_.size() > 20) {
                printf("too many numbers to display");
            } else {
                this->printf_1d_vec();
            }
            printf("\n");
        }
    }

private:
    typedef void (Solution::*func_ptr)(ListNode*);
    std::vector<func_ptr> func_vec_ = {&Solution::printListFromTailToHead1,
                                       &Solution::printListFromTailToHead2,
                                       &Solution::printListFromTailToHead3,
                                       &Solution::printListFromTailToHead4,
                                       &Solution::printListFromTailToHead5,
                                       &Solution::printListFromTailToHead6};

};

int main (int argc, char* argv[])
{
    std::vector<int> data = {1, 8, 6, 4};
    std::vector<int> data2 = {4, 5, 0, 9, 4, 2, 6, 9, 1, 7, 5, 2, 2, 4};
    std::vector<int> data3(10000, 0);
    ListNode* head = ListNode_creatFromVec(data)->next; // 跳过固定的头节点
    ListNode* head2 = ListNode_creatFromVec(data2)->next;
    ListNode* head3 = ListNode_creatFromVec(data3)->next;

    Solution s;
    s.test(head);
    s.test(head2);
    s.test(head3);

    return 0;
}