typedef struct ListNode {
    int val;
    ListNode* next;
    ListNode(int x) : val(x), next(nullptr) {}
} ListNode;

class Solution {
public:
    // 偶数时，返回后一个节点
    ListNode* middleNode(ListNode* head) {
        ListNode* p = head;
        ListNode* q = head;
        while (q && q->next) {
            p = p->next;
            q = q->next->next;
        }
        return p;
    }

    // 偶数时，返回前一个节点
    ListNode* middleNode2(ListNode* head) {
        ListNode* p = head;
        ListNode* q = head;
        while (q && q->next && q->next->next) {
            p = p->next;
            q = q->next->next;
        }
        return p;
    }
};