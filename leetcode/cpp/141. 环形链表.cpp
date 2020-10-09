#include <unordered_set>

typedef struct ListNode {
    int val;
    ListNode* next;
    ListNode(int x) : val(x), next(nullptr) {}
} ListNode;

class Solution {
public:
    // 哈希表法
    bool hadCycle1(ListNode* head) {
        std::unordered_set<ListNode*> set;
        while (head) {
            if (set.count(head)) {
                return true;
            } else {
                set.insert(head);
                head = head->next;
            }
        }
        return false;
    }

    // 本地设置标志位法
    bool hasCycle2(ListNode* head) {
        while (head) {
            if (head->val == 666) {
                return true;
            } else {
                head->val = 666;
                head = head->next;
            }
        }
        return false;
    }

    // 双指针法
    bool hasCycle3(ListNode* head) {
        ListNode* p = head;
        ListNode* q = head;
        while (q && q->next) {
            p = p->next;
            q = q->next->next;
            if (p == q) {
                return true;
            }
        }
        return false;
    }
};