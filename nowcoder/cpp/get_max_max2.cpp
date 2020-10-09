#include <stdio.h>
#include <vector>

#define MIN(x, y) ((x) < (y) ? (x) : (y))
#define MAX(x, y) ((x) > (y) ? (x) : (y))
#define MIN_INT 0x80000000

class Solution {
public:
	// 直接归并法了
	void getMaxOneAndTwo(std::vector<int>& num, int* max, int* max2) {
		if (num.empty()) {
			*max = 0;
			*max2 = 0;
		}
		if (num.size() == 1) {
			*max = num[0];
			*max2 = num[0];
		}
		mergeGetTwoMax(num, 0, num.size() - 1, max, max2);
	}

	// 归并递归函数
	void mergeGetTwoMax(std::vector<int>& num, int l, int h, int* max, int* max2) {
		if (l == h) {
			*max = num[l];
			*max2 = MIN_INT;
			return;
		}
		if (l + 1 == h) {
			*max = MAX(num[l], num[h]);
			*max2 = MIN(num[l], num[h]);
			return;
		}
		int m = l + (h - l) / 2;
		int lmax = 0, lmax2 = 0, hmax = 0, hmax2 = 0;
		mergeGetTwoMax(num, l, m, &lmax, &lmax2);
		mergeGetTwoMax(num, m + 1, h, &hmax, &hmax2);
		if (lmax > hmax) {
			*max = lmax;
			*max2 = MAX(hmax, lmax2);
		} else {
			*max = hmax;
			*max2 = MAX(lmax, hmax2);
		}
	}
};

int main(int argc, char* argv[])
{
	int max = 0, max2 = 0;
	std::vector<int> num = {3, 0, 5, 8, 3, 3, 4, 9, 1};
	Solution s;
	s.getMaxOneAndTwo(num, &max, &max2);
	printf("max: %d, max2: %d\n", max, max2);
	return 0;
}