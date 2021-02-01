class Solution {
public:
	// ===== 之前的解法 =====
    int min(vector<int>& nums, int l, int h) {
        int tmp = nums[l];
        for (int i = l; i <= h; i++) {
            if (tmp > nums[i]) {
                tmp = nums[i];
            }
        }
        return tmp;
    }

    int findMin(vector<int>& nums) {
        if (nums.empty()) {
            return 0;
        }

        int l = 0;
        int h = nums.size() - 1;
        while (l <= h) {
            int m = (l + h) / 2;
            if (nums[l] == nums[m] && nums[m] == nums[h]) {
                return min(nums, l, h);
            } else if (nums[m] <= nums[h]) {
                h = m;
            } else {
                l = m + 1;
            }
        }
        return nums[l];
    }

	// ===== 后续的解法 =====
    int findMin(vector<int>& nums) {
        if (nums.empty()) {
            return 0;
        }

        int l = 0, h = nums.size() - 1;
        while (l < h) {
            int m = l + (h - l) / 2;
            if (nums[l] == nums[m] && nums[m] == nums[h]) {
                return *min_element(nums.begin() + l, nums.begin() + h);
            } else if (nums[m] <= nums[h]) {
                h = m;
            } else {
                l = m + 1;
            }
        }
        return nums[l];
    }
};