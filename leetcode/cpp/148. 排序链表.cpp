#include <ListNode.h>

// 定义单链表
typedef struct ListNode {
    int val;
    ListNode* next;
    ListNode(int x) : val(x), next(nullptr) {}
	ListNode(int x, ListNode* next) : val(x), next(next) {}
} ListNode;

class Solution {
public:
	// ===== 归并 =====
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

	// ===== 插入排序 =====
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

	// ===== 快排 =====
	// 有不同的方式，但是效率都挺低的
	// 这里的排序，直接交换两个节点的val就行了
	// 而没有实际的移动两个Node

	// 交换函数
	void swap(ListNode* p, ListNode* q) {
		int tmp = p->val;
		p->val = q->val;
		q->val = tmp;
	}

	// 快排分区函数，找到middle节点的前驱节点
	ListNode* partition(ListNode* head, ListNode* tail) {
		// 新建一个start节点头，并初始化
		ListNode tmp(0, head);
		ListNode* start = &tmp;
		ListNode* curr = head;
		// 开始循环分区
		while (curr) {
			if (curr->val < tail->val) {
				start = start->next;
				swap(curr, start);
			}
			curr = curr->next;
		}
		ListNode* midLeft = start;
		start = start->next;
		swap(tail, start);
		return midLeft;
	}

	// 快排递归函数
	void quickSort(ListNode* head, ListNode* tail) {
		if (head == tail || tail->next == head) {
			return;
		}
		ListNode* midLeft = partition(head, tail);
		quickSort(head, midLeft);
		quickSort(midLeft->next->next, tail);
		return;
	}

	// 链表快排
	ListNode* sortList3(ListNode* head) {
		// 处理特殊情况
		if (head == nullptr) {
			return nullptr;
		}

		// 找到非空的末尾节点
		ListNode* tail = head;
		while (tail && tail->next) {
			tail = tail->next;
		}

		// 进行快排并输出结果
		quickSort(head, tail);
		return head;
	}
};