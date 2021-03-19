class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& vec) {
        if (vec.empty()) {
            return vec;
        }

        std::stack<int> stack;
        std::vector<int> ret(vec.size(), 0);

        for (int i = 0; i < vec.size(); i++) {
            while (!stack.empty() && vec[stack.top()] < vec[i]) {
                int j = stack.top();
                stack.pop();
                ret[j] = i - j;
            }
            stack.push(i);
        }
        return ret;
    }

	// ===== 优化版 =====
    vector<int> dailyTemperatures(vector<int>& T) {
        stack<int> st;
        vector<int> ret(T.size(), 0);
        for (int i = 0; i < T.size(); i++) {
            while (!st.empty() && T[st.top()] < T[i]) {
                ret[st.top()] = i - st.top();
                st.pop();
            }
            st.push(i);
        }
        return ret;
    }
};