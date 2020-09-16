#ifndef STACKNODE_H
#define STACKNODE_H

#include <stdio.h>
#include <vector>

// 定义堆栈
typedef struct StackNode {
    int val;
    StackNode* next;
    StackNode(int x) : val(x), next(nullptr) {};
} StackNode;

// 插入
void StackNode_push(StackNode*& head, int val) {
    StackNode* newHead = new StackNode(val);
    newHead->next = head;
    head = newHead;
} 

// 弹出
void StackNode_pop(StackNode*& head) {
    if (head == nullptr) {
        return;
    }
    
    StackNode* oldHead = head;
    head = head->next;
    delete oldHead;
}

// 返回顶部的值
int StackNode_top(StackNode* head) {
    if (head == nullptr) {
        return 0;
    }

    return head->val;
}

// 获取长度
int StackNode_size(StackNode* head) {
    int size = 0;
    while (head != nullptr) {
        size++;
    }

    return size;
}

// 获取第k个值
int StackNode_getValue(StackNode* head, int k) {
    int cnt = 0;
    while (head != nullptr) {
        cnt++;
        if (cnt == k) {
            return head->val;
        }
    }

    return 0;
}

// 修改第k个值
void StackNode_setValue(StackNode* head, int k, int val) {
    int cnt = 0;
    while (head != nullptr) {
        cnt++;
        if (cnt == k) {
            head->val = val;
            break;
        }
    }

    return;
}

// 从vec中创建
StackNode* StackNode_creatFromVec(std::vector<int>& vec) {
    if (vec.empty()) {
        return nullptr;
    }

    StackNode* head = new StackNode(vec[0]);
    StackNode* curr = head;

    for (int i = 1; i < vec.size(); i++) {
        curr->next = new StackNode(vec[i]);
        curr = curr->next;
    }

    return head;
}

// 保存到vec
std::vector<int> StackNode_saveToVec(StackNode* head) {
    if (head == nullptr) {
        return std::vector<int>{};
    }

    std::vector<int> ret;
    while (head != nullptr) {
        ret.push_back(head->val);
        head = head->next;
    }

    return ret;
}

// 顺序打印
void StackNode_print(StackNode* head) {
    if (head == nullptr) {
        return;
    }

    while (head != nullptr) {
        printf("%d ", head->val);
        head = head->next;
    }

    printf("\n");
    return;
}

#endif