#include <iostream>
#include <vector>

typedef struct ListNode {
    int val;
    ListNode* next;
    ListNode(int x) : val(x), next(nullptr) {}
} ListNode;

class Solution {
public:
    // 使用向量进行链表的初始化(注意是对空表进行初始化)
    void init_use_vec(ListNode* head, std::vector<int>& vec) {
        ListNode* tmp = head;
        for (auto i : vec) {
            ListNode* newNode = new ListNode(i);
            tmp->next = newNode;
            tmp = tmp->next;
        }
    }

    // 打印整个链表
    void print_listNode(ListNode* head) {
        ListNode* tmp = head;
        while (tmp != nullptr) {
            std::cout << tmp->val << " ";
            tmp = tmp->next;
        }
        std::cout << std::endl;
    }

    // 返回倒数第k个节点
    // 使用存储的方式a
    ListNode* FindKthToTail(ListNode* head, unsigned int k) {
        if (head == nullptr) {
            return nullptr;
        }

        std::vector<ListNode*> ptr;
        ListNode* tmp = head;
        while (tmp) {
            ptr.push_back(tmp);
            tmp = tmp->next;
        }

        int length = ptr.size();
        if (k > length) {
            return nullptr;
        } else {
            return ptr[length - k];
        }
    }

    // 返回倒数第k个节点
    // 采用双指针的形式
    ListNode* FindKthToTail2(ListNode* head, unsigned int k) {
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
};


int main(int argc, char* argv[])
{
    Solution s;
    ListNode* head = new ListNode(0);
    std::vector<int> vec = {1, 2, 5, 6, 7, 9};

    s.init_use_vec(head, vec);
    s.print_listNode(head);
    std::cout << s.FindKthToTail(head, 3)->val << std::endl;
    std::cout << s.FindKthToTail2(head, 3)->val << std::endl;

    return 0;
}