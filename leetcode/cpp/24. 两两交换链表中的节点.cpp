typedef struct ListNode {
    int val;
    ListNode* next;
    ListNode(int x) : val(x), next(nullptr) {}
} ListNode;

class Solution {
public:
    // 递归法
    ListNode* swapPairs(ListNode* head) {
        if (head == nullptr || head->next == nullptr) {
            return head;
        }
        ListNode* newHead = head->next;
        ListNode* skipTwo = head->next->next;
        newHead->next = head;
        head->next = swapPairs(skipTwo);
        return newHead;
    }

    // 迭代法，存在优化空间
    ListNode* swapPairs2(ListNode* head) {
        if (head == nullptr || head->next == nullptr) {
            return head;
        }

        ListNode* newHead = new ListNode(0);
        newHead->next = head;
        ListNode* last = newHead;
        ListNode* p = head;
        ListNode* q = head->next;

        while (p && q) {
            ListNode* skipTwo = q->next;
            last->next = q;
            q->next = p;
            p->next = skipTwo;
            if (skipTwo == nullptr) {
                break;
            }
            last = p;
            p = skipTwo;
            q = skipTwo->next;
        }

        return newHead->next;
    }

    // 迭代法，优化版
    ListNode* swapPairs(ListNode* head) {
        ListNode* newHead = new ListNode(0);
        newHead->next = head;
        ListNode* last = newHead;
        ListNode* curr = head;
        while (curr && curr->next) {
            ListNode* skipTwo = curr->next->next;
            last->next = curr->next;
            last->next->next = curr;
            curr->next = skipTwo;
            last = curr;
            curr = skipTwo;
        }
        return newHead->next;
    }
};