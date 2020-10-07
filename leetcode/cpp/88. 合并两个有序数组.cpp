#include <stdio.h>
#include <vector>

class Solution {
public:
    // 合并两个有序数组
    void merge(std::vector<int>& num1, int m, std::vector<int>& num2, int n) {
		m -= 1;
		n -= 1;
		for (int i = m + n + 1; i >= 0; i--) {
			if (m >= 0 && (n < 0 || num1[m] >= num2[n])) {
				num1[i] = num1[m--];
			} else {
				num1[i] = num2[n--];
			}
		}
	}

	// 打印一维数组
	void printf_1d_vec(std::vector<int>& vec) {
		for (auto & i : vec) {
			printf("%d, ", i);
		}
		printf("\n");
	}
};

int main(int argc, char* argv[])
{
	int m = 3;
	int n = 3;
	std::vector<int> num1 = {1, 2, 3, 0, 0, 0};
	std::vector<int> num2 = {2, 5, 6};

	Solution s;
	s.merge(num1, m, num2, n);
	s.printf_1d_vec(num1);

	return 0;
}