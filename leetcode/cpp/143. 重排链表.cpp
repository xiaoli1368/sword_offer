#include <vector>

typedef struct ListNode {
    int val;
    ListNode* next;
    ListNode(int val=0, ListNode* next=nullptr) : val(val), next(next) {}
} ListNode;

class Solution {
public:
    // 递归法（这个方法需要返回值）
    ListNode* reorderList(ListNode* head) {
        if (head == nullptr || head->next == nullptr || head->next->next == nullptr) {
            return head;
        }
        // 找到当前非空尾节点和上一个节点
        ListNode *p = head, *q = head->next;
        while (q->next) {
            p = p->next;
            q = q->next;
        }
        // 重新排列
        p->next = nullptr;
        ListNode* newHead = head->next;
        head->next = q;
        q->next = reorderList(newHead);
        return head;
    }

    // 全部保存法
    void reorderList2(ListNode* head) {
        // 使用vector保存所有节点
        std::vector<ListNode*> stack;
        ListNode* tmp = head;
        while (tmp) {
            stack.push_back(tmp);
            tmp = tmp->next;
        }
        // 分别从前后取值，使用flag来区分
        int flag = 0;
        int l = 0, r = stack.size() - 1;
        ListNode* newHead = new ListNode(0);
        while (l <= r) {
            if (flag == 0) {
                newHead->next = stack[l++];
            } else {
                newHead->next = stack[r--];
            }
            flag = 1 - flag;
            newHead = newHead->next;
        }
        newHead->next = nullptr;
    }

    // 后一半保存，插入前一半
    void reorderList3(ListNode* head) {
        if (head == nullptr) {
            return;
        }
        // 找中点，断开
        ListNode *p = head, *q = head;
        while (p && q && q->next) {
            p = p->next;
            q = q->next->next;
        }
        // 保存后半部分到栈
        std::vector<ListNode*> stack;
        while (p) {
            stack.push_back(p);
            p = p->next;
        }
        // 从头到尾完成插入操作
        while (head && stack.size() > 1) {
            ListNode* tmp = head->next;
            head->next = stack.back();
            head->next->next = tmp;
            head = tmp;
            stack.pop_back();
            if (!stack.empty()) {
                stack.back()->next = nullptr;
            }
        }
    }

    // 找中点，翻转，归并
    void reorderList4(ListNode* head) {
        if (head == nullptr || head->next == nullptr) {
            return;
        }
        // 找中点，断开
        ListNode *mid = head, *p = head, *q = head;
        while (q && q->next) {
            mid = p;
            p = p->next;
            q = q->next->next;
        }
        mid->next = nullptr;
        // 后半部分翻转
        ListNode* newHead = nullptr;
        while (p) {
            ListNode* tmp = p->next;
            p->next = newHead;
            newHead = p;
            p = tmp;
        }
        // 两链表合并
        ListNode* h = new ListNode(0);
        while (head || newHead) {
            if (head) {
                h->next = head;
                h = h->next;
                head = head->next;
            }
            if (newHead) {
                h->next = newHead;
                h = h->next;
                newHead = newHead->next;
            }
        }
    }
};