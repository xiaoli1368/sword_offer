#include <iostream>
#include <vector>

class Solution {
public:
    // 两个数组，一次循环
    // 这里必须是静态的才可以被外部引用为函数指针
    // 因为如果不是静态的，那么就没有地址？（存疑）
    void static reOrderArray(std::vector<int>& array) {
        std::vector<int> tmp1, tmp2;
        for (auto i : array) {
            if (i % 2 == 1) {
                tmp1.push_back(i);
            } else {
                tmp2.push_back(i);
            }
        }
        tmp1.insert(tmp1.end(), tmp2.begin(), tmp2.end());
        array = tmp1;
    }

    // 一个数组，两次遍历
    void static reOrderArray2(std::vector<int>& array) {
        std::vector<int> tmp;
        for (auto i : array) {
            if (i % 2 == 1) {
                tmp.push_back(i);
            }
        }
        for (auto i : array) {
            if (i % 2 == 0) {
                tmp.push_back(i);
            }
        }
        array = tmp;
    }

    // 二重循环，冒泡方式，将偶数放到最右边
    void static reOrderArray3(std::vector<int>& array) {
        int len = array.size();
        for (int i = 0; i < len; i++) {
            for (int j = 0; j < len; j++) {
                if (array[j] % 2 == 0 && array[j+1] % 2 == 1) {
                    int tmp = array[j];
                    array[j] = array[j+1];
                    array[j+1] = tmp;
                }
            }
        }
    }

    // 二重循环，冒泡方式，部分优化
    void static reOrderArray4(std::vector<int>& array) {
        for (int i = array.size() - 1; i > 0; i--) {
            for (int j = 0; j < i; j++) {
                if (array[j] % 2 == 0 && array[j+1] % 2 == 1) {
                    int tmp = array[j];
                    array[j] = array[j+1];
                    array[j+1] = tmp;
                }
            }
        }
    }
    
    // 输入要打印的数据，以及函数指针数组
    // 调用每个函数指针完成打印
    void print_vector(std::vector<int> array, std::vector<void(*)(std::vector<int>&)> ptr) {
        for (auto func : ptr) {
            std::vector<int> tmp = array; 
            func(tmp);
            for (auto i : tmp) {
                std::cout << i << " ";
            }
            std::cout << std::endl;
        }
    }
};

int main(int argc, char* argv[])
{
    Solution s;
    std::vector<int> array = {1, 3, 8, 2, 4, 5, 9, 7, 6};

    // 定义函数指针数组
    std::vector<void(*)(std::vector<int>&)> ptr;
    ptr.push_back(s.reOrderArray);
    ptr.push_back(s.reOrderArray2);
    ptr.push_back(s.reOrderArray3);
    ptr.push_back(s.reOrderArray4);
    s.print_vector(array, ptr);
    
    return 0;
}