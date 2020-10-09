#include <stdio.h>
#include <vector>

#define MIN(x, y) ((x) < (y) ? (x) : (y))
#define MAX(x, y) ((x) > (y) ? (x) : (y))

class Solution {
public:
	// 直接法
	void getMinMax1(std::vector<int>& num, int* min, int* max) {
		if (num.empty()) {
			*min = 0;
			*max = 0;
		}
		*min = num[0];
		*max = num[0];
		for (auto & i : num) {
			if (i < *min) {
				*min = i;
			} 
			if (i > *max) {
				*max = i;
			}
		}
	}

	// 分组比较法，每次取两个数
	void getMinMax2(std::vector<int>& num, int* min, int* max) {
		if (num.empty()) {
			*min = 0;
			*max = 0;
		}
		for (int i = 0; i < num.size() / 2; i++) {
			int curr_min = MIN(num[2*i], num[2*i+1]);
			int curr_max = MAX(num[2*i], num[2*i+1]);
			*min = MIN(*min, curr_min);
			*max = MAX(*max, curr_max);
		}
		// 处理长度为奇数的特殊情况
		if (num.size() % 2 == 1) {
			*min = MIN(*min, num.back());
			*max = MAX(*max, num.back());
		}
	}

	// 递归法，类似归并排序
	void getMinMax3(std::vector<int>& num, int* min, int* max) {
		if (num.empty()) {
			*min = 0;
			*max = 0;
		}
		getMinMaxWithIndex(num, 0, num.size() - 1, min, max);
	}

	// 归并比较的工具函数
	void getMinMaxWithIndex(std::vector<int>& num, int l, int h, int* min, int* max) {
		if (l == h) {
			*min = num[l];
			*max = num[h];
			return;
		}
		int m = l + (h - l) / 2;
		int lmin = 0, lmax = 0, hmin = 0, hmax = 0;
		getMinMaxWithIndex(num, l, m, &lmin, &lmax);
		getMinMaxWithIndex(num, m + 1, h, &hmin, &hmax);
		*min = MIN(lmin, hmin);
		*max = MAX(lmax, hmax);
	}
	
    // 测试函数
	void test(std::vector<int>& num) {
		for (auto & func : this->func_vec_) {
			int min = 0, max = 0;
			(this->*func)(num, &min, &max);
			printf("result: (%d, %d)\n", min, max);
		}
	}

private:
    typedef void (Solution::*func_ptr)(std::vector<int>&, int*, int*);
	std::vector<func_ptr> func_vec_ = {&Solution::getMinMax1,
	                                   &Solution::getMinMax2,
									   &Solution::getMinMax3};
};

int main(int argc, char* argv[])
{
	std::vector<int> num = {3, 0, 5, 8, 3, 3, 4, 9, 1};
	Solution s;
	s.test(num);
	return 0;
}