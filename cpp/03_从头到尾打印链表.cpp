#include <iostream>
#include <vector>
#include <stack>

typedef struct ListNode {
    int val;
    ListNode* next;
    ListNode (int x, ListNode* ptr) : val(x), next(ptr) {}
    // 以上是结构体的构造函数
} ListNode;

class Solution {
public:
    // 从头部插入节点
    void insertHead(ListNode* head, int val) {
        if (head == nullptr) {
            return;
        }
        ListNode* tmp = new ListNode(val, head->next);
        head->next = tmp;
    }

    // 顺序打印
    void printfList(ListNode* head) {
        while (head != nullptr && head->next != nullptr) {
            std::cout << head->next->val << std::endl;
            head = head->next;
        }
    }

    // 从尾部打印
    void printListFromTailToHead(ListNode* head) {
        if (head != nullptr && head->next != nullptr) {
            printListFromTailToHead(head->next);
            std::cout << head->next->val << std::endl;
        } else {
            return;
        }
    }

    // 尾部打印（这种方式输出参数有问题）
    std::vector<int> printListFromTailToHead2(ListNode* head) {
        std::vector<int> vec = {};
        std::vector<int> vec2 = {};
        if (head != nullptr) {
            vec2 = printListFromTailToHead2(head->next);
            vec.insert(vec.end(), vec2.begin(), vec2.end());
            vec.push_back(head->val);
        }
        return vec;
    }

    // 头插法形成反向链表，然后输出
    void printListFromTailToHead3(ListNode* head) {
        ListNode* newhead = new ListNode(0, nullptr);
        ListNode* tmp = head;
        while (tmp != nullptr) {
            insertHead(newhead, tmp->val);
            tmp = tmp->next;
        }
        printfList(newhead);
    }

    // 其他版本，未经测试
    std::vector<int> printListFromTailToHead4(ListNode * head) {
        std::vector<int> ret;
        if (head == nullptr) {
            return ret;
        }
        ListNode* p = new ListNode(0, nullptr);
        while (head != nullptr) {
            ListNode* tmp = p->next;
            p->next = head;
            head = head->next;
            p->next->next = tmp;
        }
        while (p->next != nullptr) {
            ret.push_back(p->val);
            p = p->next;
        }
        return ret;
    }

    // 使用堆栈
    std::vector<int> printListFromTailToHead5(ListNode* head) {
        std::vector<int> result;
        std::stack<int> arr;
        ListNode* p = head;
        while (p != nullptr) {
            arr.push(p->val);
            p = p->next;
        }
        int len = arr.size();
        for (int i = 0; i < len; i++) {
            result.push_back(arr.top());
            arr.pop();
        }
        return result;
    }

    // 不断在vector的头部插入元素
    std::vector<int> printListFromTailToHead6(ListNode* head) {
        std::vector<int> vec;
        while (head != nullptr) {
            vec.insert(vec.begin(), head->val);
            head = head->next;
        }
        return vec;
    }
};

int main (int argc, char* argv[])
{
    Solution s;
    ListNode* head = new ListNode(0, nullptr);

    // insert from head
    s.insertHead(head, 5);
    s.insertHead(head, 8);
    s.insertHead(head, 10);

    // print
    s.printfList(head);

    // print from tail
    s.printListFromTailToHead(head);
    s.printListFromTailToHead3(head);

    // test
    std::vector<int> vec = s.printListFromTailToHead6(head);
    for (auto i : vec) {
        std::cout << i << std::endl;
    }
    
    return 0;
}