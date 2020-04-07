#include <stdio.h>
#include <iostream>
#include <string>

class Solution {
public:
    void replaceSpace(char *str, int length) {
        int count = 0;
        for (int i = 0; i < length; i++) {
            if (str[i] == ' ') {
                count++;
            }
        }
        int j = length + 2 * count;
        str[j] = '\0';
        for (int i = length - 1; i >= 0; i--) {
            if (str[i] == ' ') {
                str[--j] = '0';
                str[--j] = '2';
                str[--j] = '%';
            } else {
                str[--j] = str[i];
            }
        }
    } 

    // c++形式
    // 借助额外空间
    void replaceSpace2(std::string& str) {
        std::string tmp = "";
        for (auto i : str) {
            if (i == ' ') {
                tmp += "%20";
            } else {
                tmp += i;
            }
        }
        str = tmp;
    }

    // c++形式
    // 减少额外空间的使用
    void replaceSpace3(std::string& str) {
        int length = str.length();
        for (int i = 0; i < length; i++) {
            if (str[i] == ' ') {
                str.append("  ");
            }
        }
        // 从后端开始搬移
        int j = str.length(); 
        for (int i = length - 1; i >= 0; i--) {
            if (str[i] == ' ') {
                str[--j] = '0';
                str[--j] = '2';
                str[--j] = '%';
            } else {
                str[--j] = str[i];
            }
        }
    }
};

int main(int argc, char* argv[])
{
    Solution s;
    char input_str[100]= " A B \0";
    s.replaceSpace(input_str, 5);
    printf("%s\n", input_str);

    // c++形式
    std::string in_str = " A B ";
    s.replaceSpace2(in_str);
    std::cout << in_str << std::endl;

    std::string in_str2 = " A B ";
    s.replaceSpace3(in_str2);
    std::cout << in_str2 << std::endl;

    return 0;
}