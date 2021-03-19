class Solution {
public:
    int maximumScore(vector<int>& nums, int k) {
        stack<int> st;
        st.push(-1);
        nums.push_back(0);
        nums.insert(nums.begin(), 0);
        int ret = 0, min_val, i, j;
        for (int x = 0; x < nums.size(); x++) {
            while (st.size() > 1 && nums[st.top()] > nums[x]) {
                min_val = nums[st.top()];
                st.pop();
                i = st.top() + 1;
                j = x - 1;
                if (i <= k + 1 && k + 1 <= j) {
                    ret = max(ret, min_val * (j - i + 1));
                }
            }
            st.push(x);
        }
        return ret;
    }

	// ===== 双指针法 =====
    int maximumScore(vector<int>& nums, int k) {
        int i = k, j = k, n = nums.size();
        int ret = nums[k], mmin = nums[k];
        while (1) {
            while (i - 1 >= 0 && nums[i - 1] >= mmin) {
                i -= 1;
            }
            while (j + 1 < n && nums[j + 1] >= mmin) {
                j += 1;
            }
            ret = max(ret, mmin * (j - i + 1));
            if (i == 0 && j == n - 1) {
                break;
            }
            if (i - 1 >= 0 && j + 1 < n) {
                mmin = max(nums[i - 1], nums[j + 1]);
            } else if (i - 1 < 0) {
                mmin = nums[j + 1];
            } else {
                mmin = nums[i - 1];
            }
        }
        return ret;
    }
};