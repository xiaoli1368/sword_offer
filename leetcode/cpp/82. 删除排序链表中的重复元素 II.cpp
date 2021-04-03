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
    ListNode* deleteDuplicates(ListNode* head) {
        ListNode *last = nullptr, *curr = head, *next = nullptr;
        ListNode *new_head = new ListNode(), *new_curr = new_head;
        while (curr) {
            next = curr->next;
            if ((last == nullptr || last->val != curr->val) && (next == nullptr || curr->val != next->val)) {
                new_curr->next = curr;
                new_curr = new_curr->next;
            }
            last = curr;
            curr = curr->next;
        }
        new_curr->next = nullptr;
        return new_head->next;
    }
};