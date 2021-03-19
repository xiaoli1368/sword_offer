class Solution {
public:
    int longestValidParentheses(string s) {
        int ret = 0;
        std::stack<int> st;
        st.push(-1);
        for (int i = 0; i < s.size(); i++) {
            if (st.size() > 1 && s[st.top()] == '(' && s[i] == ')') {
                st.pop();
                ret = max(ret, i - st.top());
            } else {
                st.push(i);
            }
        }
        return ret;
    }

    int longestValidParentheses(string s) {
        int ret = 0, n = s.size();
        vector<int> dp(n + 1, 0);
        for (int i = 2; i <= n; i++) {
            int last_length = dp[i - 1];
            int last_match = i - dp[i - 1] - 2;
            if (s[i - 1] == ')' && last_match >= 0 && s[last_match] == '(') {
                dp[i] = 2 + last_length + dp[last_match];
                ret = max(ret, dp[i]);
            }
        }
        return ret;
    }
};