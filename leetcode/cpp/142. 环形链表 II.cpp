typedef struct ListNode {
    int val;
    ListNode* next;
    ListNode(int x) : val(x), next(nullptr) {}
} ListNode;

class Solution {
public:
    // 双指针法
    ListNode* detectCycle(ListNode* head) {
        // 特殊情况判断
        if (head == nullptr or head->next == nullptr) {
            return nullptr;
        }
        // 快慢指针遍历
        ListNode* p = head;
        ListNode* q = head;
        while (q && q->next) {
            p = p->next;
            q = q->next->next;
            if (p == q) {
                break;
            }
        }
        // 判断是否有环
        if (p != q) {
            return nullptr;
        }
        // 有环确定入口
        p = head;
        while (p != q) {
            p = p->next;
            q = q->next;
        }
        return p;
    }
};