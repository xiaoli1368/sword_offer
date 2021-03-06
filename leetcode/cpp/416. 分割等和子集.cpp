class Solution {
public:
    // dp[i][j]定义为使用前i个元素，在容量为j的情况下，能否全部填充背包
    //         也就是使用前i个元素，刚好可以获取和为j的子集
    // dp[i][j] = dp[i - 1][j] || dp[i - 1][j - nums[i]]
    bool canPartition(vector<int>& nums) {
        int sum = accumulate(nums.begin(), nums.end(), 0);
        if (nums.empty() || sum % 2 == 1) {
            return false;
        }

        int row = nums.size(), col = sum / 2;
        vector<int> dp(col + 1, false);
        dp[0] = true;

        for (int i = 1; i <= row; i++) {
            for (int j = col; j >= nums[i - 1]; j--) {
                dp[j] = dp[j] || dp[j - nums[i - 1]];
            }
        } 
        return dp[col];
    }
};