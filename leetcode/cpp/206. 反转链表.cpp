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
    ListNode* reverseList(ListNode* head) {
        ListNode* last = nullptr;
        while (head) {
            ListNode* next = head->next;
            head->next = last;
            last = head;
            head = next;
        }
        return last;
    }

    ListNode* reverseList(ListNode* head) {
		// 这里进行判断，是为了保证head->next有值
        if (head == nullptr || head->next == nullptr) {
            return head;
        }
        ListNode* curr = reverseList(head->next);
        head->next->next = head;
        head->next = nullptr;
        return curr;
    }
};