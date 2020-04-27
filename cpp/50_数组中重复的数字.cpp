#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <stdio.h>
#include <sys/time.h>

class Solution {
public:
    // 第一次解法
    // Parameters:
    //        nums:        an array of integers
    //        length:      the length of array numbers
    //        duplication: (Output) the duplicated number in the array number
    // Return value:       true if the input is valid, and there are some duplications in the array number
    //                     otherwise false
	bool duplicate1(int numbers[], int length, int* duplication) {
		int i = 0;
		int index = 0;
		while (i < length) {
	        if (numbers[i] == i) {
			    i++;
			} else if (numbers[i] != numbers[numbers[i]]) {
				index = numbers[i];
				numbers[i] = numbers[index];
				numbers[index] = index;
		    } else {
			    duplication[0] = numbers[i];
				return true;
			}
		}
		return false;
	}

    // 单层循环优化版
	bool duplicate2(int nums[], int length, int* duplication) {
		int i = 0;
		while (i < length) {
			if (nums[i] == i) {
				i++;
			} else if (nums[i] == nums[nums[i]]) {
				duplication[0] = nums[i];
				return true;
			} else {
				int curr = nums[i];
				nums[i] = nums[curr];
				nums[curr] = curr;
			}
		}
		return false;
	}

    // 自定义hash版，也可以使用vector<bool>
	bool duplicate3(int nums[], int length, int* duplication) {
		bool tmp[length] = {false};
		for (int i = 0; i < length; i++) {
			if (tmp[nums[i]] == false) {
				tmp[nums[i]] = true;
			} else {
				duplication[0] = nums[i];
				return true;
			}
		}
		return false;
	}

    // map版
	bool duplicate4(int nums[], int length, int* duplication) {
		std::map<int, bool> map;
		for (int i = 0; i < length; i++) {
			if (map.count(nums[i]) == 0) {
				map[nums[i]] = true;
			} else {
				duplication[0] = nums[i];
				return true;
			}
		}
		return false;
	}

    // set版
	bool duplicate5(int nums[], int length, int* duplication) {
		std::set<int> set;
		for (int i = 0; i < length; i++) {
			if (set.insert(nums[i]).second == false) {
				duplication[0] = nums[i];
				return true;
			}
		}
		return false;
	}

    // 双层循环优化法，最终版
    bool duplicate(int nums[], int length, int* duplication) {
        for (int i = 0; i < length; i++) {
            while (nums[i] != i) {
                if (nums[i] == nums[nums[i]]) {
                    duplication[0] = nums[i];
                    return true;
                }
                int curr = nums[i];
                nums[i] = nums[curr];
                nums[curr] = curr;
            }
        }
        return false;
    }

    // 测试函数
    void test(int nums[], int length, int* duplication) {
		bool result;
		struct timeval start, end;

		for (auto ptr : this->func_vec_) {
			gettimeofday(&start, 0);
			result = (this->*ptr)(nums, length, duplication);
			gettimeofday(&end, 0);
            printf("True/False: %d, result: %d, time(us): %ld\n", result, duplication[0], end.tv_usec - start.tv_usec);
		}
	}

private:
    typedef bool (Solution::*func_ptr)(int[], int, int*);
	std::vector<func_ptr> func_vec_ = {&Solution::duplicate1,
	                                   &Solution::duplicate2,
							           &Solution::duplicate3,
							           &Solution::duplicate4,
									   &Solution::duplicate5,
							           &Solution::duplicate};
};

int main (int argc, char* argv[])
{
	int numbers[] = {2, 3, 1, 0, 2, 5, 3};
	int duplication[] = {0};

    Solution s;
	s.test(numbers, 7, duplication);
    return 0;
}
