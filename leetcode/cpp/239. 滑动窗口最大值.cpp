// 需要复习常用的deque函数：http://c.biancheng.net/view/6860.html
class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        if (nums.empty() || k <= 0 || k > nums.size()) {
            return std::vector<int>{};
        }

        std::vector<int> ret;
        std::deque<int> queue;

        for (int i = 0; i < nums.size(); i++) {
            // 维度队列的单调性
            while (!queue.empty() && nums[queue.back()] < nums[i]) {
                queue.pop_back();
            }
            // 添加当前元素
            queue.push_back(i);
            // 当头部元素滑出窗口时，删除
            if (queue.front() + k <= i) {
                queue.pop_front();
            }
            // 达到窗口大小时，添加到结果
            if (i >= k - 1) {
                ret.push_back(nums[queue.front()]);
            }
        }
        return ret;
    }

	// ===== 优化版 =====
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        deque<int> dq;
        vector<int> ret;
        for (int i = 0; i < nums.size(); i++) {
            while (!dq.empty() && nums[dq.back()] < nums[i]) {
                dq.pop_back();
            }
            dq.push_back(i);
            if (i - dq.front() >= k) {
                dq.pop_front();
            }
            if (i >= k - 1) {
                ret.push_back(nums[dq.front()]);
            }
        }
        return ret;
    }
};