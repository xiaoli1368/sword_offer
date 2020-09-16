#include <iostream>
#include <vector>
#include <map>
#include <queue>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <sys/time.h>

typedef struct RandomListNode {
    int label;
    RandomListNode* next;
    RandomListNode* random;
    RandomListNode(int x) : label(x), next(nullptr), random(nullptr) {};
} RandomListNode;

class Solution {
public:
    // 1. map映射方法
    RandomListNode* Clone1(RandomListNode* head) {
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

    // 2. map方法优化版
    RandomListNode* Clone2(RandomListNode* h1) {
        if (h1 == nullptr) {
            return nullptr;
        }

        // 完全建立线性节点以及映射
        RandomListNode* h2 = new RandomListNode(0);
        RandomListNode* curr1 = h1;
        RandomListNode* curr2 = h2;
        std::map<RandomListNode*, RandomListNode*> map;
        map[nullptr] = nullptr;

        while (curr1) {
            curr2->next = new RandomListNode(curr1->label);
            curr2 = curr2->next;
            map[curr1] = curr2;
            curr1 = curr1->next;
        }

        // 建立随机节点
        while (h1) {
            map[h1]->random = map[h1->random];
            h1 = h1->next;
        }

        return h2->next;
    }

    // 3. dfs图遍历
    // 从头结点 head 开始拷贝；
    // 由于一个结点可能被多个指针指到，因此如果该结点已被拷贝，则不需要重复拷贝；
    // 如果还没拷贝该结点，则创建一个新的结点进行拷贝，并将拷贝过的结点保存在哈希表中；
    // 使用递归拷贝所有的 next 结点，再递归拷贝所有的 random 结点。
    // 参考：https://leetcode-cn.com/problems/fu-za-lian-biao-de-fu-zhi-lcof/solution/lian-biao-de-shen-kao-bei-by-z1m/
    RandomListNode* Clone3(RandomListNode* head) {
        std::map<RandomListNode*, RandomListNode*> map;
        return dfs(head, map);
    }

    RandomListNode* dfs(RandomListNode* head, std::map<RandomListNode*, RandomListNode*>& map) {
        if (head == nullptr) {
            return nullptr;
        }
        if (map.count(head)) {
            return map[head];
        }

        // 创建新节点
        RandomListNode* copy = new RandomListNode(head->label);
        map[head] = copy;
        copy->next = dfs(head->next, map);
        copy->random = dfs(head->random, map);
        
        return copy;
    }

    // 4. bfs图遍历
    // 创建哈希表保存已拷贝结点，格式 {原结点：拷贝结点}
    // 创建队列，并将头结点入队；
    // 当队列不为空时，弹出一个结点，如果该结点的 next 结点未被拷贝过，则拷贝 next 结点并加入队列；同理，如果该结点的 random 结点未被拷贝过，则拷贝 random 结点并加入队列；
    // 参考：https://leetcode-cn.com/problems/fu-za-lian-biao-de-fu-zhi-lcof/solution/lian-biao-de-shen-kao-bei-by-z1m/
    RandomListNode* Clone4(RandomListNode* head) {
        std::map<RandomListNode*, RandomListNode*> map;
        return bfs(head, map);
    }

    RandomListNode* bfs(RandomListNode* head, std::map<RandomListNode*, RandomListNode*>& map) {
        if (head == nullptr) {
            return nullptr;
        }

        // 创建新节点
        RandomListNode* clone = new RandomListNode(head->label);
        std::queue<RandomListNode*> queue;
        queue.push(head);
        map[head] = clone;

        while (!queue.empty()) {
            RandomListNode* tmp = queue.front();
            queue.pop();

            if (tmp->next != nullptr && map.count(tmp->next) == 0) {
                map[tmp->next] = new RandomListNode(tmp->next->label);
                queue.push(tmp->next);
            }

            if (tmp->random != nullptr && map.count(tmp->random) == 0) {
                map[tmp->random] = new RandomListNode(tmp->random->label);
                queue.push(tmp->random);
            }

            map[tmp]->next = map[tmp->next];
            map[tmp]->random = map[tmp->random];
        }

        return clone;
    }

    // 5. next指针遍历
    RandomListNode* Clone5(RandomListNode* head) {
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

    // ===== 工具函数 =====

    // 生成具备题目要求的链表
    RandomListNode* generete_RandomListNode(int num, int maxVal) {
        if (num <= 0 || maxVal <= 0) {
            return nullptr;
        }

        // 生成基本的链表
        srand(time(nullptr));
        RandomListNode* head = new RandomListNode(0);
        RandomListNode* curr = head;
        std::vector<RandomListNode*> vec;
        for (int i = 0; i < num; i++) {
            curr->next = new RandomListNode(rand() % maxVal);
            curr = curr->next;
            vec.push_back(curr);
        }

        // 建立随机关系
        curr = head->next;
        while (curr != nullptr) {
            curr->random = vec[rand() % num];
            curr = curr->next;
        }

        return head->next;
    }

    // 判断两个random链表是否相同
    bool isSame(RandomListNode* h1, RandomListNode* h2) {
        while (h1 != nullptr && h2 != nullptr) {
            if (h1->label != h2->label) {
                break;
            }
            if (h1->random == nullptr && h2->random != nullptr) {
                break;
            }
            if (h1->random != nullptr && h2->random == nullptr) {
                break;
            }
            if (h1->random && h2->random && h1->random->label != h2->random->label) {
                break;
            }
            h1 = h1->next;
            h2 = h2->next;
        }

        return h1 == nullptr && h2 == nullptr;
    }

    // 打印一维链表
    void printf_1d_RandomListNode(RandomListNode* head) {
        int cnt = 0;
        while (head != nullptr) {
            printf("%d, ", head->label);
            head = head->next;
            if (++cnt >= 20) {
                printf("..., ");
                break;
            }
        }
    }

    // 测试函数
    void test(RandomListNode* head) {
        struct timeval start, end;
        RandomListNode* result;

        printf("=====\n");
        for (auto & func : this->func_vec_) {
            gettimeofday(&start, nullptr);
            result = (this->*func)(head);
            gettimeofday(&end, nullptr);

            printf("result: ");
            if (isSame(head, result)) {
                printf("True, ");
            } else {
                printf("False, ");
            }
            printf_1d_RandomListNode(result);
            printf("time(us): %ld\n", end.tv_usec - start.tv_usec);
        }
    }

private:
    typedef RandomListNode* (Solution::*func_ptr)(RandomListNode*);
    std::vector<func_ptr> func_vec_ = {&Solution::Clone1,
                                       &Solution::Clone2,
                                       &Solution::Clone3,
                                       &Solution::Clone4,
                                       &Solution::Clone5};
};

int main(int argc, char* argv[]) 
{
    Solution s;
    RandomListNode* head1 = s.generete_RandomListNode(100, 100);
    s.test(head1);
    return 0;
}