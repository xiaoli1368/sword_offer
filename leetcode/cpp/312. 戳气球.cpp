class Solution {
public:
    // 动态规划
    // dp[i][j]表示区间[i:j]能取到的最大值
    // dp[i][j] = max(dp[i][j], dp[i][k-1] + score_k + dp[k+1][j])，选定k为最后遍历的元素
    // i依赖更大的k+1，j依赖于更小的k-1，因此i从大到小遍历，j从小到大遍历
    // 初始化dp[i][j]为全0，注意 i <= j
    int maxCoins(vector<int>& nums) {
        if (nums.empty()) {
            return 0;
        }
        nums.push_back(1);
        nums.insert(nums.begin(), 1);
        int n = nums.size();
        vector<vector<int>> dp(n, vector<int>(n, 0));

        for (int i = n - 2; i >= 1; i--) {
            for (int j = i; j <= n - 2; j++) {
                for (int k = i; k <= j; k++) {
                    dp[i][j] = max(dp[i][j], dp[i][k-1] + nums[i-1]*nums[k]*nums[j+1] + dp[k+1][j]);
                }
            }
        }
        return dp[1][n-2];
    }
};