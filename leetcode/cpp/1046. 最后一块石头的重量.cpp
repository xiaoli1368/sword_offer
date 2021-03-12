/*
cpp中优先队列用法：
#include<algorithm>    堆算法
#include<functional>   堆算法中要用的到greater函数

less<int>()
greater<int>()

make_heap(v.begin(), v.end()); // 在v上创建堆，默认大顶堆

v.push_back(new_val);
push_heap(v.begin(), v.end()); // 这样添加新元素

pop_heap(v.begin(), v.end()); // 把堆首元素交换到末尾，不需要调整了
v.pop_back(); // 这样再清除掉
*/

class Solution {
public:
    int lastStoneWeight(vector<int>& stones) {
        if (stones.empty()) {
            return 0;
        }

        make_heap(stones.begin(), stones.end(), less<int>()); // 大顶堆
        while (stones.size() > 1) {
            int y = stones[0];
            pop_heap(stones.begin(), stones.end(), less<int>());
            stones.pop_back();

            int x = stones[0];
            pop_heap(stones.begin(), stones.end(), less<int>());
            stones.pop_back();

            if (x != y) {
                stones.push_back(y - x);
                push_heap(stones.begin(), stones.end());
            }
        }

        return (stones.empty() ? 0 : stones[0]);
    }

	// ===== 手写实现大顶堆 =====
    // 大顶堆下沉函数
    void shift_down(vector<int>& vec, int n, int i) {
        int largest = i, l = 2 * i + 1, r = 2 * i + 2;
        if (l < n && vec[l] > vec[largest]) {
            largest = l;
        }
        if (r < n && vec[r] > vec[largest]) {
            largest = r;
        }
        if (largest != i) {
            swap(vec[i], vec[largest]);
            shift_down(vec, n, largest);
        }
    }

    // 大顶堆上浮函数
    void shift_up(vector<int>& vec, int i) {
        while (i > 0) {
            int parent = (i - 1) / 2;
            if (vec[parent] < vec[i]) {
                swap(vec[parent], vec[i]);
                i = parent;
            } else {
                break;
            }
        }
    }

    // 建立大顶堆
    void heapify(vector<int>& vec) {
        int n = vec.size();
        for (int i = (n-1)/2; i >= 0; i--) {
            shift_down(vec, n, i);
        }
    }

    // 弹出堆顶
    int heappop(vector<int>& vec) {
        int ret = -1, n = vec.size();
        if (!vec.empty()) {
            ret = vec[0];
            swap(vec[0], vec[n - 1]);
            shift_down(vec, n - 1, 0);
            vec.pop_back();
        }
        return ret;
    }

    // 插入元素
    void heappush(vector<int>& vec, int val) {
        vec.push_back(val);
        shift_up(vec, vec.size() - 1);
    }

    int lastStoneWeight(vector<int>& stones) {
        heapify(stones);
        while (stones.size() >= 2) {
            int y = heappop(stones);
            int x = heappop(stones);
            if (y - x > 0) {
                heappush(stones, y - x);
            }
        }
        return (stones.empty() ? 0 : stones[0]);
    }
};