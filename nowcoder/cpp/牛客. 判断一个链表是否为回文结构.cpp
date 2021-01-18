/**
 * struct ListNode {
 *	int val;
 *	struct ListNode *next;
 * };
 */

class Solution {
public:
    /**
     * 
     * @param head ListNode类 the head
     * @return bool布尔型
     */
    bool isPail(ListNode* head) {
        // write code here
        if (head == nullptr || head->next == nullptr) {
            return true;
        }
        
        std::vector<int> vec;
        while (head) {
            vec.push_back(head->val);
            head = head->next;
        }
        
        int l = 0, h = vec.size() - 1;
        while (l < h) {
            if (vec[l++] != vec[h--]) {
                return false;
            }
        }
        return true;
    }

    bool isPail(ListNode* head) {
        // write code here
        if (head == nullptr || head->next == nullptr) {
            return true;
        }
        
        // 找到偏右的中间节点，并且前半部分翻转
        ListNode *tmp = nullptr, *last = nullptr;
        ListNode *slow = head, *fast = head;
        while (fast && fast->next) {
            fast = fast->next->next;
            tmp = slow->next;
            slow->next = last;
            last = slow;
            slow = tmp;
        }
        
        // 进行判断
        ListNode *p = last;
        ListNode *q = (fast == nullptr ? slow: slow->next);
        while (p && q && p->val == q->val) {
            p = p->next;
            q = q->next;
        }
        return p == nullptr && q == nullptr;
    }
};