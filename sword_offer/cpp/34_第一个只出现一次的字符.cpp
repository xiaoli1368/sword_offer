#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <stdio.h>
#include <sys/time.h>

class Solution {
public:
    // 暴力枚举
    // 对每个字符，检测全部位置判断是否是否存在相同
    // 时间复杂度O(n^2)，空间复杂度O(1)
    int FirstNotRepeatingChar1(std::string str) {
        if (str.empty()) {
            return -1;
        }

        for (int i = 0; i < str.size(); i++) {
            bool sign = true;
            for (int j = 0; j < str.size(); j++) {
                if (i != j && str[i] == str[j]) {
                    sign = false;
                    break;
                }
            }
            if (sign) {
                return i;
            }
        }
        return -1;
    }

    // map法，额外使用了vec来记录顺序（其实是多此一举）
    // 时间复杂度O(2n)，空间复杂度O(2n)
    int FirstNotRepeatingChar2(std::string str) {
        if (str.empty()) {
            return -1;
        }

        std::map<char, int> map;               // 记录字母和出现的次数
        std::vector<std::pair<char, int>> vec; // 记录字母顺序以及索引

        for (int i = 0; i < str.size(); i++) {
            if (map.count(str[i]) == 0) {
                map.insert(std::pair<char, int>(str[i], 1));
                vec.push_back(std::pair<char, int>(str[i], i));
            } else {
                map[str[i]]++;
            }
        }

        for (auto i : vec) {
            if (map[i.first] == 1) {
                return i.second;
            }
        }
        return -1;
    }

    // map法，采用原始的str顺序
    // 时间复杂度O(2n)，空间复杂度O(n)
    int FirstNotRepeatingChar3(std::string str) {
        if (str.empty()) {
            return -1;
        }

        std::map<char, int> map;

        for (auto i : str) {
            if (map.count(i) == 0) { // 这种添加方式可以优化
                map.insert(std::pair<char, int>(i, 1));
            } else {
                map[i]++;
            }
        }

        for (int i = 0; i < str.size(); i++) {
            if (map[str[i]] == 1) {
                return i;
            }
        }
        return -1;
    }

    // map法，借助str顺序
    // 上一种方法的简单优化
    // map默认初始化value为0，并且对于不存在的key，map[key]索引不会执行
    int FirstNotRepeatingChar4(std::string str) {
        if (str.empty()) {
            return -1;
        }

        std::map<char, int> map;
        for (auto i : str) {
            map[i]++;
        }

        // 注意返回索引
        for (int i = 0; i < str.size(); i++) {
            if (map[str[i]] == 1) {
                return i;
            }
        }
        return -1;
    }

    // 利用stl的高效解法
    // find(): 返回第一次出现的索引
    // rfind(): 返回最后一次出现的索引
    int FirstNotRepeatingChar5(std::string str) {
        if (str.empty()) {
            return -1;
        }
        for (int i = 0; i < str.size(); i++) {
            if (str.find(str[i]) == str.rfind(str[i])) {
                return i;
            }
        }
        return -1;
    }

    // hash法，类似map，区别在于自行定义256维度的数组，以覆盖ascii
    // str[i] 实现了一个散列函数，取出字母字符并且使用了ascii码值
    // 时间复杂度O(2n)，空间复杂度O(1)，随n的变化，空间消耗都是256
    int FirstNotRepeatingChar6(std::string str) {
        if (str.empty()) {
            return -1;
        }

        unsigned char hash[256] = {0};
        for (auto i : str) {
            hash[i]++;
        }
        for (int i = 0; i < str.size(); i++) {
            if (hash[str[i]] == 1) {
                return i;
            }
        }
        return -1;
    }

    // 测试函数
    void test(std::string& str) {
        int result = 0;
        struct timeval start, end;
        printf("=====\n");
        for (auto func : this->func_vec_) {
            gettimeofday(&start, nullptr);
            result = (this->*func)(str);
            gettimeofday(&end, nullptr);
            if (result >= 0) {
                printf("time(us): %3ld, result: %c\n", end.tv_usec - start.tv_usec, str[result]);
            } else {
                printf("time(us): %3ld, result: no!\n", end.tv_usec - start.tv_usec);
            }
        }
    }

private:
    typedef int (Solution::*func_ptr)(std::string);
    std::vector<func_ptr> func_vec_ = {&Solution::FirstNotRepeatingChar1,
                                       &Solution::FirstNotRepeatingChar2,
                                       &Solution::FirstNotRepeatingChar3,
                                       &Solution::FirstNotRepeatingChar4,
                                       &Solution::FirstNotRepeatingChar5,
                                       &Solution::FirstNotRepeatingChar6};
};

int main(int argc, char* argv[])
{
    std::string str1 = "";
    std::string str2 = "aabbcc";
    std::string str3 = "abcthka";
    std::string str4 = "leetcode";
    std::string str5 = "aslkjflasflaskdflm;eoion3g";
    std::string str6(1000, 'a');

    Solution s;
    s.test(str1);
    s.test(str2);
    s.test(str3);
    s.test(str4);
    s.test(str5);
    s.test(str6);

    return 0;
}
