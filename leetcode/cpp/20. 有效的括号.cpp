class Solution {
public:
    std::stack<char> stack;

    bool isValid(string s) {
        if (s == "") {
            return true;
        }

        for (auto & i : s) {
            if (i == '(' || i == '[' || i == '{') {
                stack.push(i);
            } else if (stack.empty()) {
                return false;
            } else if (i == ')' && stack.top() == '(') {
                stack.pop();
            } else if (i == ']' && stack.top() == '[') {
                stack.pop();
            } else if (i == '}' && stack.top() == '{') {
                stack.pop();
            } else {
                stack.push(i);
            }
        }

        return stack.empty();
    }

	// ===== 优化版 =====
    bool isValid(string s) {
        stack<char> st;
        unordered_map<char, char> d;
        d['('] = ')', d['['] = ']', d['{'] = '}';
        for (const char& chr : s) {
            if (d.count(chr) > 0) {
                st.push(chr);
            } else if (!st.empty() && d[st.top()] == chr) {
                st.pop();
            } else {
                return false;
            }
        }
        return st.empty();
    }
};