class Solution {
public:
    vector<int> findDuplicates(vector<int>& nums) {
        vector<int> ret;
        for (int i = 0; i < nums.size(); i++) {
            while (nums[i] > 0 && nums[i] != nums[nums[i] - 1]) {
                int tmp = nums[nums[i] - 1];
                nums[nums[i] - 1] = nums[i];
                nums[i] = tmp;
            }
            if (nums[i] > 0 && nums[i] != i + 1) {
                ret.push_back(nums[i]);
                nums[i] = -nums[i];
            }
        }
        return ret;
    }
};