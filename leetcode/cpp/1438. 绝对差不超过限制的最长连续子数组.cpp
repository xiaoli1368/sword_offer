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
};