#include <iostream>
#include <vector>
#include <stdio.h>
#include <sys/time.h>

#include "ListNode.h"

/*
typedef struct  ListNode {
    int val;
    ListNode* next;
    ListNode(int x) : val(x), next(nullptr) {}
} ListNode;
*/

class Solution {
public:
    // 第一次的方式，迭代法
    ListNode* ReverseList1(ListNode* head) {
        if (head == nullptr) {
            return nullptr;
        }

        ListNode* p = head;
        ListNode* q = head->next;
        head->next = nullptr;

        while (q) {
            ListNode* tmp = q->next;
            q->next = p;
            p = q;
            q = tmp;
        }

        return p;
    }

    // 迭代法优化版
    ListNode* ReverseList2(ListNode* head) {
        if (head == nullptr || head->next == nullptr) {
            return head;
        }

        ListNode* p = head->next;
        ListNode* q;
        head->next = nullptr;

        while (p != nullptr) {
            q = p->next;
            p->next = head;
            head = p;
            p = q;
        }

        return head;
    }

    // 递归法
    ListNode* ReverseList3(ListNode* head) {
        if (head == nullptr || head->next == nullptr) {
            return head;
        }

        ListNode* curr = ReverseList3(head->next);
        head->next->next = head; // 需要画图理解
        head->next = nullptr;    // 处理头节点

        return curr;
    }

    // 测试函数
    // ifPrint: 是否打印输出
    void test(ListNode* head, bool ifPrint = true) {
        ListNode* result = nullptr;
        struct timeval start, end;
        printf("=====\n");
        for (auto func : this->func_vec_) {
            gettimeofday(&start, nullptr);
            result = (this->*func)(head);
            gettimeofday(&end, nullptr);

            printf("times(us): %ld, result: ", end.tv_usec - start.tv_usec);
            if (ifPrint) {
                ListNode_print(result, false, true);
            } else {
                printf("too many numbers to display");
            }
            printf("\n");
            head = (this->*func)(result); // 注意恢复，因为还需要调用
        }
    }

private:
    typedef ListNode* (Solution::*func_ptr)(ListNode*);
    std::vector<func_ptr> func_vec_ = {&Solution::ReverseList1,
                                       &Solution::ReverseList2,
                                       &Solution::ReverseList3};
};

int main(int argc, char* argv[])
{
    std::vector<int> vec = {2, 3, 9, 5, 1, 7};
    std::vector<int> vec2(100000, 0);
    ListNode* head = ListNode_creatFromVec(vec);
    ListNode* head2 = ListNode_creatFromVec(vec2);
 
    Solution s;
    s.test(head->next, true);
    s.test(head2->next, false);

    return 0;
}