#include <iostream>
#include <vector>
#include <map>
#include <deque>
#include <algorithm>
#include <stdio.h>
#include <sys/time.h>

class Solution {
public:
    // 第一次的解法，使用stl直接求最大值
    std::vector<int> maxInWindows1(const std::vector<int>& num, unsigned int size) {
        std::vector<int> ret;
        int length = num.size();
        
        if (size > length || size == 0) {
            return ret;
        }
        
        for (int i = 0; i <= length - size; i++) {
            ret.push_back(*std::max_element(num.begin() + i, num.begin() + i + size));
        }
        
        return ret;
    }

    // stl优化版，使用了临时变量
    std::vector<int> maxInWindows2(const std::vector<int>& num, unsigned int size) {
        if (size <= 0 || size > num.size()) {
            return std::vector<int>{};
        }

        int lastMax = num[0]; 
        int popValue = num[0];
        std::vector<int> ret;

        for (int i = 0; i <= num.size() - size; i++) {
            if (lastMax == popValue) { // 被丢弃则更新
                lastMax = *std::max_element(num.begin() + i, num.begin() + i + size);
            } else if (lastMax < num[i + size - 1]) { // 比新加的小则更新
                lastMax = num[i + size - 1];
            }
            ret.push_back(lastMax);
            popValue = num[i];
        }

        return ret;
    }

    // 使用map
    std::vector<int> maxInWindows3(const std::vector<int>& num, unsigned int size) {
        if (size <= 0 || size > num.size()) {
            return std::vector<int>{};
        }

        std::vector<int> ret;
        std::map<int, int> map;

        for (int i = 0; i < num.size(); i++) {
            // 加入当前值
            ++map[num[i]];

            // 过期则删除
            if (i >= size && 0 == --map[num[i - size]]) {
                map.erase(num[i - size]);
            }

            // 获取最大值
            if (i >= size - 1) {
                ret.push_back(map.rbegin()->first);
            }
        }

        return ret;
    }

    // 使用最大堆
    std::vector<int> maxInWindows4(const std::vector<int>& num, unsigned int size) {
        if (size <= 0 || size > num.size()) {
            return std::vector<int>{};
        }

        std::vector<int> maxHeap(num.begin(), num.begin() + size);
        std::make_heap(maxHeap.begin(), maxHeap.end());
        std::vector<int> ret = {maxHeap[0]};

        for (int i = size, j = 0; i < num.size(); i++, j++) {
            // 移除元素
            std::vector<int>::iterator iter = std::find(maxHeap.begin(), maxHeap.end(), num[j]);
            maxHeap.erase(iter);

            // 加入新元素
            maxHeap.push_back(num[i]);
            std::make_heap(maxHeap.begin(), maxHeap.end());

            // 获取当前窗口最大值
            ret.push_back(maxHeap.front());
        }

        return ret;
    }

    // 使用deque
    // 双端队列，存储长度最大为size
    // 存储的是降序的序列索引，表示当前最大值，次大值，...
    std::vector<int> maxInWindows5(const std::vector<int>& num, unsigned int size) {
        if (size <= 0 || size > num.size()) {
            return std::vector<int>{};
        }

        std::vector<int> ret;
        std::deque<int> deq;

        for (int i = 0; i < num.size(); i++) {
            // 清空之前比新加入的num[i]小的元素
            // 保证num[i]为最大或者次大...
            while (!deq.empty() && num[i] > num[deq.back()]) {
                deq.pop_back();
            }

            // 从前pop元素，保证滑窗长度
            if ((!deq.empty()) && deq.front() < (i - int(size) + 1)) {
                // 这里是个坑阿，(int) - (unsigned int)结果就错了
                deq.pop_front();
            }

            // 引入当前值
            deq.push_back(i);

            // 从头部提取有效的最大值
            if (i >= size - 1) {
                ret.push_back(num[deq.front()]);
            }

            // 用于测试
            // this->print_1d_deq(deq, num);
        }

        return ret;
    }

    // 打印一维向量
    void print_1d_vec(const std::vector<int>& num) {
        for (auto i : num) {
            std::cout << i << " ";
        }
        std::cout << std::endl;
    }
    
    // 打印一维队列
    void print_1d_deq(const std::deque<int>& deq, const std::vector<int>& num) {
        for (auto i : deq) {
            std::cout << num[i] << " ";
        }
        std::cout << std::endl;
    }

    // 测试函数
    void test(const std::vector<int>& num, unsigned int size) {
        std::vector<int> result;
        struct timeval start, end;
        printf("=====\n");
        for (auto func : this->func_vec_) {
            gettimeofday(&start, nullptr);
            result = (this->*func)(num, size);
            gettimeofday(&end, nullptr);
            printf("time(us): %2ld, result: ", end.tv_usec - start.tv_usec);
            this->print_1d_vec(result);
        }
    }

private:
    typedef std::vector<int> (Solution::*func_ptr)(const std::vector<int>&, unsigned int);
    std::vector<func_ptr> func_vec_ = {&Solution::maxInWindows1,
                                       &Solution::maxInWindows2,
                                       &Solution::maxInWindows3,
                                       &Solution::maxInWindows4,
                                       &Solution::maxInWindows5};
    
};

int main(int argc, char* argv[])
{
    std::vector<int> num = {2, 3, 4, 2, 6, 2, 5, 1};
    std::vector<int> num2 = {16, 14, 12, 10, 8, 6, 4};

    Solution s;
    s.test(num, 3);
    s.test(num2, 5);

    return 0;
}