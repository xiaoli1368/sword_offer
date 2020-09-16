#include <iostream>
#include <vector>
#include <map>
#include <stdio.h>
#include <sys/time.h>

#include "ListNode.h"
#include "my_vector.h"

/*
struct ListNode {
    int val;
    struct ListNode *next;
    ListNode(int x) :
        val(x), next(NULL) {
    }
};
*/
class Solution {
public:
    // 1. 哈希表解法
    // 时间复杂度O(n)，空间复杂度O(n)
    ListNode* EntryNodeOfLoop1(ListNode* head) {
        if (head == nullptr) {
            return nullptr;
        }

        std::map<ListNode*, int> map;
        while (head != nullptr) {
            if (map.count(head) == 0) {
                map[head] = head->val;
                head = head->next;
            } else {
                return head;
            }
        }
        
        return nullptr;
    }

    // 2. 快慢指针解法
    // 时间复杂度 > O(n)，空间复杂度O(1)
    ListNode* EntryNodeOfLoop2(ListNode* head) {
        if (head == nullptr) {
            return nullptr;
        }

        ListNode* p = head;
        ListNode* q = head;
        
        // 第一次快慢追踪相遇
        while (p && q && q->next) {
            p = p->next;
            q = q->next->next;
            if (p == q) {
                break;
            }
        }
        // 防止特殊情况
        if (p != q) {
            return nullptr;
        }

        // 移动位置后，第二次同速追踪相遇
        p = head;
        while (p != q) {
            p = p->next;
            q = q->next;
        }
        return p;
    }

    // 3. 利用链表存储标记，类似哈希表法
    // 时间复杂度O(n)，空间复杂度(1)
    // 缺点是会破环原有的数据
    ListNode* EntryNodeOfLoop3(ListNode* head) {
        if (head == nullptr) {
            return nullptr;
        }

        while (head != nullptr) {
            if (head->val == 666) {
                return head;
            }
            head->val = 666;
            head = head->next;
        }

        return nullptr;
    }

 
    // 测试函数
    void test(std::vector<int>& array, int pos) {
        struct timeval start, end;
        ListNode* result = nullptr;

        // 生成环形链表
        ListNode* head = ListNode_creatFromVec(array);
        ListNode* tail = ListNode_getLastNode(head);
        ListNode* circle = ListNode_getIndexNode(head, pos);
        tail->next = circle;

        printf("=====\n");
        for (auto & func : this->func_vec_) {
            gettimeofday(&start, nullptr);
            result = (this->*func)(head);
            gettimeofday(&end, nullptr);

            printf("result: %d, pointer: %p, time(us): %ld\n", result->val, result, end.tv_usec - start.tv_usec);
        }
    }

private:
    typedef ListNode* (Solution::*func_ptr)(ListNode*);
    std::vector<func_ptr> func_vec_ = {&Solution::EntryNodeOfLoop1,
                                       &Solution::EntryNodeOfLoop2,
                                       &Solution::EntryNodeOfLoop3};
};

int main(int argc, char* argv[])
{
    std::vector<int> array = {3, 2, 0, -4, 1, 5};
    std::vector<int> array2 = vector_CreatRange(1, 10000, 1);

    Solution s;
    s.test(array, 2); // 在位置2处生成环形链表并且测试
    s.test(array2, 100);

    return 0;
}