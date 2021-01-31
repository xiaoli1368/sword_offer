class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        // 特殊情况
        std:;vector<int> ret = {-1, -1};
        if (nums.empty()) {
            return ret;
        }
        // 进行二分
        int n = nums.size();
        int l = 0;
        int h = n - 1;
        while (l <= h) {
            int m = l + (h - l) / 2;
            if (nums[m] >= target) {
                h = m - 1;
            } else if (nums[m] < target) {
                l = m + 1;
            }
        }
        // 验证左边界
        int left = h + 1;
        if (left < 0 || left >= n || nums[left] != target) {
            return ret;
        }
        // 查找右边界
        int right = left;
        while (right + 1 < n && nums[right + 1] == target) {
            right += 1;
        }
        // 返回结果
        ret[0] = left, ret[1] = right;
        return ret;
    }

	// ===== 更加简便的方法 =====
    // 找到大于等于target的最小索引，注意结果有可能越界
    int binarySearch(vector<int>& nums, int target, int l, int h) {
        while (l < h) {
            int m = l + (h - l) / 2;
            if (nums[m] < target) {
                l = m + 1;
            } else {
                h = m;
            }
        }
        return (l >= nums.size() || nums[l] >= target ? l : l + 1);
    }

    vector<int> searchRange(vector<int>& nums, int target) {
        int n = nums.size();
        int left = binarySearch(nums, target, 0, n - 1);
        int right = binarySearch(nums, target + 1, left, n - 1);
        if (left < n && nums[left] == target) {
            return vector<int>{left, right - 1};
        } else {
            return vector<int>{-1, -1};
        }
    }
};