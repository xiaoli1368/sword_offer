class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        vector<int> ret;
        int row = matrix.size(), col = matrix[0].size();
        int top = 0, left = 0, bottom = row - 1, right = col - 1;
        while (top <= bottom && left <= right) {
            for (int i = left; i <= right; i++) {
                ret.push_back(matrix[top][i]);
            }
            for (int i = top + 1; i <= bottom; i++) {
                ret.push_back(matrix[i][right]);
            }
            if (top != bottom) {
                for (int i = right - 1; i >= left; i--) {
                    ret.push_back(matrix[bottom][i]);
                }
            }
            if (left != right) {
                for (int i = bottom - 1; i > top; i--) {
                    ret.push_back(matrix[i][left]);
                }
            }
            top++, left++, bottom--, right--;
        }
        return ret;
    }
};