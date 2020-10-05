#include <ListNode.h>
#include <stack>

class Solution {
public:
    // 双栈法
    ListNode* addTwoNumbers(ListNode* p, ListNode* q) {
		if (p == nullptr) {
			return q;
		}
		if (q == nullptr) {
			return p;
		}
		
		// 转换为双栈
		std::stack<int> pstack, qstack;
		ListNode* tmp = p;
		while (tmp) {
			pstack.push(tmp->val);
			tmp = tmp->next;
		}
		tmp = q;
		while (tmp) {
			qstack.push(tmp->val);
			tmp = tmp->next;
		}

		// 从两个栈的顶部开始相加，s为进位
		int s = 0;
		ListNode* newhead = nullptr;
		ListNode* lasthead = nullptr;
		while (!pstack.empty() || !qstack.empty() || s) {
			if (!pstack.empty()) {
				s += pstack.top();
				pstack.pop();
			}
			if (!qstack.empty()) {
				s += qstack.top();
				qstack.pop();
			}
			newhead = new ListNode(s % 10);
			newhead->next = lasthead;
			lasthead = newhead;
			s /= 10;
		}

		return newhead;
	}
};