#include <vector>
#include <map>

class Solution {
public:
	// 交换函数
	void swap(std::vector<std::vector<int>>& vec, int a, int b) {
		auto tmp = vec[a];
		vec[a] = vec[b];
		vec[b] = tmp;
	}

    // 堆化下沉函数
	void heapify(std::vector<std::vector<int>>& vec, int n, int i) {
		int largest = i;
		int l = 2 * i + 1;
		int r = 2 * i + 2;
		if (l < n && vec[l][1] > vec[largest][1]) {
			largest = l;
		}
		if (r < n && vec[r][1] > vec[largest][1]) {
			largest = r;
		}
		if (largest != i) {
			swap(vec, i, largest);
			heapify(vec, n, largest);
		}
	}

	std::vector<int> topKFrequent(std::vector<int>& nums, int k) {
		// 使用字典统计元素个数
		std::map<int, int> map;
		for (auto & i : nums) {
			map[i]++;
		}

		// 转换为二维数组
		std::vector<std::vector<int>> vec;
		for (auto it = map.begin(); it != map.end(); it++) {
			std::vector<int> tmp = {it->first, it->second};
			vec.push_back(tmp);
		}

		// 进行堆排序
		std::vector<int> ret;
		int n = vec.size();
		for (int i = n - 1; i >= 0; i--) {
			heapify(vec, n, i);
		}
		for (int i = n - 1; i >= n - k; i--) {
			ret.push_back(vec[0][0]);
			swap(vec, 0, i);
			heapify(vec, i, 0);
		}
		return ret;
	}

	// ===== 另一种方法 =====
	// 交换函数
	void swap(std::vector<std::vector<int>>& vec, int a, int b) {
		auto tmp = vec[a];
		vec[a] = vec[b];
		vec[b] = tmp;
	}

    // 快排分区函数
    int partition(std::vector<std::vector<int>>& vec, int l, int h) {
        int start = l - 1;
        for (int i = l; i < h; i++) {
            if (vec[i][1] > vec[h][1]) {
                swap(vec, i, ++start);
            }
        }
        swap(vec, h, ++start);
        return start;
    }

    // 快排递归函数
    void quickSort(std::vector<std::vector<int>>& vec, int l, int h) {
        if (l >= h) {
            return;
        }
        int m = partition(vec, l, h);
        quickSort(vec, l, m - 1);
        quickSort(vec, m + 1, h);
        return;
    }

	std::vector<int> topKFrequent(std::vector<int>& nums, int k) {
        // 特殊情况
        if (nums.empty() || k > nums.size()) {
            return std::vector<int>{};
        }

		// 使用字典统计元素个数
        std::map<int, int> map;
        for (auto & i : nums) {
            map[i]++;
        }

        // 整理为二维vector
        std::vector<std::vector<int>> ret;
        for (auto it = map.begin(); it != map.end(); it++) {
            ret.push_back(std::vector<int>{it->first, it->second});
        }

        // 二分找到第k大元素的索引
        int l = 0, h = ret.size() - 1;
        while (l <= h) {
            int m = partition(ret, l, h);
            if (m == k - 1) {
                quickSort(ret, 0, m);
                break;
            } else if (m > k - 1) {
                h = m - 1;
            } else if (m < k - 1) {
                l = m + 1;
            }
        }

        // 返回topk
        std::vector<int> tmp;
        for (int i = 0; i < k; i++) {
            tmp.push_back(ret[i][0]);
        }
        return tmp;
	}
};