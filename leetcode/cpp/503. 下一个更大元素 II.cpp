class Solution {
public:
    vector<int> nextGreaterElements(vector<int>& nums) {
        if (nums.empty()) {
            return nums;
        }

        int n = nums.size();
        std::vector<int> ret(n, -1);
        std::stack<int> stack;

        for (int i = 0; i < 2 * n; i++) {
            int j = i % n;
            while (!stack.empty() && nums[stack.top()] < nums[j]) {
                int top = stack.top();
                stack.pop();
                ret[top] = nums[j];
            }
            stack.push(j);
        }
        return ret;
    }
};