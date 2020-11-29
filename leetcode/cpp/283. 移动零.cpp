class Solution {
public:
    inline void swap(vector<int>& vec, int a, int b) {
        int tmp = vec[a];
        vec[a] = vec[b];
        vec[b] = tmp;
    }

    void moveZeroes(vector<int>& nums) {
        if (nums.empty()) {
            return;
        }
        int start = -1;
        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] != 0 && ++start != i) {
                swap(nums, i, start);
            }
        }
        return;
    }
};