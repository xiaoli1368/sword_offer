class Solution {
public:
    int minOperations(vector<int>& nums1, vector<int>& nums2) {
        int len1 = nums1.size(), len2 = nums2.size();
        if (max(len1, len2) > 6 * min(len1, len2)) {
            return -1;
        }

        int sum1 = accumulate(nums1.begin(), nums1.end(), 0);
        int sum2 = accumulate(nums2.begin(), nums2.end(), 0);
        int diff = (sum1 > sum2 ? sum1 - sum2 : sum2 - sum1);
        if (sum1 > sum2) {
            swap(nums1, nums2);
        }

        unordered_map<int, int> dict;
        for (const int& val : nums1) {
            if (val <= 5) {
                dict[6 - val] += 1;
            }
        }
        for (const int& val : nums2) {
            if (val >= 2) {
                dict[val - 1] += 1;
            }
        }

        int ret = 0, curr_diff = 5;
        while (diff > 0) {
            if (dict[curr_diff] > 0) {
                ret += 1;
                diff -= curr_diff;
                dict[curr_diff] -= 1;
            } else {
                curr_diff -= 1;
            }
        }
        return ret;
    }
};