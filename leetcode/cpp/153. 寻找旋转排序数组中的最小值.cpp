class Solution {
public:
    int findMin(vector<int>& nums) {
        if (nums.empty()) {
            return 0;
        }

        int l = 0, h = nums.size() - 1;
        while (l < h) {
            int m = l + (h - l) / 2;
            if (nums[m] <= nums[h]) {
                h = m;
            } else {
                l = m + 1;
            }
        }
        return nums[l];
    }
};