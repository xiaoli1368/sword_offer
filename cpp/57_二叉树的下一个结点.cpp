/*
struct TreeLinkNode {
    int val;
    struct TreeLinkNode *left;
    struct TreeLinkNode *right;
    struct TreeLinkNode *next;
    TreeLinkNode(int x) :val(x), left(NULL), right(NULL), next(NULL) {
        
    }
};
*/
class Solution {
public:
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
};