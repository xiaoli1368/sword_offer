#include <iostream>
#include <vector>
#include <stack>
#include <stdio.h>
#include <sys/time.h>

class Solution {
public:
    // 1. 递归法
    bool VerifySequenceOfBST(std::vector<int>& seq) {
        if (seq.empty()) {
            return false;
        }

        return VerifyBST(seq, 0, seq.size() - 1);
    }

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

    // 2. 单调栈
    bool VerifySequenceOfBST2(std::vector<int>& seq) {
        if (seq.empty()) {
            return false;
        }

        std::stack<int> q; // 单调栈，用来存储根和右节点
        int root = 0x7fffffff;

        for (int i = seq.size() - 1; i >= 0; i--) {
            if (seq[i] > root) {
                return false;
            }
            while (!q.empty() && q.top() > seq[i]) {
                root = q.top();
                q.pop();
            }
            q.push(seq[i]);
        }

        return true;
    }

    // 测试函数
    void test(std::vector<int>& vec) {
        bool result = false;
        struct timeval start, end;
        printf("=====\n");
        for (auto & func : this->func_vec_) {
            gettimeofday(&start, nullptr);
            result = (this->*func)(vec);
            gettimeofday(&end, nullptr);
            printf("result: %d, times(us): %ld\n", result, end.tv_usec - start.tv_usec);
        }
    }

private:
    typedef bool (Solution::*func_ptr)(std::vector<int>&);
    std::vector<func_ptr> func_vec_ = {&Solution::VerifySequenceOfBST,
                                       &Solution::VerifySequenceOfBST2};
};

int main(int argc, char* argv[])
{
    std::vector<int> seq = {2, 9, 5, 16, 17, 15, 19, 12};
    std::vector<int> seq2 = {4, 5, 2, 6, 7, 3, 1};

    Solution s;
    s.test(seq);
    s.test(seq2);

    return 0;
}