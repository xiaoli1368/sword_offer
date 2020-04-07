#include <iostream>
#include <vector>

class Solution {
public:
    // 递归层次的函数调用
    bool VerifyBST(std::vector<int>&seq, int first, int last) {
        if (first >= last) {
            return true;
        }

        // 寻找左右子树的区分点
        int rootVal = seq[last];
        int cutIndex = first;
        while (cutIndex < last && seq[cutIndex] < rootVal) {
            cutIndex++;
        }

        // 检测右子树是否满足都大于根节点的值
        for (int i = cutIndex; i < last; i++) {
            if (seq[i] < rootVal) {
                return false;
            }
        }

        // 当前层次已经满足，递归检测下一层次
        return VerifyBST(seq, first, cutIndex - 1) && VerifyBST(seq, cutIndex, last - 1);
    }

    // 顶层的函数调用
    bool VerifySequenceOfBST(std::vector<int>& seq) {
        if (seq.empty()) {
            return false;
        }

        return VerifyBST(seq, 0, seq.size() - 1);
    }
};

int main(int argc, char* argv[])
{
    Solution s;
    std::vector<int> seq = {2, 9, 5, 16, 17, 15, 19, 12};
    std::vector<int> seq2 = {4, 5, 2, 6, 7, 3, 1};

    std::cout << s.VerifySequenceOfBST(seq) << std::endl;
    std::cout << s.VerifySequenceOfBST(seq2) << std::endl;

    return 0;
}