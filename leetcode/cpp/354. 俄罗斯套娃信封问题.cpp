class Solution {
public:
    int maxEnvelopes(vector<vector<int>>& vec) {
        if (vec.empty()) {
            return 0;
        }

        int ret = 1, n = vec.size();
        vector<int> dp(n, 1);
        sort(vec.begin(), vec.end(), [](vector<int>& a, vector<int>& b) {return a[0] * a[1] < b[0] * b[1];});

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < i; j++) {
                if (vec[j][0] < vec[i][0] && vec[j][1] < vec[i][1]) {
                    dp[i] = max(dp[i], 1 + dp[j]);
                }
            }
            ret = max(ret, dp[i]);
        }

        return ret;
    }

    int maxEnvelopes(vector<vector<int>>& vec) {
        if (vec.empty()) {
            return 0;
        }

        int ret = 1, n = vec.size();
        vector<int> dp(n, 1);
        sort(vec.begin(), vec.end(), [](vector<int>& a, vector<int>& b) {return a[0] < b[0] || (a[0] == b[0] && a[1] > b[1]);});

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < i; j++) {
                if (vec[j][1] < vec[i][1]) {
                    dp[i] = max(dp[i], 1 + dp[j]);
                }
            }
            ret = max(ret, dp[i]);
        }

        return ret;
	}

    int maxEnvelopes(vector<vector<int>>& vec) {
        if (vec.empty()) {
            return 0;
        }

        vector<int> dp;
        int n = vec.size(), target;
        sort(vec.begin(), vec.end(), [](vector<int>& a, vector<int>& b) {return a[0] < b[0] || (a[0] == b[0] && a[1] > b[1]);});

        for (int i = 0; i < n; i++) {
            target = vec[i][1];
            if (dp.empty() || dp.back() < target) {
                dp.push_back(target);
                continue;
            }
            int l = 0, h = dp.size() - 1, m;
            while (l < h) {
                m = l + (h - l) / 2;
                if (dp[m] < target) {
                    l = m + 1;
                } else {
                    h = m;
                }
            }
            dp[l] = target;
        }

        return dp.size();
    }
};