class Solution {
public:
    int maxProfit(vector<int>& prices) {
        if (prices.empty()) {
            return 0;
        }
        int sell1 = 0, sell2 = 0;
        int buy1 = prices[0], buy2 = prices[0];
        for (const int& price : prices) {
            buy1 = min(buy1, price);
            sell1 = max(sell1, price - buy1);
            buy2 = min(buy2, price - sell1);
            sell2 = max(sell2, price - buy2);
        }
        return sell2;
    }
};