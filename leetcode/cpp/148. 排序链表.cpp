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

	// 插入排序
	ListNode* sortList2(ListNode* head) {
		ListNode* newHead = new ListNode(0x80000000);
		newHead->next = head;
		ListNode *lastp = newHead, *p = head;
		while (p) {
			ListNode* nextp = p->next;
			ListNode* q = newHead; // 表示待插入位置的前一个节点
			while (q && q->next && q->next->val < p->val) {
				q = q->next;
			}
			if (q == lastp) {
				lastp = p;
				p = nextp;
				continue;
			}
			ListNode* tmp = q->next;
			q->next = p;
			p->next = tmp;
			lastp->next = nextp;
			p = nextp;
		}
		return newHead->next;
	}
};