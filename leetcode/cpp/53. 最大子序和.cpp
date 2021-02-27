class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        if (nums.empty()) {
            return 0;
        }
        int curr_sum = 0, max_sum = INT_MIN;
        for (const int& num : nums) {
            curr_sum = num + max(0, curr_sum);
            max_sum = max(max_sum, curr_sum);
        }
        return max_sum;
    }
};