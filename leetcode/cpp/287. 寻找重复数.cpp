class Solution {
public:
    // 使用hash
    int findDuplicate(vector<int>& nums) {
        unordered_set<int> s;
        for (const int& num : nums) {
            if (s.count(num) > 0) {
                return num;
            }
            s.insert(num);
        }
        return -1;
    }

    // 原地hash
    int findDuplicate(vector<int>& nums) {
        for (int i = 0; i < nums.size(); i++) {
            while (nums[nums[i] - 1] != nums[i]) {
                int tmp = nums[nums[i] - 1];
                nums[nums[i] - 1] = nums[i];
                nums[i] = tmp;
            }
            if (nums[i] - 1 != i) {
                return nums[i];
            }
        }
        return -1;
    }
};