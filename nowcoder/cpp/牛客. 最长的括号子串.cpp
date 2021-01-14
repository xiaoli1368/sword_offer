class Solution {
public:
    /**
     * 
     * @param s string字符串 
     * @return int整型
     */
    int longestValidParentheses(string s) {
        // write code here
        if (s.empty()) {
            return 0;
        }
        
        int ret = 0;
        std::stack<int> stack;
        stack.push(-1);
        
        for (int i = 0; i < s.size(); i++) {
            if (s[i] == ')' && !stack.empty() && stack.top() >= 0 && s[stack.top()] == '(') {
                stack.pop();
                ret = max(ret, i - stack.top());
            } else {
                stack.push(i);
            }
        }
        return ret;
    }
};