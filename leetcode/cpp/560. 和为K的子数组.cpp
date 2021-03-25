class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        int cnt = 0, ssum = 0;
        unordered_map<int, int> dict;
        dict.insert(make_pair(0, 1));
        for (int i = 0; i < nums.size(); i++) {
            ssum += nums[i];
            if (dict.count(ssum - k)) {
                cnt += dict[ssum - k];
            }
            dict[ssum] += 1;
        }
        return cnt;
    }
};