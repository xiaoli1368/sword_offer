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
    std::map<ListNode*, int> map;
    ListNode* EntryNodeOfLoop(ListNode* head) {
        while (head != nullptr) {
            if (map.count(head) == 0) {
                map[head] = head->val;
                head = head->next;
            } else {
                return head;
            }
        }
        
        return nullptr;
    }
};