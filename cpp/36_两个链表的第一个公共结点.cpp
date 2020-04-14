#include <iostream>
#include <map>

typedef struct ListNode {
    int val;
    ListNode* next;
    ListNode(int x) : val(x), next(nullptr) {}
} ListNode;

class Solution {
public:
    // 字典方式
    ListNode* FindFirstCommonNode(ListNode* h1, ListNode* h2) {
        if (h1 == nullptr || h2 == nullptr) {
            return nullptr;
        }

        std::map<ListNode*, int> map;

        ListNode* tmp = h1;
        while (tmp) {
            map[tmp] = tmp->val;
            tmp = tmp->next;
        }

        tmp = h2;
        while (tmp) {
            if (map.count(tmp) == 1) {
                return tmp;
            }
            tmp = tmp->next;
        }

        return nullptr;
    }

    // 高效的迭代方式
    ListNode* FindFirstCommonNode2(ListNode* h1, ListNode* h2) {
        ListNode* t1 = h1;
        ListNode* t2 = h2;
        while (t1 != t2) {
            t1 = (t1 == nullptr ? h2 : t1->next);
            t2 = (t2 == nullptr ? h1 : t2->next);
        }
        return t1;
    }
};

int main(int argc, char* argv[])
{
    // 需要补充测试用例
    return 0;
}