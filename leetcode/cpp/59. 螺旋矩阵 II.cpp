class Solution {
public:
    vector<vector<int>> generateMatrix(int n) {
        vector<vector<int>> ret(n, vector<int>(n, n * n));
        int cnt = 0, top = 0, left = 0, bottom = n - 1, right = n - 1;
        while (top < bottom && left < right) {
            for (int i = left; i < right; i++) {
                ret[top][i] = ++cnt;
            }
            for (int i = top; i < bottom; i++) {
                ret[i][right] = ++cnt;
            }
            for (int i = right; i > left; i--) {
                ret[bottom][i] = ++cnt;
            }
            for (int i = bottom; i > top; i--) {
                ret[i][left] = ++cnt;
            }
            top++, left++, bottom--, right--;
        }
        return ret;
    }
};