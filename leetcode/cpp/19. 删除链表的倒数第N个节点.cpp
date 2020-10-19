typedef struct ListNode {
	int val;
	ListNode* next;
	ListNode(int x) : val(x), next(nullptr) {}
} ListNode;

class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
		int cnt = 0;
		ListNode* newHead = new ListNode(0);
		ListNode *p = newHead, *q = newHead;
		newHead->next = head;
		while (q) {
			q = q->next;
			if (cnt > n) {
				p = p->next;
			}
			cnt += 1;
		}
		p->next = p->next->next;
		return newHead->next;
	}
};

int main(int argc, char* argv[])
{
	return 0;
}