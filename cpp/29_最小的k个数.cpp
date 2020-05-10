#include <iostream>
#include <vector>
#include <algorithm>
#include <stdlib.h>
#include <stdio.h>
#include <sys/time.h>

class Solution {
public:
    // 利用stl进行排序，第一次的方式
    std::vector<int> GetLeastNumbers_Solution1(std::vector<int> input, int k) {
        if (input.empty() || k > input.size()) {
            return input;
        }

        std::vector<int> result;
        sort(input.begin(), input.end());
        result.insert(result.begin(), input.begin(), input.begin() + k);
        return result;
    }

    // 冒泡排序，每次将最小值放到前部
    std::vector<int> GetLeastNumbers_Solution2(std::vector<int> input, int k) {
        if (input.empty() || k > input.size()) {
            return input;
        }

        // 冒泡排序，找到前k个最小值
        for (int i = 0; i < k; i++) {
            for (int j = input.size() - 1; j > i; j--) {
                if (input[j - 1] > input[j]) {
                    int tmp = input[j - 1];
                    input[j - 1] = input[j];
                    input[j] = tmp;
                }
            }
        }

        std::vector<int> result;
        result.insert(result.begin(), input.begin(), input.begin() + k);
        return result;
    }

    // 基于快排partition方法
    std::vector<int> GetLeastNumbers_Solution3(std::vector<int> input, int k) {
        if (input.empty() || k > input.size()) {
            return input;
        }

        int start = 0;
        int end = input.size() - 1;
        int index = Partition(input, start, end);
        while (index != k - 1) {
            if (index > k - 1) {
                end = index - 1;
            } else {
                start = index + 1;
            }
            index = Partition(input, start, end);
        }
        // 此时将数组调整为[0, k-1]处的值都小于后面的，但是是无序的

        std::vector<int> result;
        result.insert(result.begin(), input.begin(), input.begin() + k);
        sort(result.begin(), result.end());
        return result;
    }
    
    // 利用空间换取时间的方式，然而随着初始tmp的增大存在巨大的时间浪费
    std::vector<int> GetLeastNumbers_Solution4(std::vector<int> input, int k) {
        if (input.empty() || k <= 0 || k > input.size()) {
            return std::vector<int>{};
        }

        std::vector<int> tmp(200000);
        for (auto i : input) {
            tmp[i]++;
        }

        int cnt = 0;
        std::vector<int> result;
        for (int i = 0; i < tmp.size(); i++) {
            while (tmp[i]-- > 0 && cnt < k) {
                cnt++;
                result.push_back(i);
            }
            if (cnt == k) {
                break;
            }
        }

        return result;
    }

    // 高效解法：使用最大堆实现（也被称为大根堆）
    // 最大堆定义：根结点的键值是所有堆结点键值中最大者，且每个结点的值都比其孩子的值大。
    // make_heap: 在容器范围内，就地建堆，保证最大值在所给范围的最前面，其他值的位置不确定
    // pop_heap: 将堆顶(所给范围的最前面)元素移动到所给范围的最后，并且将新的最大值置于所给范围的最前面
    // push_heap: 当已建堆的容器范围内有新的元素插入末尾后，应当调用push_heap将该元素插入堆中。
    std::vector<int> GetLeastNumbers_Solution(std::vector<int> input, int k) {
        if (input.empty() || k <= 0 || k > input.size()) {
            return std::vector<int>{}; // 返回一个空的vec
        }
        
        std::vector<int> result(input.begin(), input.begin() + k); // 直接迭代器初始化
        std::make_heap(result.begin(), result.end());

        for (int i = k; i < input.size(); i++) {
            if (input[i] < result[0]) {                       // 如果后续元素小于当前堆的最大值
                std::pop_heap(result.begin(), result.end());  // 把最大值放到最后，其它的形成heap
                result.pop_back();                            // 删除最后一个元素，也就是之前的最大值
                result.push_back(input[i]);                   // 插入新增的值到result
                std::push_heap(result.begin(), result.end()); // 重新生成堆
            }
        }
        std::sort_heap(result.begin(), result.end());
        
        return result;
    }

    // 快排的关键函数，分区
    // @input: 数组，起始索引
    // @otput: 一个索引，该索引左右元素分别小于大于该处的值
    int Partition(std::vector<int>& data, int start, int end) {
        if (data.empty() || start < 0 || end >= data.size()) {
            return -1;
        }

        // 随机选择一个元素为参考点（需要将其交换至end）
        srand(time(nullptr));
        int index = start + (rand() % (end - start + 1));
        Swap(&data[index], &data[end]);

        // 循环一遍完成分区，small左右分别为小于大于end处值
        int small = start - 1;
        for (index = start; index < end; index++) {
            if (data[index] < data[end]) {
                Swap(&data[index], &data[++small]);
            }
        }

        // 将end处的参考值交换回分界点位置
        Swap(&data[++small], &data[end]);
        return small;
    }

    // 交换两处指针的值
    void Swap(int* a, int* b) {
        int tmp = *a;
        *a = *b;
        *b = tmp;
    }

    // 打印一维向量
    void print_1d_vec(std::vector<int>& vec) {
        for (auto i : vec) {
            std::cout << i << " ";
        }
    }

    // 测试函数
    void test(std::vector<int>& input, int k) {
        std::vector<int> result;
        struct timeval start, end;
        for (auto func : this->func_vec_) {
            gettimeofday(&start, 0);
            result = (this->*func)(input, k);
            gettimeofday(&end, 0);
            printf("result: ");
            this->print_1d_vec(result);
            printf(", time(us): %ld\n", end.tv_usec - start.tv_usec);
        }
    }

private:
    typedef std::vector<int> (Solution::*func_ptr)(std::vector<int>, int);
    std::vector<func_ptr> func_vec_ = {&Solution::GetLeastNumbers_Solution1,
                                       &Solution::GetLeastNumbers_Solution2,
                                       &Solution::GetLeastNumbers_Solution3,
                                       &Solution::GetLeastNumbers_Solution4,
                                       &Solution::GetLeastNumbers_Solution};
};

// 获取随机整数向量
void get_rand_vec(std::vector<int>& vec, int range, int length) {
    if (range <= 0) {
        return;
    }

    srand(time(nullptr));
    for (int i = 0; i < length; i++) {
        vec.push_back(rand() % range);
    }
}

int main(int argc, char* argv[])
{
    std::vector<int> input = {4, 5, 1, 6, 2, 7, 3, 8};
    std::vector<int> input2;
    std::vector<int> input3;
    get_rand_vec(input2, 1000, 1000);
    get_rand_vec(input3, 100000, 100000);

    Solution s;
    s.test(input, 4);
    std::cout << "=====" << std::endl;
    s.test(input2, 7);
    std::cout << "=====" << std::endl;
    s.test(input3, 10);

    return 0;
}