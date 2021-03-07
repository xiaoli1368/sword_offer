class Solution {
public:
    int maxProfit(vector<int>& prices, int fee) {
        if (prices.empty()) {
            return 0;
        }
        int sell = 0, buy = prices[0];
        for (const int& price : prices) {
            buy = min(buy, price - sell);
            sell = max(sell, price - buy - fee);
        }
        return sell;
    }
};