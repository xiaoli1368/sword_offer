class Solution {
public:
    int longestSubsequence(vector<int>& arr, int difference) {
        int ret = 0, last;
        unordered_map<int, int> d;
        for (const auto & num : arr) {
            last = num - difference;
            d[num] = (d.count(last) == 0 ? 1 : 1 + d[last]);
            ret = max(ret, d[num]);
        }
        return ret;
    }
};