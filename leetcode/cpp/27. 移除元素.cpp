class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int l = 0;
        int h = nums.size() - 1;
        while (l <= h) {
            if (nums[l] != val) {
                l++;
                continue;
            }
            if (nums[h] == val) {
                h--;
                continue;
            }
            swap(&nums[l], &nums[h]);
            l++;
            h--;
        }

        return h + 1;
    }

    void swap(int* a, int* b) {
        int tmp = *a;
        *a = *b;
        *b = tmp;
    }

    // ===== 快排分区 =====
    inline void swap(vector<int>& vec, int a, int b) {
        int tmp = vec[a];
        vec[a] = vec[b];
        vec[b] = tmp;
    }

    int removeElement(vector<int>& nums, int val) {
        if (nums.empty()) {
            return 0;
        }
        int start = -1;
        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] != val && ++start != i) {
                swap(nums, i, start);
            }
        }
        return start + 1;
    }
};
};