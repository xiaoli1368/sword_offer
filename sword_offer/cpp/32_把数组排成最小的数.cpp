#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <sys/time.h>

class Solution {
public:
    // 暴力枚举
    // 全排列字符串遍历
    std::string PrintMinNumber1(std::vector<int> numbers) {
        if (numbers.empty()) {
            return "";
        }

        std::string curr;
        std::string ret = vec2str(numbers);
        // 使用stl生成全排列，注意会跳过初始排列，所以ret要初始化
        while (std::next_permutation(numbers.begin(), numbers.end())) {
            curr = vec2str(numbers);
            if (ret > curr) {
                ret = curr;
            }
        }

        return ret;
    }

    // 第一次的方式：没有额外函数
    std::string PrintMinNumber2(std::vector<int> numbers) {
        if (numbers.empty()) {
            return "";
        }

        int length = numbers.size();
        for (int i = 0; i < length - 1; i++) {
            for (int j = i + 1; j < length; j++) {
                std::string a = std::to_string(numbers[i]);
                std::string b = std::to_string(numbers[j]);
                if (a + b > b + a) {
                    int tmp = numbers[i];
                    numbers[i] = numbers[j];
                    numbers[j] = tmp;
                }
            }
        }

        std::string result;
        for (auto i : numbers) {
            result += std::to_string(i);
        }
        return result;
    }

    // 高效方式：冒泡排序修改版
    std::string PrintMinNumber3(std::vector<int> numbers) {
        if (numbers.empty()) {
            return "";
        }

        for (int i = numbers.size() - 1; i >= 1; i--) {
            for (int j = 0; j < i; j++) {
                if_swap(&numbers[j], &numbers[j + 1]);
            }
        }

        return vec2str(numbers);
    }

    // 高效方式：stl排序
    std::string PrintMinNumber4(std::vector<int> numbers) {
        if (numbers.empty()) {
            return "";
        }

        sort(numbers.begin(), numbers.end(), this->my_cmp);
        return vec2str(numbers);
    }

    // 高效方式：快速排序（待补充）
    std::string PrintMinNumber(std::vector<int> numbers) {}

    // ========== 工具函数 ==========
    // 将vec转换为string
    std::string vec2str(std::vector<int>& vec) {
        if (vec.empty()) {
            return "";
        }

        std::string tmp = "";
        for (auto i : vec) {
            tmp += std::to_string(i);
        }
        return tmp;
    }

    // 按自定义的比较函数来交换数组中两个数的值
    void if_swap(int* a, int* b) {
        std::string aa = std::to_string(*a);
        std::string bb = std::to_string(*b);
        if (aa + bb > bb+ aa) {
            int tmp = *a;
            *a = *b;
            *b = tmp;
        }
    }

    // 自定义的比较函数
    static bool my_cmp(int a, int b) {
        std::string aa = std::to_string(a);
        std::string bb = std::to_string(b);
        return a + b < b + a;
    }

    // 测试函数
    void test(std::vector<int>& numbers) {
        std::string result;
        struct timeval start, end;
        for (auto func: this->func_vec_) {
            gettimeofday(&start, 0);
            result = (this->*func)(numbers);
            gettimeofday(&end, 0);
            std::cout << "result: " << result << ", time(us): " << end.tv_usec - start.tv_usec << std::endl; 
        }
    }

private:
    typedef std::string (Solution::*func_ptr)(std::vector<int>);
    std::vector<func_ptr> func_vec_ = {&Solution::PrintMinNumber1,
                                       &Solution::PrintMinNumber2,
                                       &Solution::PrintMinNumber3,
                                       &Solution::PrintMinNumber4};
};

int main(int argc, char* argv[])
{
    std::vector<int> numbers = {3, 32, 321};
    std::vector<int> numbers2 = {13, 21, 4, 41, 323, 3, 210, 4145};

    Solution s;
    s.test(numbers);
    std::cout << "=====" << std::endl;
    s.test(numbers2);

    return 0;
}