#include <iostream>
#include <string>
#include <vector>
#include <map>

class Solution {
public:
    // 暴力枚举，复杂度很大
    int FirstNotRepeatingChar(std::string str) {
        int length = str.size();
        if (length <= 1) {
            return 0;
        }

        for (int i = 0; i < length; i++) {
            bool sign = true;
            for (int j = 0; j < length; j++) {
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

    // map法，额外使用了vec来记录顺序
    int FirstNotRepeatingChar2(std::string str) {
        std::map<char, int> map; // 记录字母和出现的次数
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

    // 借助map，不使用额外的vec来记录顺序，采用原始的str顺序
    int FirstNotRepeatingChar3(std::string str) {
        std::map<char, int> map;

        for (auto i : str) {
            if (map.count(i) == 0) {
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

    // 上一种方法的简单优化
    // map默认初始化value为0
    // 对于不存在的key，map[key]索引不会执行
    int FirstNotRepeatingChar4(std::string str) {
        std::map<char, int> map;

        for (int i = 0; i < str.size(); i++) {
            map[str[i]]++;
        }

        for (int i = 0; i < str.size(); i++) {
            if (map[str[i]] == 1) {
                return i;
            }
        }
        return -1;
    }

    // 利用stl的高效解法
    int FirstNotRepeatingChar5(std::string str) {
        if (str.empty()) {
            return -1;
        }
        for (size_t i = 0; i < str.size(); i++) {
            if (str.find(str[i]) == str.rfind(str[i])) {
                return i;
            }
        }
    }

    // 采用数组构建hash
    // 核心在于考虑到大小写字母的ascii小于一个字节，因此最大也不超过256
    // 所以利用256数组可以全部覆盖
    // str[i] 实现了一个散列函数，取出字母字符并且使用了ascii码值
    int FirstNotRepeatingChar6(std::string str) {
        if (str.empty()) {
            return -1;
        }

        unsigned int hashTime[256] = {0};
        for (int i = 0; i < str.size(); i++) {
            hashTime[str[i]]++;
        }
        for (int i = 0; i < str.size(); i++) {
            if (hashTime[str[i]] == 1) {
                return i;
            }
        }
        return -1;
    }
 
};

int main(int argc, char* argv[])
{
    Solution s;
    std::string input = "google";

    std::cout << s.FirstNotRepeatingChar(input) << std::endl;
    std::cout << s.FirstNotRepeatingChar2(input) << std::endl;
    std::cout << s.FirstNotRepeatingChar3(input) << std::endl;
    std::cout << s.FirstNotRepeatingChar4(input) << std::endl;
    std::cout << s.FirstNotRepeatingChar5(input) << std::endl;
    return 0;
}
