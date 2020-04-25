/*
struct ListNode {
    int val;
    struct ListNode *next;
    ListNode(int x) :
        val(x), next(NULL) {
    }
};
*/
class Solution {
public:
    // 输出一个结点，返回从这里开始有多少个重复的结点，next_head为不重复的下一个结点
    // 这里注意要用引用
    int checkSame(ListNode* head, ListNode* & next_head) {
        int cnt = 0;
        while (head != nullptr && head->next != nullptr) {
            if (head->val != head->next->val) {
                next_head = head->next;
                return cnt;
            } else {
                cnt++;
                head = head->next;
            }
        }
        
        next_head = nullptr;
        return cnt;
    }
    
    ListNode* deleteDuplication(ListNode* head) {
        if (head == nullptr) {
            return nullptr;
        }
        
        // 为了检测head是否存在重复，需要新加一个额外的head
        ListNode* new_head = new ListNode(0);
        new_head->next = head;
        ListNode* curr = new_head;
        ListNode* tmp = nullptr;
        
        while (curr != nullptr) {
            if (checkSame(curr->next, tmp) == 0) {
                curr = curr->next;
            } else {
                curr->next = tmp;
            }
        }
        
        return new_head->next;
    }
};