class Solution {
public:
    int numberOfSubarrays(vector<int>& nums, int k) {
        int cnt = 0, ssum = 0;
        unordered_map<int, int> d;
        d.insert(make_pair(0, 1));
        for (const int& num : nums) {
            if (num % 2 == 1) {
                ssum += 1;
            }
            if (d.count(ssum - k) > 0) {
                cnt += d[ssum - k];
            }
            d[ssum] += 1;
        }
        return cnt;
    }
};