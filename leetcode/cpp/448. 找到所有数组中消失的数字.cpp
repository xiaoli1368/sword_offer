class Solution {
public:
    vector<int> findDisappearedNumbers(vector<int>& nums) {
        vector<int> ret;
        for (int i = 0; i < nums.size(); i++) {
            while (nums[nums[i] - 1] != nums[i]) {
                int tmp = nums[nums[i] - 1];
                nums[nums[i] - 1] = nums[i];
                nums[i] = tmp;
            }
        }
        for (int i = 0; i < nums.size(); i++) {
            if (i + 1 != nums[i]) {
                ret.push_back(i + 1);
            }
        }
        return ret;
    }

	// 把已经出现过的位置标记为负数，最终保持正数的位置就是没有出现过的元素
    vector<int> findDisappearedNumbers(vector<int>& nums) {
        vector<int> ret;
        for (const int& num : nums) {
            int pos = (num > 0 ? num : -num) - 1;
            if (nums[pos] > 0) {
                nums[pos] = -nums[pos];
            }
        }
        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] > 0) {
                ret.push_back(i + 1);
            }
        }
        return ret;
    }
};