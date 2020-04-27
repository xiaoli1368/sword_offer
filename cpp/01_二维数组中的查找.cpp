#include <iostream>
#include <vector>
#include <stdio.h>
#include <sys/time.h>

class Solution {
public:
    // 暴力枚举
	bool Find1(int target, std::vector<std::vector<int>> array) {
		if (array.empty()) {
			return false;
		}

        for (auto i : array) {
			for (auto j : i) {
				if (j == target) {
					return true;
				}
			}
		}

		return false;
	}
	
	// 从左下开始查找的版本
	bool Find2(int target, std::vector<std::vector<int>> array) {
		if (array.empty()) {
			return false;
		}

		int i = array.size() - 1;
		int j = 0;
		while (j < array[0].size() && i >= 0) {
	        if (target == array[i][j]) {
			    return true;
			} else if (target < array[i][j]) {
			    i--;
			} else {
			    j++;
			}
		}

		return false;
	}


    // 最终优化版，从右上开始查找
	bool Find(int target, std::vector<std::vector<int>> array) {
		if (array.empty()) {
			return false;
		}

		int i = 0;
		int j = array[0].size() - 1;
		while (i < array.size() && j >= 0) {
	        if (target == array[i][j]) {
			    return true;
			} else if (target < array[i][j]) {
			    j--;
			} else {
			    i++;
			}
		}

		return false;
	}

    // 测试函数
	void test(int& target, std::vector<std::vector<int>>& array) {
		bool result;
		struct timeval start, end;

		for (auto ptr : this->func_vec_) {
			gettimeofday(&start, 0);
			result = (this->*ptr)(target, array);
			gettimeofday(&end, 0);
			printf("result: %d, time(us): %ld\n", result, end.tv_usec - start.tv_usec);
		}
	}

private:
    typedef bool (Solution::*func_ptr)(int, std::vector<std::vector<int>>);
	std::vector<func_ptr> func_vec_ = {&Solution::Find1,
	                                   &Solution::Find2,
									   &Solution::Find};
};

int main(int argc, char* argv[])
{
    int target = 26;
	std::vector<std::vector<int>> array = {{1, 4, 7, 11, 15},
	                                       {2, 5, 8, 12, 19},
	                                       {3, 6, 9, 16, 22},
	                                       {10, 13, 14, 17, 24},
										   {18, 21, 23, 26, 30}};
	Solution s;
	s.test(target, array);
	std::cout << "==========" << std::endl;
	target = 29;
	s.test(target, array);

	return 0;
}
