#include <iostream>
#include <vector>
#include <stdio.h>
#include <sys/time.h>

class Solution {
public:
    // 使用除法的思路，复杂度也是O(2n)
    // 然而题目要求不能使用除法
    std::vector<int> multiply1(const std::vector<int>& A) {
        if (A.empty()) {
            return A;
        }

        long tmp = 1;
        for (auto i : A) {
            tmp *= i;
        }

        std::vector<int> result;
        for (auto i : A) {
            result.push_back(tmp / i);
        }
        return result;
    }

    // 其它思路，两层遍历，每次使用1修改元素，复杂度O(n^2)
    // 注意到A是const，所以只能额外使用空间（这种方法低效）
    std::vector<int> multiply2(const std::vector<int>& A) {
        if (A.empty()) {
            return A;
        }

        std::vector<int> result;
        std::vector<int> data(A.begin(), A.end());

        for (int i = 0 ; i < data.size(); i++) {
            long tmp = 1;
            int curr = data[i];
            data[i] = 1;
            for (auto j : data) {
                tmp *= j;
            }
            data[i] = curr;
            result.push_back(tmp);
        }

        return result;
    }

    // 常规思路，左右延伸计算，复杂度O(n*(n-1))
    // 第一次的解法
    std::vector<int> multiply3(const std::vector<int>& A) {
        std::vector<int> ret;
        if (A.empty()) {
            return ret;
        }
        
        for (int i = 0; i < A.size(); i++) {
            int tmp = 1;
            for (int j = 0; j < A.size(); j++) {
                if (j != i) {
                    tmp *= A[j]; 
                }
            }
            ret.push_back(tmp);
        }
        
        return ret;
    }

    // 高效思路，两次遍历，区分左右侧元素构成的乘积数组
    std::vector<int> multiply(const std::vector<int>& A) {
        if (A.empty()) {
            return A;
        }
        
        int tmp = 1;
        std::vector<int> ret;
        for (auto i : A) {
            ret.push_back(tmp);
            tmp *= i;
        }
        
        tmp = 1;
        for (int i = A.size() - 1; i >= 0; i--) {
            ret[i] *= tmp;
            tmp *= A[i];
        }
        
        return ret;
    }

    // 打印一维向量
    void print_1d_vec(std::vector<int>& vec) {
        if (vec.empty()) {
            return;
        }

        for (auto i : vec) {
            std::cout << i << " ";
        }
    }

    // 测试函数
    void test(std::vector<int>& vec) {
        std::vector<int> result;
        struct timeval start, end;
        for (auto func : this->func_vec_) {
            gettimeofday(&start, 0);
            result = (this->*func)(vec);
            gettimeofday(&end, 0);
            printf("result: ");
            this->print_1d_vec(result);
            printf(", time(us): %ld\n", end.tv_usec - start.tv_usec);
        }
    }

private:
    typedef std::vector<int> (Solution::*func_ptr)(const std::vector<int>&);
    std::vector<func_ptr> func_vec_ = {&Solution::multiply1,
                                       &Solution::multiply2,
                                       &Solution::multiply3,
                                       &Solution::multiply};
};

int main(int argc, char* argv[])
{
    std::vector<int> vec = {1, 2, 3, 4 ,5};
    std::vector<int> vec2 = {8, 3, 5, 2, 2, 4, 1, 6, 7};

    Solution s;
    s.test(vec);
    std::cout << "=====" << std::endl;
    s.test(vec2);

    return 0;
}