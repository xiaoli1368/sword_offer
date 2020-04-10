#include <iostream>
#include <map>

typedef struct RandomListNode {
    int label;
    RandomListNode* next;
    RandomListNode* random;
    RandomListNode(int x) : label(x), next(nullptr), random(nullptr) {};
} RandomListNode;

class Solution {
public:
    // next指针遍历
    RandomListNode* Clone(RandomListNode* head) {
        if (head == nullptr) {
            return nullptr;
        }
        
        // 1、复制每个结点，如复制结点A得到A1，将结点A1插到结点A后面；
        // 注意尾部的nullptr没有复制
        RandomListNode* currNode = head;
        RandomListNode* nextNode = nullptr;
        while (currNode != nullptr) {
            nextNode = currNode->next;
            RandomListNode *newNode = new RandomListNode(currNode->label);
            currNode->next = newNode;
            newNode->next = nextNode;
            currNode = nextNode;
        }
        
        // 2、重新遍历链表，复制老结点的随机指针给新结点，如A1.random = A.random.next;
        // 拷贝随机的链接关系
        currNode = head;
        while (currNode != nullptr) {
            currNode->next->random = currNode->random == nullptr ? nullptr : currNode->random->next;
            currNode = currNode->next->next;
        }
        
        // 3、拆分链表，将链表拆分为原链表和复制后的链表
        // 从旧链表分离得到新链表
        currNode = head;
        RandomListNode* headClone = head->next;
        while (currNode != nullptr) {
            RandomListNode* tmp = currNode->next;
            currNode->next = tmp->next;
            tmp->next = tmp->next == nullptr ? nullptr : tmp->next->next;
            currNode = currNode->next;
        }
        
        return headClone;
    }

    // map映射方法
    RandomListNode* Clone2(RandomListNode* head) {
        if (head == nullptr) {
            return nullptr;
        }
        
        // map法, 初始化
        std::map<RandomListNode*, RandomListNode*> map;
        RandomListNode* head1 = head;
        RandomListNode* head2 = new RandomListNode(head1->label);
        RandomListNode* newhead = head2;
        map[head1] = head2;
        
        // 完全复制链表并建立map
        while (head1) {
            if (head1->next) {
                head2->next = new RandomListNode(head1->next->label);
            } else {
                head2->next = nullptr;
            }
            
            head1 = head1->next;
            head2 = head2->next;
            map[head1] = head2;
        }
        
        // 复制随机的链接
        head1 = head;
        head2 = newhead;
        while (head1) {
            head2->random = map[head1->random];
            head1 = head1->next;
            head2 = head2->next;
        }
        
        return newhead;
    }
};

int main(int argc, char* argv) {
    /* 后续补充 */
    return 0;
}