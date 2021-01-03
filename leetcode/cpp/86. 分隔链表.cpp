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
    ListNode* partition(ListNode* head, int x) {
        if (head == nullptr) {
            return head;
        }

        ListNode* low = new ListNode(0);
        ListNode* high = new ListNode(0);
        ListNode *lh = low, *hh = high;

        while (head) {
            if (head->val < x) {
                lh->next = head;
                lh = lh->next;
            } else {
                hh->next = head;
                hh = hh->next;
            }
            head = head->next;
        }

        lh->next = high->next;
        hh->next = nullptr;
        return low->next;
    }
};