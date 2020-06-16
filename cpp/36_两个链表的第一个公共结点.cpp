#include <iostream>
#include <map>
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
    // 1. hash方式
    // 时间复杂度O(n + m)，空间复杂度O(n)
    ListNode* FindFirstCommonNode(ListNode* h1, ListNode* h2) {
        if (h1 == nullptr || h2 == nullptr) {
            return nullptr;
        }

        std::map<ListNode*, int> map;
        while (h1) {
            map[h1] = h1->val;
            h1 = h1->next;
        }

        while (h2) {
            if (map.count(h2) == 1) {
                return h2;
            }
            h2 = h2->next;
        }

        return nullptr;
    }

    // 2. 循环法，高效的迭代方式
    // 时间复杂度O(n + m)，空间复杂度O(1)
    ListNode* FindFirstCommonNode2(ListNode* h1, ListNode* h2) {
        ListNode* t1 = h1;
        ListNode* t2 = h2;
        while (t1 != t2) {
            t1 = (t1 == nullptr ? h2 : t1->next);
            t2 = (t2 == nullptr ? h1 : t2->next);
        }
        return t1;
    }

    // 测试函数
    // 输入两个vec，分别构建链表，将vec2链接到vec1的中点位置
    void test(std::vector<int>& data1, std::vector<int>& data2) {
        struct timeval start, end;
        ListNode* result = nullptr;

        // 构建链表
        ListNode* head1 = ListNode_creatFromVec(data1);
        ListNode* head2 = ListNode_creatFromVec(data2);
        ListNode* tail2 = ListNode_getLastNode(head2);
        tail2->next = ListNode_getMiddleNode(head1);

        printf("=====\n");
        for (auto & func : this->func_vec_) {
            gettimeofday(&start, nullptr);
            result = (this->*func)(head1, head2);
            gettimeofday(&end, nullptr);
            printf("result: %d, times(us): %ld\n", result->val, end.tv_usec - start.tv_usec);
        }

        // 注意释放head2之前需要处理尾部的野指针
        tail2->next = nullptr;
        ListNode_clear(head1);
        ListNode_clear(head2);
    }

private:
    typedef ListNode* (Solution::*func_ptr)(ListNode*, ListNode*);
    std::vector<func_ptr> func_vec_ = {&Solution::FindFirstCommonNode,
                                       &Solution::FindFirstCommonNode2};
};

int main(int argc, char* argv[])
{
    std::vector<int> data1 = {1, 2, 4, 8, 2, 9, 6};
    std::vector<int> data2 = {4, 6, 9};

    std::vector<int> data3 = vector_CreatRandom(1, 1000, 1000);
    std::vector<int> data4 = vector_CreatRange(1, 100);

    Solution s;
    s.test(data1, data2);
    s.test(data3, data4);

    return 0;
}