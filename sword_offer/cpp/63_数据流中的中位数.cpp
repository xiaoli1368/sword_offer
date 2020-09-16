#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
#include <stdio.h>
#include <sys/time.h>

/* 抽象基类（为了自行测试方便）
 * 利用虚函数、纯虚函数，实现基类调用子类成员
 * 基类的数据结构data继承到子类，可以选择不使用
 */
class Solution {
public:
    std::vector<int> data;

    virtual void Insert(int num) = 0;

    virtual double GetMedian() {
        if (data.empty()) {
            return 0;
        }

        int length = data.size();
        if (length % 2 == 1) {
            return data[length / 2];
        } else {
            return double(data[length / 2] + data[length / 2 - 1]) / 2;
        }
    }
};

// 方法一：利用stl排序
class Solution1 : public Solution {
public:
    void Insert(int num) {
        data.push_back(num);
        sort(data.begin(), data.end());
    }
};

// 方法二：遍历寻找插入位置，插入保证有序
class Solution2 : public Solution {
public:
    void Insert(int num) {
        if (data.empty()) {
            data.push_back(num);
            return;
        }

        int i = 0;
        while (i < data.size() && num > data[i]) {
            i++;
        }
        data.insert(data.begin() + i, num);
    }
};

// 方法三：利用二分查找，插入排序
class Solution3 : public Solution {
public:
    void Insert(int num) {
        int index = binarySearch(num);
        if (index >= data.size()) {
            data.push_back(num);
        } else {
            data.insert(data.begin() + index, num);
        }
    }

    // 二分查找左边界
    int binarySearch(int num) {
        if (data.empty()) {
            return 0;
        }

        int l = 0;
        int h = data.size() - 1;

        while (l <= h) {
            int m = l + (h - l) / 2;
            if (num >= data[m]) {
                l = m + 1;
            } else if (num < data[m]) {
                h = m - 1;
            }
        }

        return l;
    }
};

// 方法四：优先队列（堆）方法
class Solution4 : public Solution {
private:
    std::priority_queue<int> maxQueue; // 大顶堆
    std::priority_queue<int, std::vector<int>, std::greater<int>> minQueue; // 小顶堆
public:
    void Insert(int num) {
        // 先向大顶堆插入新元素，然后将大顶堆堆顶pop-push进入小顶堆
        maxQueue.push(num);
        minQueue.push(maxQueue.top());
        maxQueue.pop();

        // 从小顶堆向大顶堆回推，保证二者size相等或者相差为1
        if (maxQueue.size() < minQueue.size()) {
            maxQueue.push(minQueue.top());
            minQueue.pop();
        }
    }

    double GetMedian() {
        if (maxQueue.size() > minQueue.size()) {
            return maxQueue.top();
        } else {
            return (maxQueue.top() + minQueue.top()) * 0.5;
        }
    }
};

// ===== 工具函数 =====

// 打印double向量
void printf_1d_vec(std::vector<double>& vec) {
    for (auto i : vec) {
        printf("%.1f, ", i);
    }
    printf("\n");
}

// 测试函数
void test(std::vector<int>& input, std::vector<Solution*>& classPtr) {
    struct timeval start, end;
    for (auto ptr : classPtr) {
        std::vector<double> result;
        gettimeofday(&start, nullptr);
        for (auto i : input) {
            ptr->Insert(i);
            result.push_back(ptr->GetMedian());
        }
        gettimeofday(&end, nullptr);
        printf("time(us): %3ld, result: ", end.tv_usec - start.tv_usec);
        printf_1d_vec(result);
    }
}

int main(int argc, char* argv[])
{
    Solution1 s1;
    Solution2 s2;
    Solution3 s3;
    Solution4 s4;
    std::vector<Solution*> classPtr = {&s1, &s2, &s3, &s4};
    std::vector<int> input = {1, 2, 4, 9, 6, 7, 1, 3, 3, 5, 10, 8, 3, 2, 4, 5};

    test(input, classPtr);

    return 0;
}