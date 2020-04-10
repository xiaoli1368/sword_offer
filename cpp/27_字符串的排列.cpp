#include <iostream>
#include <vector>
#include <algorithm>

class Solution {
public:
    std::vector<std::string> ret;
    
    void swap(char& a, char& b) {
        char tmp = a;
        a = b;
        b = tmp;
    }
    
    // 采用递归，输入str，每个函数实现的功能是将当前的全排列可能添加到ret中去
    void perm(std::string str, int low, int high) {
        if (low == high) {
            ret.push_back(str);
            return;
        }
        
        sort(str.begin() + low, str.end());
        
        // 依次交换，并进行下一次的迭代
        for (int i = low; i <= high; i++) {
            // 跳过重复
            if (i == low || str[low] != str[i]) {
                swap(str[i], str[low]); // 交换
                perm(str, low + 1, high); // 递归
                //swap(str[i], str[low]); // 交换回来
            }
        }
        return;
    }
    
    std::vector<std::string> Permutation(std::string str) {
        if (str.empty()) {
            return ret;
        }
        
        sort(str.begin(), str.end());
        perm(str, 0, str.size() - 1);
        return ret;
    }
};

int main(int argc, char* argv[])
{
    Solution s;
    std::string ss = "aabc";
    std::vector<std::string> result = s.Permutation(ss);

    for (auto i : result) {
        std::cout << i << std::endl;
    }

    return 0;
}