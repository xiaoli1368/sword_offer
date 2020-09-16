#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <stdio.h>
#include <sys/time.h>

class Solution {
public:
    std::vector<std::string> ret;

    // ===== 外部接口 =====

    // 1. 使用stl求解（有序，无重复）
    std::vector<std::string> Permutation1(std::string str) {
        if (str.empty()) {
            return ret;
        }
        
        sort(str.begin(), str.end());

        do {
            ret.push_back(str);
        } while (std::next_permutation(str.begin(), str.end()));

        return ret;
    }

    // 2. 递归传递引用，set,sort（有序，无重复）
    std::vector<std::string> Permutation2(std::string str) {
        if (str.empty()) {
            return ret;
        }
        
        // 无序版本
        perm0(str, 0);

        // 利用set对vec去重复
        std::set<std::string> set(ret.begin(), ret.end());
        ret.assign(set.begin(), set.end());

        // 利用stl对vec排序
        sort(ret.begin(), ret.end());
        return ret;
    }

    // 3. 递归传递引用，内部使用stl排序（有序，无重复）
    std::vector<std::string> Permutation3(std::string str) {
        if (str.empty()) {
            return ret;
        }
        
        sort(str.begin(), str.end());
        perm1(str, 0); // 调用perm-method-1
        return ret;
    }

    // 4. 递归传递值，不使用stl排序，循环替换实现（有序，无重复）
    std::vector<std::string> Permutation4(std::string str) {
        if (str.empty()) {
            return ret;
        }
        
        sort(str.begin(), str.end());
        perm2(str, 0); // 调用perm-method-2
        return ret;
    }

    // ===== 递归函数 =====

    // 无序版本
    void perm0(std::string& str, int start) {
        if (start == str.size() - 1) {
            ret.push_back(str);
            return;
        }

        for (int i = start; i < str.size(); i++) {
            swap(str[i], str[start]);
            perm0(str, start + 1);
            swap(str[i], str[start]);
        }
        return;
    }


    // 说明：
    //     [1] 递归求解，将当前的全排列添加到ret
    //     [2] 输入str引用，起始索引
    // 存在的问题：
    //     [1] 每次递归调用sort排序，使用引用
    //     [2] 如果不要求有序，可以省去sort()步骤
    //     [3] 需要调用额外的函数，检测重复性
    void perm1(std::string& str, int start) {
        if (start == str.size() - 1) {
            ret.push_back(str);
            return;
        }
        
        // 注意在传递引用时内部排序，后打乱str，使用上一层swap无法恢复str，导致出现重复
        // 所以这里保存排序之前的str
        std::string oriStr = str;
        sort(str.begin() + start, str.end());
        
        // 依次交换，并进行下一次的迭代
        for (int i = start; i < str.size(); i++) {
            if (i == start || (str[start] != str[i] && !ifHasSame(str, start, i))) {
                swap(str[i], str[start]); // 交换
                perm1(str, start + 1);    // 递归
                swap(str[i], str[start]); // 交换回来
            }
        }

        str = oriStr; // 保证排序不影响上一层递归恢复
        return;
    }

    // ===== 其它方式：优化版 =====
    // 改动：
    //     [1] 递归内部传值，而非引用
    //     [2] 去除了不必要的形式参数
    //     [3] 不使用sort，借助循环交换来实现有序
    // 缺点：
    //     [1] 这种方式传递了很多次形式参数
    //     [2] 不需要额外的防重复逻辑
    void perm2(std::string str, int start) {
        if (start == str.size() - 1) {
            ret.push_back(str);
            return;
        }
        
        // 依次交换，并进行下一次的迭代
        for (int i = start; i < str.size(); i++) {
            // 跳过重复
            if (i == start || str[start] != str[i]) {
                swap(str[i], str[start]); // 交换
                perm2(str, start + 1); // 递归
            }
        }
        return;
    }

    // ===== 工具函数 =====
    // 交换string中两个字符的值
    void swap(char& a, char& b) {
        char tmp = a;
        a = b;
        b = tmp;
    }

    // 判断[start, i]之间是否有与i相同的元素
    bool ifHasSame(std::string& str, int start, int i) {
        for (int k = start + 1; k < i; k++) {
            if (str[k] == str[i]) {
                return true;
            }
        }
        return false;
    }

    // 打印结果，仅显示结果个数不超过24的情况
    void printf_vecStr(std::vector<std::string>& vec) {
        if (vec.size() > 24) {
            printf("%ld numbers, too many to display!\n", vec.size());
            return;
        }

        for (auto i : vec) {
            std::cout << i << ", ";
        }
        std::cout << std::endl;
        return;
    }

    // 测试函数
    void test(std::string& str) {
        std::vector<std::string> result;
        struct timeval start, end;
        printf("=====\n");
        for (auto func : this->func_vec_) {
            this->ret.clear();
            gettimeofday(&start, nullptr);
            result = (this->*func)(str);
            gettimeofday(&end, nullptr);
            printf("time(us): %4ld, result: ", end.tv_usec - start.tv_usec);
            this->printf_vecStr(result);
        }
    }

private:
    typedef std::vector<std::string> (Solution::*func_ptr)(std::string);
    std::vector<func_ptr> func_vec_ = {&Solution::Permutation1,
                                       &Solution::Permutation2,
                                       &Solution::Permutation3,
                                       &Solution::Permutation4};
};

int main(int argc, char* argv[])
{
    std::string str1 = "cab";
    std::string str2 = "abac";
    std::string str3 = "cbba";
    std::string str4 = "sghi";
    std::string str5 = "iugoa";
    std::string str6 = "sadjbg";

    Solution s;
    s.test(str1);
    s.test(str2);
    s.test(str3);
    s.test(str4);
    s.test(str5); // 结果个数：5! = 120
    s.test(str6); // 结果个数：6! = 720

    return 0;
}