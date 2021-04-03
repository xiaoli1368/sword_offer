/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* reverseListNode(ListNode* head) {
        ListNode *last = nullptr, *next;
        while (head) {
            next = head->next;
            head->next = last;
            last = head;
            head = next;
        }
        return last;
    }

    bool isPalindrome(ListNode* head) {
        // 特殊情况
        if (head == nullptr || head->next == nullptr) {
            return true;
        }

        // 找到中间节点并截断
        ListNode *fast = head, *slow = head, *mid;
        while (fast && fast->next && fast->next->next) {
            slow = slow->next;
            fast = fast->next->next;
        }
        mid = slow->next;
        slow->next = nullptr;

        // 后半部分翻转
        ListNode *p = head;
        ListNode *q = reverseListNode(mid);
        
        // 判断两链表是否回文
        while (p && q && p->val == q->val) {
            p = p->next;
            q = q->next;
        }
        return p == nullptr || (q == nullptr && p->next == nullptr);
    }
};