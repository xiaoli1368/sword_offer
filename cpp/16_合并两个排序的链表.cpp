#include <iostream>
#include <vector>
#include <stdio.h>
#include <sys/time.h>

#include "ListNode.h"

/*
typedef struct ListNode {
    int val;
    ListNode* next;
    ListNode(int x) : val(x), next(nullptr) {}
} ListNode;
*/

class Solution {
public:
    // 递归法，创建新的节点
    ListNode* Merge1(ListNode* p, ListNode* q) {
        if (p == nullptr) {
            return q;
        }
        if (q == nullptr) {
            return p;
        }

        ListNode* head = new ListNode(0);
        if (p->val < q->val) {
            head->val = p->val;
            head->next = Merge1(p->next, q);
        } else {
            head->val = q->val;
            head->next = Merge1(q->next, p);
        }

        return head;
    }

    // 循环法，创建新的节点
    ListNode* Merge2(ListNode* p, ListNode* q) {
        ListNode* head = new ListNode(0);
        ListNode* curr = head;

        while (p && q) {
            if (p->val < q->val) {
                curr->next = new ListNode(p->val);
                p = p->next;
            } else {
                curr->next = new ListNode(q->val);
                q = q->next;
            }
            curr = curr->next;
        }
        curr->next = p ? p : q;

        return head->next;
    }

    // 递归法，直接构建链接
    // 这种方式会对原始链表造成破坏
    ListNode* Merge3(ListNode* p, ListNode* q) {
        if (p == nullptr) {
            return q;
        }
        if (q == nullptr) {
            return p;
        }
        if (p->val < q->val) {
            p->next = Merge3(p->next, q);
            return p;
        } else {
            q->next = Merge3(q->next, p);
            return q;
        }
    }

    // 循环法，直接构建链接
    // 这种方式也会破坏链表
    ListNode* Merge4(ListNode* p, ListNode* q) {
        ListNode* head = new ListNode(0);
        ListNode* curr = head;

        while (p != nullptr && q != nullptr) {
            if (p->val < q->val) {
                curr->next = p;
                p = p->next;
            } else {
                curr->next = q;
                q = q->next;
            }
            curr = curr->next;
        }
        curr->next = p ? p : q;

        return head->next;
    }

    // 测试函数
    // 输入两个有序vec，各自构造成链表，然后合并
    void test(std::vector<int>& array1, std::vector<int>& array2) {
        struct timeval start, end;
        printf("=====\n");

        for (auto & func : this->func_vec_) {
            // 生成两个链表
            ListNode* p = ListNode_creatFromVec(array1)->next;
            ListNode* q = ListNode_creatFromVec(array2)->next;

            // 合并
            gettimeofday(&start, nullptr);
            ListNode* result = (this->*func)(p, q);
            gettimeofday(&end, nullptr);

            // 打印结果
            printf("time(us): %ld, result: ", end.tv_usec - start.tv_usec);
            ListNode_print(result, false);
            printf("\n");

            // 清除缓存
            // 注意对于直接建立链接的情况，delete p q result 会报错 double free
            //ListNode_clear(p);
            //ListNode_clear(q);
            //ListNode_clear(result);
        }
    }

private:
    typedef ListNode* (Solution::*func_ptr)(ListNode*, ListNode*);
    std::vector<func_ptr> func_vec_ = {&Solution::Merge1,
                                       &Solution::Merge2,
                                       &Solution::Merge3,
                                       &Solution::Merge4};
};

int main(int argc, char* argv[])
{
    std::vector<int> array1 = {1, 4, 7, 8, 9, 10};
    std::vector<int> array2 = {2, 5, 6, 7, 8, 11, 13};

    Solution s;
    s.test(array1, array2);

    return 0;
}