#include <iostream>
#include <vector>

typedef struct ListNode {
    int val;
    ListNode* next;
    ListNode(int x) : val(x), next(nullptr) {}
} ListNode;

class Solution {
public:
    // 使用向量初始化链表
    void init_ListNode(ListNode* head, std::vector<int>& vec) {
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

    // 合并两个递增链表，递归法
    // 这种方式会对原始链表造成破坏
    ListNode* Merge(ListNode* p, ListNode* q) {
        if (p == nullptr) {
            return q;
        }
        if (q == nullptr) {
            return p;
        }
        if (p->val < q->val) {
            p->next = Merge(p->next, q);
            return p;
        } else {
            q->next = Merge(q->next, p);
            return q;
        }

    }

    // 合并两个递增链表，迭代法
    // 这种方式也会破坏链表
    ListNode* Merge2(ListNode* p, ListNode* q) {
        ListNode* head = new ListNode(0);
        ListNode* tmp = head;

        while (p != nullptr && q != nullptr) {
            if (p->val < q->val) {
                tmp->next = p;
                p = p->next;
            } else {
                tmp->next = q;
                q = q->next;
            }
            tmp = tmp->next;
        }

        if (p == nullptr) {
            tmp->next = q;
        }
        if (q == nullptr) {
            tmp->next = p;
        }
        
        return head->next;
    }
};

int main(int argc, char* argv[])
{
    Solution s;
    std::vector<int> array1 = {1, 4, 7, 8, 9, 10};
    std::vector<int> array2 = {2, 5, 6, 7, 8, 11, 13};

    // 递归的方式
    ListNode* p = new ListNode(0);
    ListNode* q = new ListNode(0);
    s.init_ListNode(p, array1);
    s.init_ListNode(q, array2);
    s.print_ListNode(p);
    s.print_ListNode(q);
    ListNode* m = s.Merge(p, q);
    s.print_ListNode(m);

    // 迭代的方式
    ListNode* p2 = new ListNode(0);
    ListNode* q2 = new ListNode(0);
    s.init_ListNode(p2, array1);
    s.init_ListNode(q2, array2);
    std::cout << "=====" << std::endl;
    s.print_ListNode(p2);
    s.print_ListNode(q2);
    ListNode* m2 = s.Merge2(p2, q2);
    s.print_ListNode(m2);

    // 注意存在内存泄露，没有delete
    return 0;
}