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

    // 分区函数
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
};