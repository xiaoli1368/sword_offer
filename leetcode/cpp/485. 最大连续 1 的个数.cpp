class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        int ret = 0, l = -1;
        for (int h = 0; h < nums.size(); h++) {
            if (nums[h] == 1) {
                ret = max(ret, h - l);
            } else {
                l = h;
            }
        }
        return ret;
    }
};