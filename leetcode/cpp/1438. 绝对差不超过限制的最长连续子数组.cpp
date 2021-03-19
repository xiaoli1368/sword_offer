class Solution {
public:
    int longestSubarray(vector<int>& nums, int limit) {
        if (nums.empty() || limit < 0) {
            return 0;
        }

        // 初始化双端队列：[front, back]
        // 三个涉及的操作：push_back, pop_back, pop_front()，头部是极值
        int maxLen = 0, l = -1;
        deque<int> maxq, minq;

        for (int h = 0; h < nums.size(); h++) {
            while (!minq.empty() && minq.back() > nums[h]) {
                minq.pop_back();
            }
            while (!maxq.empty() && maxq.back() < nums[h]) {
                maxq.pop_back();
            }
            minq.push_back(nums[h]);
            maxq.push_back(nums[h]);
            while (l < h && maxq.front() - minq.front() > limit) {
                l += 1;
                if (nums[l] == maxq.front()) {
                    maxq.pop_front();
                }
                if (nums[l] == minq.front()) {
                    minq.pop_front();
                }
            }
            maxLen = max(maxLen, h - l);
        }
        return maxLen;
    }

    // ===== 优化版 =====
    int longestSubarray(vector<int>& nums, int limit) {
        int l = 0, ret = 0;
        deque<int> mindq, maxdq;
        for (int h = 0; h < nums.size(); h++) {
            while (!mindq.empty() && mindq.back() > nums[h]) {
                mindq.pop_back();
            }
            while (!maxdq.empty() && maxdq.back() < nums[h]) {
                maxdq.pop_back();
            }
            mindq.push_back(nums[h]);
            maxdq.push_back(nums[h]);
            while (l < h && maxdq.front() - mindq.front() > limit) {
                if (nums[l] == mindq.front()) {
                    mindq.pop_front();
                }
                if (nums[l] == maxdq.front()) {
                    maxdq.pop_front();
                }
                l += 1;
            }
            ret = max(ret, h - l + 1);
        }
        return ret;
    }
};