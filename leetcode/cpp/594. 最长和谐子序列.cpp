class Solution {
public:
    int findLHS(vector<int>& nums) {
        int cnt = 0;
        unordered_map<int, int> d;
        for (const int& num : nums) {
            d[num] += 1;
            if (d.count(num + 1) > 0) {
                cnt = max(cnt, d[num] + d[num + 1]);
            }
            if (d.count(num - 1) > 0) {
                cnt = max(cnt, d[num] + d[num - 1]);
            }
        }
        return cnt;
    }
};