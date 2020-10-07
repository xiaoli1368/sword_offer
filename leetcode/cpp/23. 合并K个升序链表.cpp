// 合并k个有序链表
#include <vector>

typedef struct ListNode {
	int val;
	ListNode* next;
	ListNode(int x) : val(x), next(nullptr) {}
} ListNode;

class Solution {
public:
    // 合并两个有序链表
	ListNode* mergeTwoLists(ListNode* p, ListNode* q) {
		if (p == nullptr) {
			return q;
		}
		if (q == nullptr) {
			return p;
		}
		if (p->val < q->val) {
			p->next = mergeTwoLists(p->next, q);
			return p;
		} else {
			q->next = mergeTwoLists(p, q->next);
			return q;
		}
	}

	// 合并k个有序链表，使用索引确定区间
	ListNode* merge(std::vector<ListNode*>& lists, int l, int h) {
		if (l > h) {
			return nullptr;
		}
		if (l == h) {
			return lists[l];
		}
		int m = l + (h - l) / 2;
		ListNode* p = merge(lists, l, m);
		ListNode* q = merge(lists, m + 1, h);
		return mergeTwoLists(p, q);
	}

    // 合并k个有序链表，leetcode接口
    ListNode* mergeKLists(std::vector<ListNode*>& lists) {
		return merge(lists, 0, lists.size() - 1);
	}
};