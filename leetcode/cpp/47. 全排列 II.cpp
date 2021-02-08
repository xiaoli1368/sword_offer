class Solution {
public:
    void swap(vector<int>& vec, int a, int b) {
        int tmp = vec[a];
        vec[a] = vec[b];
        vec[b] = tmp;
    }

    void dfs(vector<vector<int>>& ret, vector<int>& nums, int i) {
        if (i >= nums.size()) {
            ret.push_back(nums);
            return;
        }
        for (int j = i; j < nums.size(); j++) {
            // 需要保证nums[j]没有出现在nums[i:j]中去
            if (find(nums.begin() + i, nums.begin() + j, nums[j]) != nums.begin() + j) {
                continue;
            }
            swap(nums, i, j);
            dfs(ret, nums, i + 1);
            swap(nums, i, j);
        }
        return;
    }

    vector<vector<int>> permuteUnique(vector<int>& nums) {
        vector<vector<int>> ret;
        if (!nums.empty()) {
            sort(nums.begin(), nums.end(), [](int a, int b){return a < b;});
            dfs(ret, nums, 0);
        }
        return ret;
    }
};