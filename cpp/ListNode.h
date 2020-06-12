#ifndef LISTNODE_H
#define LISTNODE_H

#include <vector>

// 定义单链表
typedef struct ListNode {
    int val;
    ListNode* next;
    ListNode(int x) : val(x), next(nullptr) {}
} ListNode;

// 尾部插入
void ListNode_insertTail(ListNode* head, int val) {
    if (head == nullptr) {
        return;
    }
    while (head->next != nullptr) {
        head = head->next;
    }
    head->next = new ListNode(val);
}

// 头部插入
void ListNode_insertHead(ListNode* head, int val) {
    if (head == nullptr) {
        return;
    }

    ListNode* tmp = head->next;
    head->next = new ListNode(val); 
    head->next->next = tmp;
}

// 尾部删除
void ListNode_deleteTail(ListNode* head) {
    if (head == nullptr || head->next == nullptr) {
        return;
    }

    while (head->next->next != nullptr) {
        head = head->next;
    }

    delete head->next;
    head->next = nullptr;
}

// 从vec中创建，头节点默认为0
ListNode* ListNode_creatFromVec(std::vector<int>& vec) {
    if (vec.empty()) {
        return nullptr;
    }

    ListNode* head = new ListNode(0);
    ListNode* currhead = head;

    for (auto i : vec) {
        currhead->next = new ListNode(i);
        currhead = currhead->next;
    }

    return head;
}

// 顺序保存到vec
std::vector<int> ListNode_saveToVec(ListNode* head) {
    if (head == nullptr) {
        return std::vector<int>{};
    }
    head = head->next;

    std::vector<int> ret;
    while (head != nullptr) {
        ret.push_back(head->val);
        head = head->next;
    }
    return ret;
}

// 顺序打印
// ifJumpHead: 是否跳过头节点
// printRow: 是否打印为一行，否则打印为一列
void ListNode_print(ListNode* head, bool ifJumpHead = true, bool printRow = true) {
    if (head == nullptr) {
        return;
    }

    if (ifJumpHead) {
        head = head->next;
    }

    std::string argv = "%d";
    argv += printRow ? " " : "\n";

    while (head != nullptr) {
        printf(argv.c_str(), head->val);
        head = head->next;
    }
}

// 清空所有节点，不保留默认的头节点
void ListNode_clear(ListNode* head) {
    if (head == nullptr) {
        return;
    }

    while (head != nullptr) {
        ListNode* currNode = head;
        head = head->next;
        delete currNode;
    }
}

#endif