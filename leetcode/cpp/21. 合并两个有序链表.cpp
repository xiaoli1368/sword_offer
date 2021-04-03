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

#include <ListNode.h>

class Solution {
public:
    // 循环法
    ListNode* mergeTwoLists(ListNode* p, ListNode* q) {
        if (p == nullptr) {
            return q;
        }
        if (q == nullptr) {
            return p;
        }

        ListNode* head = new ListNode(0);
        ListNode* curr = head;
        while (p && q) {
            if (p->val < q->val) {
                curr->next = new ListNode(p->val);
                p = p->next;
            } else {
                curr->next = new ListNode(q->val);
                q = q->next;
            }
            curr = curr->next;
        }
        curr->next = p ? p : q;

        return head->next;
    }

	// 递归法
	ListNode* mergeTwoLists2(ListNode* p, ListNode* q) {
		if (p == nullptr) {
			return q;
		}
		if (q == nullptr) {
			return p;
		}
		if (p->val < q->val) {
			p->next = mergeTwoLists2(p->next, q);
			return p;
		} else {
			q->next = mergeTwoLists2(p, q->next);
			return q;
		}
	}

    ListNode* mergeTwoLists(ListNode* p, ListNode* q) {
        ListNode *newHead = new ListNode(), *curr = newHead;
        while (p && q) {
            if (p->val < q->val) {
                curr->next = p;
                p = p->next;
            } else {
                curr->next = q;
                q = q->next;
            }
            curr = curr->next;
        }
        curr->next = (p ? p : q);
        return newHead->next;
    }
};