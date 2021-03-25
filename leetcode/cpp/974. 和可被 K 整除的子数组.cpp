class Solution {
public:
    int subarraysDivByK(vector<int>& nums, int k) {
        int cnt = 0, ssum = 0, mod = 0;
        unordered_map<int, int> d;
        d.insert(make_pair(0, 1));
        for (int i = 0; i < nums.size(); i++) {
            ssum += nums[i];
            mod = (ssum % k + k) % k; // 取模为负数的进行纠正
            cnt += d[mod];
            d[mod] += 1;
        }
        return cnt;
    }
};