#include <iostream>
#include <vector>
#include <stdio.h>
#include <sys/time.h>

#include "ListNode.h"
#include "my_vector.h"

/*
typedef struct ListNode {
    int val;
    ListNode* next;
    ListNode(int x) : val(x), next(nullptr) {}
} ListNode;
*/

class Solution {
public:
    // 1. 存储的方式
    // 时间复杂度O(n)，空间复杂度O(n)
    ListNode* FindKthToTail1(ListNode* head, unsigned int k) {
        if (head == nullptr || k <= 0) {
            return nullptr;
        }

        // 把链表保存到vec
        std::vector<ListNode*> ptr;
        while (head != nullptr) {
            ptr.push_back(head);
            head = head->next;
        }

        if (k > ptr.size()) {
            return nullptr;
        } else {
            return ptr[ptr.size() - k];
        }
    }

    // 2. 两重遍历的方式
    // 时间复杂度O(2n - k)，空间复杂度O(1)
    ListNode* FindKthToTail2(ListNode* head, unsigned int k) {
        if (head == nullptr || k <= 0) {
            return nullptr;
        }

        // 获取链表总长度
        int length = 0;
        ListNode* curr = head;
        while (curr != nullptr) {
            length++;
            curr = curr->next;
        }

        if (k > length) {
            return nullptr;
        }

        for (int i = 0; i < length - k; i++) {
            head = head->next;
        }

        return head;
    }

    // 3. 采用双指针的形式
    // 时间复杂度O(n)，空间复杂度O(1)
    ListNode* FindKthToTail3(ListNode* head, unsigned int k) {
        ListNode* p = head;
        ListNode* q = head;

        int count = 0;
        while (p) {
            count++;
            p = p->next;
            if (count > k) {
                q = q->next;
            }
        }
        
        if (k > count) {
            return nullptr;
        } else {
            return q;
        }
    }

    // 测试函数
    void test(ListNode* head, unsigned int k) {
        ListNode* result = nullptr;
        struct timeval start, end;
        printf("=====\n");
        for (auto & func : this->func_vec_) {
            gettimeofday(&start, nullptr);
            result = (this->*func)(head, k);
            gettimeofday(&end, nullptr);
            printf("time(us): %ld, result: ", end.tv_usec - start.tv_usec);
            if (result != nullptr) {
                printf("%d\n", result->val);
            } else {
                printf("nullptr\n");
            }
        }
    }

private:
    typedef ListNode* (Solution::*func_ptr)(ListNode*, unsigned int);
    std::vector<func_ptr> func_vec_ = {&Solution::FindKthToTail1,
                                  &Solution::FindKthToTail2,
                                  &Solution::FindKthToTail3};
};


int main(int argc, char* argv[])
{
    std::vector<int> vec = {1, 2, 5, 6, 7, 9};
    std::vector<int> vec2 = vector_CreatRandom(1, 10000, 10000);
    ListNode* head1 = ListNode_creatFromVec(vec)->next;
    ListNode* head2 = ListNode_creatFromVec(vec2)->next;

    Solution s;
    s.test(head1, 2);
    s.test(head1, 10);
    s.test(head2, 100);
    s.test(head2, 300);

    ListNode_clear(head1);
    ListNode_clear(head2);

    return 0;
}