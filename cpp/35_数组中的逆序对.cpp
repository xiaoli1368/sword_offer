#include <iostream>
#include <vector>

class Solution {
public:
    long cnt = 0;
    std::vector<int> tmp;
    
    // 外部接口函数
    int InversePairs(std::vector<int> nums) {
        int length = nums.size();
        if (length == 0) {
            return 0;
        }
        
        tmp = nums;
        mergeSort(nums, 0, length - 1);
        return int(cnt % 1000000007);
    }

    // 递归调用的函数
    // 注意使用引用，否则排序后无法替换原数组的值
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
};

int main(int argc, char* argv[])
{
    Solution s;
    std::vector<int> nums = {1, 2, 3, 4, 5, 6, 7, 0};

    std::cout << s.InversePairs(nums) << std::endl;
    return 0;
}
