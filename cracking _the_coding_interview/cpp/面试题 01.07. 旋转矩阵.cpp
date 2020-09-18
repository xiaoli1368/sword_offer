class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        if (matrix.empty()) {
            return;
        }

        int k = 1; // 表示从外往里的第k层
        int size = matrix.size();

        while (size >= 2 * k) {
            int top = k - 1;
            int left = k - 1;
            int bottom = size - k;
            int right = size - k;
            for (int i = 0; i < right - left; i++) {
                int tmp = matrix[top][left + i];
                matrix[top][left + i] = matrix[bottom - i][left];
                matrix[bottom - i][left] = matrix[bottom][right - i];
                matrix[bottom][right - i] = matrix[top + i][right];
                matrix[top + i][right] = tmp;
            }
            k += 1;
        }

        return;
    }
};