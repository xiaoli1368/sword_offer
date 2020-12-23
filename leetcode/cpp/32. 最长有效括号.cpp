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
};