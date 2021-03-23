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

	// ===== 优化版 =====
    ListNode* mergeKLists_(vector<ListNode*>& lists, int l, int h) {
        if (l > h) {
            return nullptr;
        }
        if (l == h) {
            return lists[l];
        }
        int m = l + (h - l) / 2;
        ListNode* p = mergeKLists_(lists, l, m);
        ListNode* q = mergeKLists_(lists, m + 1, h);
        ListNode* newHead = new ListNode();
        ListNode* curr = newHead;
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

    ListNode* mergeKLists(vector<ListNode*>& lists) {
        return mergeKLists_(lists, 0, lists.size() - 1);
    }

	// ===== 使用优先队列 =====
    struct Comp{
        bool operator() (ListNode* p, ListNode* q) {
            if (p == nullptr) {
                return true;
            }
            if (q == nullptr) {
                return false;
            }
            return p->val > q->val;
        }
    };

    ListNode* mergeKLists(vector<ListNode*>& lists) {
        priority_queue<ListNode*, vector<ListNode*>, Comp> q;
        for (const auto& head : lists) {
            q.push(head);
        }
        ListNode* newHead = new ListNode(0), *curr = newHead;
        while (!q.empty() && curr) {
            curr->next = q.top();
            curr = curr->next;
            q.pop();
            if (curr && curr->next) {
                q.push(curr->next);
            }
        }
        return newHead->next;
    }
};