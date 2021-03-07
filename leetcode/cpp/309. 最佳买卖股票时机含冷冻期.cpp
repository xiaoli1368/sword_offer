class Solution {
public:
    int maxProfit(vector<int>& prices) {
        if (prices.empty()) {
            return 0;
        }
        int last_buy = prices[0], last_cell = 0, last2_cell = 0, curr_buy, curr_sell;
        for (const int& price : prices) {
            curr_buy = min(last_buy, price - last2_cell);
            curr_sell = max(last_cell, price - last_buy);
            last_buy = curr_buy;
            last2_cell = last_cell;
            last_cell = curr_sell;
        }
        return curr_sell;
    }
};