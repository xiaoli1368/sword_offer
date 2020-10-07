/* 定义单链表
typedef struct ListNode {
    int val;
    ListNode* next;
    ListNode(int x) : val(x), next(nullptr) {}
} ListNode
*/

#include <ListNode.h>

class Solution {
public:
    // 找到链表的中点，并且拆分，返回第二个链表的头节点
    ListNode* findMiddle(ListNode* head) {
		if (head == nullptr || head->next == nullptr) {
			return nullptr;
		}
		ListNode* p = head;
		ListNode* q = head;
		ListNode* midHead = nullptr;
		while (q && q->next && q->next->next) {
			p = p->next;
			q = q->next->next;
		}
		midHead = p->next;
		p->next = nullptr;
		return midHead;
	}
	
	// 合并两个有序链表
	ListNode* mergeTwo(ListNode* p, ListNode* q) {
		if (p == nullptr) {
			return q;
		}
		if (q == nullptr) {
			return p;
		}
		if (p->val < q->val) {
			p->next = mergeTwo(p->next, q);
			return p;
		} else {
			q->next = mergeTwo(p, q->next);
			return q;
		}
	}

	// 单链表排序
	ListNode* sortList(ListNode* head) {
		if (head == nullptr || head->next == nullptr) {
			return head;
		}
		ListNode* midHead = findMiddle(head);
		ListNode* p = sortList(head);
		ListNode* q = sortList(midHead);
		return mergeTwo(p, q);
	}
};