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
};