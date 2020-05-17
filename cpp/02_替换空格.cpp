#include <string>
#include <stdio.h>
#include <string.h>
#include <sys/time.h>

class Solution {
public:
    // 基于c字符数组，扩容搬移法
    void replaceSpace(char *str, int length) {
        if (str == nullptr || length <= 0) {
            return;
        }

        // 获取空格的长度
        int count = 0;
        for (int i = 0; i < length; i++) {
            if (str[i] == ' ') {
                count++;
            }
        }

        // 从尾部开始搬移
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

    // 基于c++中字符串，借助额外空间
    void replaceSpace(std::string& str) {
        if (str.empty()) {
            return;
        }

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

    // 测试函数
    void test(char* str1, int length, std::string& str2) {
        struct timeval start, end;
        printf("=====\n");

        gettimeofday(&start, nullptr);
        this->replaceSpace(str1, length);
        gettimeofday(&end, nullptr);
        printf("time(us): %ld, result: %s\n", end.tv_usec - start.tv_usec, str1);

        gettimeofday(&start, nullptr);
        this->replaceSpace(str2);
        gettimeofday(&end, nullptr);
        printf("time(us): %ld, result: %s\n", end.tv_usec - start.tv_usec, str2.c_str());
    }
};

int main(int argc, char* argv[])
{
    Solution s;

    char str1[100] = " A B ";
    std::string str2 = " A B ";
    s.test(str1, 5, str2);

    strcpy(str1, " 23sa  woj fpqfm qo jsa ");
    str2 = " 23sa  woj fpqfm qo jsa ";
    s.test(str1, str2.size(), str2);

    return 0;
}