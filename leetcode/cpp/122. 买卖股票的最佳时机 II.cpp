class Solution {
public:
    int maxProfit(vector<int>& prices) {
        // 本质是统计递增段的最高度
        if (prices.empty()) {
            return 0;
        }

        int ret = 0;
        int last = prices[0];
        for (int i = 1; i < prices.size(); i++) {
            ret += max(prices[i] - last, 0);
            last = prices[i];
        }
        return ret;
    }
};