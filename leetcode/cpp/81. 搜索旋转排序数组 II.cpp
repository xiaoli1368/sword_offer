class Solution {
public:
    bool search(vector<int>& nums, int target) {
        if (nums.empty()) {
            return false;
        }

        int l = 0, h = nums.size() - 1;
        while (l <= h) {
            int m = l + (h - l) / 2;
            if (nums[m] == target) {
                return true;
            } else if (nums[l] == nums[m] && nums[m] == nums[h]) {
                auto it = nums.begin();
                return find(it + l, it + h, target) != it + h; // 注意这里的stl用法
            } else if  (nums[m] <= nums[h]) {
                if (nums[m] < target && target <= nums[h]) {
                    l = m + 1;
                } else {
                    h = m - 1;
                }
            } else if (nums[m] > nums[h]) {
                if (nums[l] <= target && target < nums[m]) {
                    h = m - 1;
                } else {
                    l = m + 1;
                }
            }
        }
        return false;
    }
};