#include <iostream>
#include <string>
#include <queue>
#include <stdio.h>
#include <string.h>
#include <sys/time.h>

class Solution
{
private:
    typedef void (Solution::*func_ptr_Insert)(char);
    typedef char (Solution::*func_ptr_Appear)();
    std::vector<func_ptr_Insert> func_vec_Insert = {&Solution::Insert1, &Solution::Insert2};
    std::vector<func_ptr_Appear> func_vec_Appear = {&Solution::FirstAppearingOnce1, &Solution::FirstAppearingOnce2};

public:
    // ===== 使用hash + string =====
    std::string s; // 用来记录顺序
    unsigned char hash[256] = {0};
    
    // Insert one char from stringstream
    void Insert1(char ch) {
        s += ch;
        hash[ch]++;
    }
    
    // return the first appearence once char in current stringstream
    char FirstAppearingOnce1() {
        for (auto i : s) {
            if (hash[i] == 1) {
                return i;
            }
        }
        
        return '#';
    }

    // ===== 使用hash + queue =====
    std::queue<char> que;
    unsigned char hash2[256] = {0};
    
    // Insert one char from stringstream
    void Insert2(char ch) {
        hash2[ch]++;
        if (hash2[ch] == 1) {
            que.push(ch);
        }
    }
    
    // return the first appearence once char in current stringstream
    char FirstAppearingOnce2() {
        while (!que.empty()) {
            if (hash2[que.front()] == 1) {
                return que.front();
            } else {
                que.pop();
            }
        }

        return '#';
    }

    // 测试函数，内部调用
    // 输入测试字符串，insert函数指针，appear函数指针
    // 输出每次调用结果拼接而成的字符串
    std::string test_inner(std::string& str, func_ptr_Insert Insert, func_ptr_Appear Appear) {
        std::string tmp;
        for (auto i : str) {
            (this->*Insert)(i);
            tmp += (this->*Appear)();
        }
        return tmp;
    }

    // 测试函数，外部接口
    void test(std::string& str) {
        // 清空数据结构
        this->s.clear();
        this->que = std::queue<char>{};
        memset(this->hash, 0, 256 * sizeof(unsigned char));
        memset(this->hash2, 0, 256 * sizeof(unsigned char));

        // 临时变量
        std::string result;
        struct timeval start, end;

        printf("=====\n");
        for (int i = 0; i < 2; i++) {
            gettimeofday(&start, nullptr);
            result = this->test_inner(str, func_vec_Insert[i], func_vec_Appear[i]);
            gettimeofday(&end, nullptr);
            printf("time(us): %ld, result: %s\n", end.tv_usec - start.tv_usec, result.c_str());
        }
    }
};

int main(int argc, char* argv[])
{
    std::string str1 = "google";
    std::string str2 = "sasladfjslai65d13asfi2u";

    Solution s;
    s.test(str1);
    s.test(str2);

    return 0;
}