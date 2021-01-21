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

	// 添加注释版
    int candy(vector<int>& ratings) {
        if (ratings.empty()) {
            return 0;
        }
        int n = ratings.size();
        std::vector<int> dp(n, 1);

        // 从左向右遍历，当前比左侧大，则更新为左侧+1
        for (int i = 1; i < n; i++) {
            if (ratings[i] > ratings[i - 1]) {
                dp[i] = dp[i - 1] + 1;
            }
        }

        // 从右往左遍历，当前比右侧大，并且已分配的达不到要求，则更新
        // 同时进行求和
        int sum = dp[n - 1];
        for (int i = n - 2; i >= 0; i--) {
            if (ratings[i] > ratings[i + 1] && dp[i] < dp[i + 1] + 1) {
                dp[i] = dp[i + 1] + 1;
            }
            sum += dp[i];
        }

        // 返回结果
        return sum;
    }
};