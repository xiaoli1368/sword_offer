/* 1.遍历累加相邻两点递减次数，设为d。
 * 2.遍历累加间隔一点的前后两点递减次数，设为g。
 * 3.如果d或g为2，则为False，反之为True。
 * 讲道理这个思路暂时无法理解，应该是得推导一下，以后待定吧。
 */

class Solution {
public:
    bool checkPossibility(vector<int>& nums) {
        if (nums.empty()) {
            return false;
        }
        
        int cnt1 = 0;
        int cnt2 = 0;
        for (int i = 0; i < nums.size() - 1; i++) {
            if (i < nums.size() - 1 && nums[i] > nums[i + 1]) {
                cnt1++;
            }
            if (i < nums.size() - 2 && nums[i] > nums[i + 2]) {
                cnt2++;
            }

            if (cnt1 == 2 || cnt2 == 2) {
                return false;
            }
        }

        return true;
    }
};