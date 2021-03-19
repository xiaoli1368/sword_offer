class Solution {
public:
    // 最大矩形面积，等于区间极值，高度为区间中的最小值，宽度为区间宽度
    // 使用单调递增栈，一旦不满足要求，则左侧会出现一个求值区间
    // 注意特殊情况，需要遍历到右侧数组外的一个位置
    int largestRectangleArea(vector<int>& heights) {
        if (heights.empty()) {
            return 0;
        }

        int ret = 0;
        int n = heights.size();
        std::stack<int> stack;

        for (int i = 0; i <= n; i++) {
            while (!stack.empty() && (i == n || heights[stack.top()] > heights[i])) {
                int top = stack.top();
                stack.pop();
                int left = (stack.empty() ? -1 : stack.top());
                ret = max(ret, heights[top] * (i - left - 1));
            }
            if (i < n) {
                stack.push(i);
            }
        }

        return ret;
    }

	// ===== 优化版 =====
    int largestRectangleArea(vector<int>& heights) {
        stack<int> st;
        st.push(-1);
        heights.push_back(0);
        int ret = 0, width, min_height;
        for (int i = 0; i < heights.size(); i++) {
            while (st.size() >= 2 && heights[st.top()] > heights[i]) {
                min_height = heights[st.top()];
                st.pop();
                width = i - st.top() - 1;
                ret = max(ret, width * min_height);
            }
            st.push(i);
        }
        return ret;
    }
};