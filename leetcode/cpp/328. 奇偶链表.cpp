/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* oddEvenList(ListNode* head) {
        ListNode *odd = new ListNode(), *curr_odd = odd;
        ListNode *even = new ListNode(), *curr_even = even;
        while (head) {
            curr_odd->next = head;
            curr_odd = curr_odd->next;
            head = head->next;
            if (head) {
                curr_even->next = head;
                curr_even = curr_even->next;
                head = head->next;
            }
        }
        curr_even->next = nullptr;
        curr_odd->next = even->next;
        return odd->next;
    }
};