class Solution {
public:
    bool wordBreak(string s, vector<string>& wordDict) {
        // 特殊情况
        if (s.empty() || wordDict.empty()) {
            return false;
        }

        // 初始化
        int n = s.size();
        vector<int> dp(n + 1, false);
        dp[0] = true;
        unordered_set<string> wdict(wordDict.begin(), wordDict.end());

        // 动态规划
        for (int i = 0; i < n; i++) {
            for (int j = 0; j <= i; j++) {
                if (dp[j] && wdict.count(s.substr(j, i - j + 1)) > 0) {
                    dp[i + 1] = true;
					break;
                }
            }
        }
        return dp[n];
    }

	// ===== 另一种遍历方式（非常高效） =====
    bool wordBreak(string s, vector<string>& wordDict) {
        // 特殊情况
        if (s.empty() || wordDict.empty()) {
            return false;
        }

        // 初始化
        vector<int> dp(s.size() + 1, false);
        dp[0] = true;

        // 动态规划
        for (int i = 0; i < s.size(); i++) {
            for (const auto& word : wordDict) {
                int j = i + 1 - word.size();
                if (j >= 0 && dp[j] && s.substr(j, word.size()) == word) {
                    dp[i + 1] = true;
                    break;
                }
            }
        }
        return dp.back();
    }
};