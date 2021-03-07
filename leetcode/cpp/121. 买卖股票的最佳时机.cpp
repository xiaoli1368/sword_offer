class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int mmax = INT_MIN, mmin = INT_MAX;
        for (const int& price : prices) {
            mmin = min(mmin, price);
            mmax = max(mmax, price - mmin);
        }
        return mmax;
    }
};