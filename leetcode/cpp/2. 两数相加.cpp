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
    // 递归版，多函数法，存在优化空间
    ListNode* addTwoNumbers1(ListNode* p, ListNode* q) {
		return addThree(p, q, 0);
	}

	// 递归版，高效写法
	ListNode* addTwoNumbers2(ListNode* p, ListNode* q) {
		return add(p, q, 0);
	}

	// 迭代法，高效写法
	ListNode* addTwoNumbers3(ListNode* p, ListNode* q) {
		int s = 0;
		ListNode* head = new ListNode(0);
		ListNode* curr = head;

		while (p || q || s) {
			if (p) {
				s += p->val;
				p = p->next;
			}
			if (q) {
				s += q->val;
				q = q->next;
			}
			curr->next = new ListNode(s % 10);
			curr = curr->next;
			s /= 10;
		}

		return head->next;
	}

	// ===== 工具函数 =====
	// 只有进位的加法
	ListNode* addOne(int s) {
		if (s == 0) {
			return nullptr;
		}
		ListNode* head = new ListNode(s);
		return head;
	}

	// 单链表和进位的加法
	ListNode* addTwo(ListNode* p, int s) {
		if (p == nullptr) {
			return addOne(s);
		}
		int value = p->val + s;
		if (value >= 10) {
			value -= 10;
			s = 1;
		} else {
			s = 0;
		}
		ListNode* head = new ListNode(value);
		head->next = addTwo(p->next, s);
		return head;
	}

	// 两个链表和进位的加法
	ListNode* addThree(ListNode* p, ListNode* q, int s) {
		if (p == nullptr) {
			return addTwo(q, s);
		}
		if (q == nullptr) {
			return addTwo(p, s);
		}
		int value = p->val + q->val + s;
		if (value >= 10) {
			value -= 10;
			s = 1;
		} else {
			s = 0;
		}
		ListNode* head = new ListNode(value);
		head->next = addThree(p->next, q->next, s);
		return head;
	}

	// 一个函数覆盖两个链表和进位的所有加法情况
	ListNode* add(ListNode* p, ListNode* q, int s) {
		if (p == nullptr && q == nullptr && s == 0) {
			return nullptr;
		}
		if (p) {
			s += p->val;
			p = p->next;
		}
		if (q) {
			s += q->val;
			q = q->next;
		}
		ListNode* head = new ListNode(s % 10);
		head->next = add(p, q, s / 10);
		return head;
	} 
};