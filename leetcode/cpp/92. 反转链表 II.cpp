/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* reverseBetween(ListNode* head, int m, int n) {
        if (head == nullptr || m <= 0 || n <= 0 || m > n) {
            return head;
        } 

        // 考虑到头节点可能翻转，因此需要额外的头节点
        // 将链表划分为4个区域[newHead, mprev, mnode, nnode, nnext]
        ListNode* newHead = new ListNode(0, head);

        // 找到第m-1个节点
        int cnt = 0;
        ListNode* mprev = newHead;
        while (mprev && cnt < m - 1) {
            mprev = mprev->next;
            cnt += 1;
        }

        // 如果长度不满足要求
        if (mprev == nullptr || mprev->next == nullptr) {
            return head;
        }

        // 翻转[m,n]段
        ListNode* mnode = mprev->next;
        ListNode* nnext = mprev->next;
        ListNode* nnode = nullptr;
        while (nnext && cnt < n) {
            ListNode* next = nnext->next;
            nnext->next = nnode;
            nnode = nnext;
            nnext = next;
            cnt += 1;
        }

        // 进行拼接输出
        mprev->next = nnode;
        mnode->next = nnext;
        return newHead->next;
    }

    // 使用头插法，这种方式耗费空间
    ListNode* reverseBetween(ListNode* head, int m, int n) {
        if (head == nullptr || m <= 0 || n <= 0 || m > n) {
            return head;
        } 

        // 考虑到头节点可能翻转，因此需要额外的头节点
        ListNode* newHead = new ListNode(0);
        ListNode* curr = newHead; // 定位到当前链表的末尾
        ListNode* mprev = newHead; // 定位到第m-1个节点

        int cnt = 1;
        while (head) {
            // [0, m-1] [n+1, inf]，正常遍历
            if (cnt < m || cnt > n) {
                curr->next = new ListNode(head->val);
                mprev = mprev->next;
            } else { // 开始头插法[m, n]
                ListNode* next = mprev->next;
                mprev->next = new ListNode(head->val);
                mprev->next->next = next;
            }
            if (curr->next) {
                curr = curr->next;
            }
            // 更新状态
            cnt += 1;
            head = head->next;
        }
        return newHead->next;
    }
};