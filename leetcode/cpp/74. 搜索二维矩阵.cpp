class Solution {
public:
    int binarySearch(const vector<vector<int>>& matrix, int target, int index, int axis) {
        if (index < 0) {
            return index;
        }
        int l = 0, h = (axis == 0 ? matrix.size() : matrix[0].size()) - 1;
        while (l <= h) {
            int m = (l + h + 1) / 2;
            int val = (axis == 0 ? matrix[m][index] : matrix[index][m]);
            if (val > target) {
                h = m - 1;
            } else {
                l = m;
                if (l == h) {
                    break;
                }
            }
        }
        return h;
    }

    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int row = binarySearch(matrix, target, 0, 0);
        int col = binarySearch(matrix, target, row, 1);
        return row >= 0 && col >= 0 && matrix[row][col] == target;
    }

	// ===== 优化方法 =====
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int row = matrix.size(), col = matrix[0].size();
        int l = 0, h = row * col - 1, m, val;
        while (l <= h) {
            m = l + (h - l) / 2;
            val = matrix[m/col][m%col];
            if (val == target) {
                return true;
            } else if (val > target) {
                h = m - 1;
            } else {
                l = m + 1;
            }
        }
        return false;
    }
};