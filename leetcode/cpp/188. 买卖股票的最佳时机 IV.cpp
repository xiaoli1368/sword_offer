class Solution {
public:
    int maxProfit(int k, vector<int>& prices) {
        if (prices.empty() || k <= 0) {
            return 0;
        }
        vector<int> sell(k, 0), buy(k, prices[0]);
        for (const int& price : prices) {
            for (int j = 0; j < k; j++) {
                int lastSell = (j == 0 ? 0 : sell[j - 1]);
                buy[j] = min(buy[j], price - lastSell);
                sell[j] = max(sell[j], price - buy[j]);
            }
        }
        return sell.back();
    }
};