class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> ret;
        unordered_map<int, int> d;
        for (int i = 0; i < nums.size(); i++) {
            if (d.count(target - nums[i]) > 0) {
                ret.push_back(d[target - nums[i]]);
                ret.push_back(i);
                break;
            }
            d[nums[i]] = i;
        }
        return ret;
    }
};