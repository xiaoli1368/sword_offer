#include <stdio.h>
#include <queue>

typedef struct Node {
    int val;
    Node* left;
    Node* right;
    Node* next;
    Node(int val, Node* left, Node* right, Node* next) : 
        val(val), left{left}, right(right), next(next) {}
} Node;

class Solution {
public:
    // 层次遍历法
    Node* connect(Node* root) {
        if (root == nullptr) {
            return root;
        }
        std::queue<Node*> queue;
        queue.push(root);
        while (!queue.empty()) {
            int size = queue.size();
            for (int i = 0; i < size; i++) {
                Node* node = queue.front();
                queue.pop();
                if (!queue.empty() && i != size - 1) {
                    node->next = queue.front();
                }
                if (node->left) {
                    queue.push(node->left);
                }
                if (node->right) {
                    queue.push(node->right);
                }
            }
        }
        return root;
    }

    // 带下一个节点的先序遍历
    void dfs(Node* root, Node* nextNode) {
        if (root == nullptr) {
            return;
        }
        root->next = nextNode;
        dfs(root->left, root->right);
        dfs(root->right, nextNode ? nextNode->left : nullptr);
        return;
    }

    // 直接先序遍历
    Node* connect2(Node* root) {
        dfs(root, nullptr);
        return root;
    }
};

int main(int argc, char* argv[])
{
    return 0;
}