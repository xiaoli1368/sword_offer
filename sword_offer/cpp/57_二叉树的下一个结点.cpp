#include <vector>
#include <stdio.h>
#include <sys/time.h>

// 具有双亲节点的二叉树
struct TreeLinkNode {
    int val;
    struct TreeLinkNode *left;
    struct TreeLinkNode *right;
    struct TreeLinkNode *next; // 其实是向上指的father
    TreeLinkNode(int x) :val(x), left(NULL), right(NULL), next(NULL) {}
};

// 先序生成，递归
TreeLinkNode* TreeLinkNode_creatFunc(std::vector<int>& vec, int& begin, int& end, TreeLinkNode* father) {
    if (vec.empty() || begin > end || vec[begin] == -1) {
        begin++;
        return nullptr;
    }

    TreeLinkNode* root = new TreeLinkNode(vec[begin++]);
    root->next = father;
    root->left = TreeLinkNode_creatFunc(vec, begin, end, root);
    root->right = TreeLinkNode_creatFunc(vec, begin, end, root);

    return root;
}

// 从先序序列生成具备双亲节点的二叉树
TreeLinkNode* TreeLinkNode_creatFromFrontOrder(std::vector<int>& vec) {
    int begin = 0;
    int end = vec.size() - 1;
    return TreeLinkNode_creatFunc(vec, begin, end, nullptr);
}

// 层次遍历，把所有节点存储
std::vector<TreeLinkNode*> TreeLinkNode_getAllNode(TreeLinkNode* root) {
    std::vector<TreeLinkNode*> ret;
    std::vector<TreeLinkNode*> curr_list = {root};

    if (root == nullptr) {
        return ret;
    }

    while (!curr_list.empty()) {
        std::vector<TreeLinkNode*> next_list;
        for (auto & node : curr_list) {
            ret.push_back(node);
            if (node->left) {
                next_list.push_back(node->left);
            }
            if (node->right) {
                next_list.push_back(node->right);
            }
        }
        curr_list = next_list;
    }

    return ret;
}

class Solution {
public:
    // 获取当前节点的中序遍历的下一个节点
    TreeLinkNode* GetNext(TreeLinkNode* p) {
        if (p == nullptr) {
            return nullptr;
        }
        
        if (p->right != nullptr) {
            // 右子树非空时，中序遍历右子树，得到一个结点并返回，即最底层的左子树
            p = p->right;
            while (p->left != nullptr) {
                p = p->left;
            }
            return p;
        } else {
            // 右子树为空时，迭代循环，直到满足输出
            // 注意一下循环判断条件为p->next，而非是p非空，坑
            while (p->next != nullptr) {
                if (p == p->next->left){ // 右子树为空，且p是上一级的左，输出
                    return p->next;
                } else { // 右子树为空，且p是上一级的右，迭代
                    p = p->next;
                }
            }
        }
       
        // 最终跳槽循环只可能是，一直是右子树往上迭代，直到顶点
        return nullptr;
    }

    // 测试函数
    // 输入先序序列，构建一个二叉树，获取层次遍历结果
    // 输出每个节点的下一个中序遍历节点
    void test(std::vector<int>& vec) {
        struct timeval start, end;
        TreeLinkNode* root = TreeLinkNode_creatFromFrontOrder(vec);
        TreeLinkNode* result = nullptr;
        std::vector<TreeLinkNode*> all_node = TreeLinkNode_getAllNode(root);

        printf("=====\n");
        for (auto & node : all_node) {
            gettimeofday(&start, nullptr);
            result = this->GetNext(node);
            gettimeofday(&end, nullptr);
            int next_node = (result == nullptr ? -1 : result->val);
            int father_node = (node->next == nullptr ? -1 : node->next->val);
            printf("curr-node: %2d, father-node: %2d, next-node: %2d, times(us): %ld\n", node->val, father_node, next_node, end.tv_usec- start.tv_usec);
        }
    }
};

int main(int argc, char* argv[])
{
    std::vector<int> vec = {1, 2, 4, 8, -1, -1, 9, -1, -1, 5, 10, -1, -1, 11, -1, -1, 3, 6, -1, -1, 7, -1, -1};

    Solution s;
    s.test(vec);

    return 0;
}