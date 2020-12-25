class Solution {
public:
    int candy(vector<int>& ratings) {
        if (ratings.empty()) {
            return 0;
        }

        int n = ratings.size();
        std::vector<int> ret(n, 1);
        for (int i = 1; i < n; i++) {
            if (ratings[i] > ratings[i - 1]) {
                ret[i] = ret[i - 1] + 1;
            }
        }

        int sum = ret[n - 1];
        for (int i = n - 2; i >= 0; i--) {
            if (ratings[i] > ratings[i + 1] && ret[i] < ret[i + 1] + 1) {
                ret[i] = ret[i + 1] + 1;
            }
            sum += ret[i];
        }
        return sum;
    }
};