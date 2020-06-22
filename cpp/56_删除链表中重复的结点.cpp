#include <iostream>
#include <vector>
#include <stdio.h>
#include <sys/time.h>

#include "ListNode.h"

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
    // 1. 第一次的方式，利用辅助函数，检测当前节点后续的重复次数
    ListNode* deleteDuplication(ListNode* head) {
        if (head == nullptr) {
            return nullptr;
        }
        
        // 为了检测head是否存在重复，需要新加一个额外的head
        ListNode* new_head = new ListNode(0);
        new_head->next = head;
        ListNode* curr = new_head;
        ListNode* tmp = nullptr;
        
        while (curr != nullptr) {
            // 检测接下来有多少个节点相同，如果不同则返回cnt，并修改tmp指针
            if (checkSame(curr->next, tmp) == 0) {
                curr = curr->next;
            } else {
                curr->next = tmp;
            }
        }
        
        return new_head->next;
    }

    // ===== 工具函数 =====
    // 输出一个结点，返回从这里开始有多少个重复的结点
    // next_head为不重复的下一个结点，这里注意要用引用
    int checkSame(ListNode* head, ListNode* & next_head) {
        int cnt = 0;
        while (head != nullptr && head->next != nullptr) {
            if (head->val != head->next->val) {
                next_head = head->next;
                return cnt;
            } else {
                cnt++;
                head = head->next;
            }
        }
        
        next_head = nullptr;
        return cnt;
    }

    // 测试函数
    void test(std::vector<int>& array) {
        ListNode* result = nullptr;
        struct timeval start, end;
        ListNode* head = ListNode_creatFromVec(array)->next;

        printf("=====\n");
        gettimeofday(&start, nullptr);
        result = this->deleteDuplication(head);
        gettimeofday(&end, nullptr);
        printf("times(us): %ld, result: ", end.tv_usec - start.tv_usec);
        ListNode_print(result, false, true);
        printf("\n");
    }
};

int main(int argc, char* argv[])
{
    std::vector<int> array = {1, 1, 2 ,3, 3, 5, 7, 7, 9};

    Solution s;
    s.test(array);
    
    return 0;
}