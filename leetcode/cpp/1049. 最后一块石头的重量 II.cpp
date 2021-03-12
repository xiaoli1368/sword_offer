class Solution {
public:
    int lastStoneWeightII(vector<int>& stones) {
        int ssum = accumulate(stones.begin(), stones.end(), 0);
        vector<int> dp(ssum / 2 + 1, 0);
        for (const int& stone : stones) {
            for (int j = dp.size() - 1; j >= stone; j--) {
                dp[j] = max(dp[j], dp[j - stone] + stone);
            }
        }
        return ssum - 2 * dp.back();
    }
};