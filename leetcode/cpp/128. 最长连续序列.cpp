class Solution {
public:
    // 哈希存储当前区间长度
    int longestConsecutive(vector<int>& nums) {
        if (nums.empty()) {
            return 0;
        }

        int ret = 0;
        std::map<int, int> d;

        for (auto & i : nums) {
            if (d.count(i) == 0) {
                int left = (d.count(i - 1) > 0 ? d[i - 1] : 0);
                int right = (d.count(i + 1) > 0 ? d[i + 1] : 0);
                int length = 1 + left + right;
                ret = max(ret, length);
                // 更新字典
                d[i] = d[i - left] = d[i + right] = length;
            }
        }
        return ret;
    }

    // set遍历
    int longestConsecutive(vector<int>& nums) {
        if (nums.empty()) {
            return 0;
        }

        int ret = 0;
        std::unordered_set<int> d(nums.begin(), nums.end());

        for (auto it = d.begin(); it != d.end(); it++) {
            int curr = *it, length = 1;
            if (d.count(curr - 1) == 0) { // 保证从首端开始遍历
                while (d.count(curr + 1) > 0) {
                    curr += 1;
                    length += 1;
                }
                ret = max(ret, length);
            }
        }
        return ret;
    }
};