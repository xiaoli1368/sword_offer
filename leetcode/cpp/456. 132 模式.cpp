class Solution {
public:
    bool find132pattern(vector<int>& nums) {
        int n = nums.size();
        stack<int> right_st;
        vector<int> left_min(n, INT_MAX);
        for (int i = 1; i < n; i++) {
            left_min[i] = min(left_min[i - 1], nums[i - 1]);
        }
        for (int i = n - 1; i >= 0; i--) {
            int curr = nums[i], left = left_min[i], right = INT_MIN;
            while (!right_st.empty() && right_st.top() < curr) {
                right = right_st.top();
                right_st.pop();
            }
            right_st.push(curr);
            if (left < right && right < curr) {
                return true;
            }
        }
        return false;
    }

    // ===== 优化版 =====
    bool find132pattern(vector<int>& nums) {
        stack<int> st;
        int lasti, currj, lastk = INT_MIN;
        for (int i = nums.size() - 1; i >= 0; i--) {
            lasti = currj = nums[i];
            if (lasti < lastk) {
                return true;
            }
            while (!st.empty() && st.top() < currj) {
                lastk = st.top();
                st.pop();
            }
            st.push(currj);
        }
        return false;
    }
};