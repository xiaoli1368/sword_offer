#include <iostream>
#include <vector>
#include <ctime>
#include <cstdlib>
#include <stdio.h>
#include <sys/time.h>

class Solution {
public:
    // 暴力枚举
    int InversePairs1(std::vector<int> nums) {
        if (nums.empty()) {
            return 0;
        }

        int count = 0;
        for (int i = 0; i < nums.size() - 1; i++) {
            for (int j = i + 1; j < nums.size(); j++) {
                if (nums[i] > nums[j]) {
                    count++;
                }
            }
        }

        return count;
    }

    // 高效方式：归并排序
    long cnt = 0;
    std::vector<int> tmp;
    int InversePairs(std::vector<int> nums) {
        if (nums.empty()) {
            return 0;
        }
        
        tmp = nums;
        mergeSort(nums, 0, nums.size() - 1);
        return int(cnt % 1000000007);
    }

    // 递归调用的函数
    // 注意使用引用，否则排序后无法替换原数组的值
    // 这里其实是二分的思想
    void mergeSort(std::vector<int>& nums, int l, int h) {
        if (l >= h) {
            // 当分组到只剩一个时，返回上一层，开始merge
            return;
        }
        int m = l + (h - l) / 2;
        mergeSort(nums, l, m);     // 左数组，统计，排序
        mergeSort(nums, m + 1, h); // 右数组，统计，排序
        merge(nums, l, m, h);      // 本次的前后数组，统计，排序
    }
    
    // 用来实现当前前后数组统计与合并的函数
    // 将两个有序数组合并为一个，同时统计逆序对
    // 注意使用引用
    void merge(std::vector<int>& nums, int l, int m, int h) {
        int i = l, j = m + 1, k = l;
        while (i <= m || j <= h) {
            if (i > m) { // 此时前数组已被遍历完，所有前数组小于后数组当前值
                tmp[k++] = nums[j++];
            } else if (j > h) { // 后数组被遍历完
                tmp[k++] = nums[i++];
            } else if (nums[i] <= nums[j]) { // 两个数组都没有遍历完，前 < 后
                tmp[k++] = nums[i++];
            } else { // 两个数组都没有遍历完，前 > 后，符合逆序数要求
                tmp[k++] = nums[j++];
                this->cnt += m - i + 1;
            }
        }
        
        // 将完成排序的部分拷贝到原数组中
        for (k = l; k <= h; k++) {
            nums[k] = tmp[k];
        }
    }

    // [NOTE](lzc/2020/10/07):改进版归并合并函数
	void merge(std::vector<int>& nums, int l, int m, int h) {
		int* tmp = new int[h - l + 1];
		for (int i = l; i <= h; i++) {
			tmp[i] = nums[i - l];
		}
		int p = l;
		int q = m + 1;
		for (int i = l; i <= h; i++) {
			if (p <= m && q >= h && tmp[p - l] > tmp[q - l]) {
				cnt += m - q + 1;
			}
			if (p <= m && (q > h || tmp[p - l] <= tmp[q - l])) {
				nums[i] = tmp[p - l];
				p += 1;
			} else {
				nums[i] = tmp[q - l];
				q += 1;
			}
		}
		return;
	}

    // 测试函数
    void test(std::vector<int>& nums) {
        int result = 0;
        struct timeval start, end;
        for (auto func : this->func_vec_) {
            // 必要的处理，防止后续调用干扰
            this->cnt = 0;

            // 正式调用
            gettimeofday(&start, 0);
            result = (this->*func)(nums);
            gettimeofday(&end, 0);
            printf("result: %d, time(us): %ld\n", result, end.tv_usec - start.tv_usec);
        }
    }

private:
    typedef int (Solution::*func_ptr)(std::vector<int>);
    std::vector<func_ptr> func_vec_ = {&Solution::InversePairs1, &Solution::InversePairs};
};

// 获取指定数目和范围的随机数组
void get_rand_vec(std::vector<int>& nums, int range, int length) {
    if (range <= 0) {
        return;
    }

    srand((unsigned)time(nullptr)); // 设置随机数种子
    for (int i = 0; i < length; i++) {
        nums.push_back(rand() % range);
    }
}

int main(int argc, char* argv[])
{
    std::vector<int> nums = {1, 2, 3, 4, 5, 6, 7, 0};
    std::vector<int> nums2;
    get_rand_vec(nums2, 100, 100);
 
    Solution s;
    s.test(nums);
    std::cout << "=====" << std::endl;
    s.test(nums2);

    return 0;
}
