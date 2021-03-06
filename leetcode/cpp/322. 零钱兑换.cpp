class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        vector<int> dp(amount + 1, amount + 1);
        dp[0] = 0;
        for (const int& coin : coins) {
            for (int j = coin; j <= amount; j++) {
                dp[j] = min(dp[j], 1 + dp[j - coin]);
            }
        }
        return (dp[amount] > amount ? -1 : dp[amount]);
    }
};