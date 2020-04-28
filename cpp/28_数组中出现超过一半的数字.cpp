#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#include <stdio.h>
#include <sys/time.h>

class Solution {
public:
    // 排序法，直接输出索引为length/2的元素
    // 没有考虑：不存在超过一半的数字
    int MoreThanHalfNum_Solution1(std::vector<int> nums) {
        if (nums.empty()) {
            return 0;
        }

        sort(nums.begin(), nums.end());
        return nums[nums.size() / 2];
    }

    // 排序法
    // 实际检测了是否存在长度超过一半的数字
    int MoreThanHalfNum_Solution2(std::vector<int> nums) {
        if (nums.empty()) {
            return 0;
        }

        // 使用stl排序
        sort(nums.begin(), nums.end());

        int length = nums.size();
        int first = 0;
        int end = first + length / 2;

        while (end < length) {
            if (nums[first] == nums[end]) {
                return nums[first];
            }
            first++;
            end++;
        }
        return 0;
    }

    // map法
    int MoreThanHalfNum_Solution3(std::vector<int> nums) {
        if (nums.empty()) {
            return 0;
        }

        std::map<int, int> map; 
        for (auto i : nums) {
            if (map.count(i) == 0) {
                map[i] = 1;
            } else if (map[i] >= nums.size() / 2) {
                return i;
            } else {
                map[i]++;
            }
        }

        return 0;
    }

    // 高效方法
    // 多数投票法，复杂度是O(n)
    int MoreThanHalfNum_Solution(std::vector<int> nums) {
        if (nums.empty()) {
            return 0;
        }

        int curr_val = 0;
        int curr_cnt = 0;

        for (auto i : nums) {
            if (curr_cnt == 0) {
                curr_cnt = 1;
                curr_val = i;
            } else {
                curr_cnt += (curr_val == i ? 1 : -1);
            }
        }

        // 此时不存在大于一半的数字
        if (curr_cnt == 0) {
            return 0;
        }

        return curr_val;
    }

    // 测试函数
    void test(std::vector<int>& nums) {
        int result = 0;
        struct timeval start, end;
        for (auto func : this->func_vec_) {
            gettimeofday(&start, 0);
            result = (this->*func)(nums);
            gettimeofday(&end, 0);
            printf("result: %d, time(us): %ld\n", result, end.tv_usec - start.tv_usec);
        }
    }

private:
    typedef int (Solution::*func_ptr)(std::vector<int>);
    std::vector<func_ptr> func_vec_ = {&Solution::MoreThanHalfNum_Solution1,
                                       &Solution::MoreThanHalfNum_Solution2,
                                       &Solution::MoreThanHalfNum_Solution3,
                                       &Solution::MoreThanHalfNum_Solution};
    
};

int main(int argc, char* argv[])
{
    std::vector<int> nums = {1, 2, 3, 2, 2, 2, 5, 4, 2};

    Solution s;
    s.test(nums);

    return 0;
}