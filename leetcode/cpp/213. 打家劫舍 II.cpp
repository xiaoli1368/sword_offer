class Solution {
public:
    int robLine(const vector<int>& nums, int begin, int end) {
        int prev = 0, curr = 0, tmp = 0;
        for (int i = begin; i <= end; i++) {
            tmp = max(curr, prev + nums[i]);
            prev = curr;
            curr = tmp;
        }
        return curr;
    }

    int rob(vector<int>& nums) {
        int n = nums.size();
        return (n == 1 ? nums[0] : max(robLine(nums, 0, n - 2), robLine(nums, 1, n - 1)));
    }
};