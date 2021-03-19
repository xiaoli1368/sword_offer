class Solution {
public:
    vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
        if (nums1.empty() || nums2.empty()) {
            return std::vector<int>{};
        }

        // 构造nums1由val到ind的映射
        std::unordered_map<int, int> map;
        for (int i = 0; i < nums1.size(); i++) {
            map[nums1[i]] = i;
        }

        // 对nums2使用单调递减栈，直接保存值
        std::stack<int> stack;
        std::vector<int> ret(nums1.size(), -1);
        for (auto & val2 : nums2) {
            while (!stack.empty() && stack.top() < val2) {
                int val = stack.top();
                stack.pop();
                if (map.count(val) > 0) {
                    ret[map[val]] = val2;
                }
            }
            stack.push(val2);
        }
        return ret;
    }

	// ===== 优化版 =====
    vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
        stack<int> st;
        unordered_map<int, int> d;
        vector<int> ret(nums1.size(), -1);
        for (int i = 0; i < nums1.size(); i++) {
            d[nums1[i]] = i;
        }
        for (const int& val : nums2) {
            while (!st.empty() && st.top() < val) {
                int num = st.top();
                st.pop();
                if (d.count(num) > 0) {
                    ret[d[num]] = val;
                }
            }
            st.push(val);
        }
        return ret;
    }
};