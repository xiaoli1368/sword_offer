class Solution {
public:
    // 计数排序
    void sortColors(vector<int>& nums) {
        if (nums.empty()) {
            return;
        }

        vector<int> cnt(3, 0);
        for (auto & num : nums) {
            cnt[num] += 1;
        }

        int i = 0;
        for (int n = 0; n < cnt.size(); n++) {
            while (cnt[n]) {
                nums[i++] = n; 
                cnt[n]--;
            }
        }
        return;
    }

    // ===== 快排方式 =====

    // 交换函数
    inline void swap(vector<int>& nums, int a, int b) {
        int tmp = nums[a];
        nums[a] = nums[b];
        nums[b] = tmp;
    }

    // 快排分区法
    void sortColors(vector<int>& nums) {
        if (nums.empty()) {
            return;
        }

        int p0 = -1;
        int p1 = 0;
        int p2 = nums.size();

        while (p1 < p2) {
            if (nums[p1] == 1 || p1 == p0) {
                p1 += 1;
            } else if (nums[p1] == 0) {
                p0 += 1;
                swap(nums, p0, p1);
            } else if (nums[p1] == 2) {
                p2 -= 1;
                swap(nums, p2, p1);
            }
        }
        return;
	}

    // 两次快排，效率不高
    void sortColors(vector<int>& nums) {
        // 特殊情况
        if (nums.empty()) {
            return;
        }

        // 快排分区
        // 先从左往右遍历，把0放到左侧，然后从右往左遍历，把2放到右侧
        int t0 = -1;
        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] == 0) {
                swap(nums, i, ++t0);
            }
        }

        int t2 = nums.size();
        for (int i = nums.size() - 1; i >= 0; i--) {
            if (nums[i] == 2) {
                swap(nums, i, --t2);
            }
        }

        return;
    }
};