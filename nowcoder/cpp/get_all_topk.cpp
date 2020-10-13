#include <stdio.h>
#include <vector>
#include <queue>
#include <algorithm>

class Solution {
public:
    // 交换两vector中元素的值
    void swap(std::vector<int>& vec, int a, int b) {
        int tmp = vec[a];
        vec[a] = vec[b];
        vec[b] = tmp;
    }

    // 使用API建堆，默认大顶堆
    // pop_heap自动把堆顶元素放到末尾，然后其它调整为堆
    // 下次操作应该把末尾弹出，或者缩短heap长度
    std::vector<int> getAllTopk_bigheap(std::vector<int> num, int k) {
        std::vector<int> ret;
        std::make_heap(num.begin(), num.end());
        for (int i = 0; i < k; i++) {
            std::pop_heap(num.begin(), num.end() - i);
            ret.push_back(num[num.size() - 1 - i]);
        }
        return ret;
    }

    // 使用API建堆，小顶堆
    std::vector<int> getAllTopk_smallheap(std::vector<int> num, int k) {
        std::make_heap(num.begin(), num.begin() + k - 1, std::greater<>());
        for (int i = k; i < num.size(); i++) {
            if (num[i] > num[0]) {
                swap(num, 0, i);
                std::make_heap(num.begin(), num.begin() + k - 1, std::greater<>());
            }
        }
        std::vector<int> ret(num.begin(), num.begin() + k); 
        return ret;
    }

    // 建立大顶堆
    void heapify_bigheap(std::vector<int>& num, int n, int i) {
        int largest = i;
        int l = 2 * i + 1;
        int r = 2 * i + 2;
        if (l < n && num[l] > num[largest]) {
            largest = l;
        }
        if (r < n && num[r] > num[largest]) {
            largest = r;
        }
        if (largest != i) {
            swap(num, i, largest);
            heapify_bigheap(num, n, largest);
        }
    }

    // 小顶堆的下沉
    void heapify_smallheap(std::vector<int>& num, int n, int i) {
        int smallest = i;
        int l = 2 * i + 1;
        int r = 2 * i + 2;
        if (l < n && num[l] < num[smallest]) {
            smallest = l;
        }
        if (r < n && num[r] < num[smallest]) {
            smallest = r;
        }
        if (smallest != i) {
            swap(num, i, smallest);
            heapify_smallheap(num, n, smallest);
        }
    }

    // 自行构建大顶堆
    std::vector<int> getAllTopk2_bigheap(std::vector<int> num, int k) {
        int n = num.size();
        std::vector<int> ret;
        for (int i = n - 1; i >= 0; i--) {
            heapify_bigheap(num, n, i);
        }
        for (int i = n - 1; i >= n - k; i--) {
            ret.push_back(num[0]);
            swap(num, 0, i);
            heapify_bigheap(num, i, 0);
        }
        return ret;
    }

    // 自行构建小顶堆
    std::vector<int> getAllTopk2_smallheap(std::vector<int> num, int k) {
        int n = num.size() - 1;
        std::vector<int> ret;
        for (int i = 0; i < n; i++) {
            if (i < k) {
                ret.push_back(num[i]);
            } else if (num[i] > ret[0]) {
                ret[0] = num[i];
                heapify_smallheap(ret, k, 0);
            }
        }
        return ret;
    }

    // 打印一维数组
    void printf_1d_vec(std::vector<int> vec) {
        for (auto & i : vec) {
            printf("%d, ", i);
        }
        printf("\n");
    }
};

int main(int argc, char* argv[])
{
    int k = 5;
    std::vector<int> num = {3, 0, 5, 8, 3, 3, 4, 9, 1};
    Solution s;
    s.printf_1d_vec(s.getAllTopk_bigheap(num, k));
    s.printf_1d_vec(s.getAllTopk_smallheap(num, k));
    s.printf_1d_vec(s.getAllTopk2_bigheap(num, k));
    s.printf_1d_vec(s.getAllTopk2_smallheap(num, k));
    return 0;
}