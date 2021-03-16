class Solution {
public:
    vector<vector<int>> matrixReshape(vector<vector<int>>& nums, int r, int c) {
        int row = nums.size(), col = nums[0].size(), index, ii, jj;
        if (row * col != r * c) {
            return nums;
        }
        vector<vector<int>> ret(r, vector<int>(c, 0));
        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                index = i * col + j;
                ii = index / c;
                jj = index % c;
                ret[ii][jj] = nums[i][j];
            }
        }
        return ret;
    }
};