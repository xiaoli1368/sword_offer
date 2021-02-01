class Solution {
public:
    int singleNonDuplicate(vector<int>& nums) {
        /*
        // 异或法
        int ret = 0;
        for (const auto & i : nums) {
            ret ^= i;
        }
        return ret;
        */

        // 二分法
        if (nums.empty()) {
            return 0;
        }
        int l = 0, h = nums.size() - 1;
        while (l < h) {
            int m = l + (h - l + 1) / 2;
            if (m % 2 == 1) {
                m -= 1;
            }
            if (nums[m] == nums[m + 1]) {
                l = m + 2;
            } else {
                h = m;
            }
        }
        return nums[l];
    }
};