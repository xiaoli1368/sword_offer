#include <stdio.h>
#include <vector>

class Solution {
public:
    // 交换函数
	void swap(std::vector<int>& num, int a, int b) {
		int tmp = num[a];
		num[a] = num[b];
		num[b] = tmp;
	}
    
    // 直接快排版本，快排分区函数
	int partition(std::vector<int>& num, int l, int h) {
		int start = l - 1;
		for (int i = l; i < h; i++) {
			if (num[i] < num[h]) {
				swap(num, i, ++start);
			}
		}
		swap(num, h, ++start);
		return start;
	}

	// 快排寻找topk
	int getTopK(std::vector<int>& num, int k) {
		if (num.size() < k) {
			return -1;
		}
		int l = 0, h = num.size() - 1;
		k = num.size() - k;
		while (1) {
			int m = partition(num, l, h);
			if (m == k) {
				return num[m];
			} else if (m < k) {
				l = m + 1;
			} else {
				h = m - 1;
			}
		}
	}
};

int main(int argc, char* argv[])
{
	int k = 5;
	std::vector<int> num = {3, 0, 5, 8, 3, 3, 4, 9, 1};
	Solution s;
	printf("%d\n", s.getTopK(num, k));

	// just for test
	// 也就是说num并不是等价于数组名
	int* ptr = (int*)(&num);
	printf("just for test: %d\n", *(ptr + 0));

	return 0;
}