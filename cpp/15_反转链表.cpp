#include <iostream>
#include <vector>

typedef struct  ListNode {
    int val;
    ListNode* next;
    ListNode(int x) : val(x), next(nullptr) {}
} ListNode;

class Solution {
public:
    // 使用向量来初始化空链表
    void init_use_vec(ListNode* head, std::vector<int>& vec) {
        if (head == nullptr) {
            return;
        }

        ListNode* tmp = head;
        for (auto i : vec) {
            tmp->next = new ListNode(i);
            tmp = tmp->next;
        }
    }

    // 打印链表
    void print_ListNode(ListNode* head) {
        if (head == nullptr) {
            return;
        }

        ListNode* tmp = head;
        while (tmp) {
            std::cout << tmp->val << " ";
            tmp = tmp->next;
        }
        std::cout << std::endl;
    }

    // 反转链表
    ListNode* ReverseList(ListNode* head) {
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
};

int main(int argc, char* argv[])
{
    Solution s;
    ListNode* head = new ListNode(0);
    std::vector<int> vec = {2, 3, 9, 5, 1, 7};

    s.init_use_vec(head, vec);
    s.print_ListNode(head);

    head = s.ReverseList(head);
    s.print_ListNode(head);

    return 0;
}