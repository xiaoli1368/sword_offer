class Solution {
public:
    int findPairs(vector<int>& nums, int k) {
        int cnt = 0;
        unordered_map<int, int> d;
        for (const int& curr : nums) {
            if (d.count(curr) > 0 && d[curr] == 1 && k == 0) {
                cnt += 1;
            }
            if (d.count(curr) == 0 && d.count(curr - k) > 0) {
                cnt += 1;
            }
            if (d.count(curr) == 0 && k != 0 && d.count(curr + k) > 0) {
                cnt += 1;
            }
            d[curr] += 1;
        }
        return cnt;
    }
};