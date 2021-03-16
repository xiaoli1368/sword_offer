class Solution {
public:
    void tryToAdd(vector<vector<int>>& ret, int& R, int& C, int& x, int& y) {
        if (x >= 0 && y >= 0 && x < R && y < C) {
            ret.push_back(vector<int>{x, y});
        }
    }

    vector<vector<int>> spiralMatrixIII(int R, int C, int r0, int c0) {
        vector<vector<int>> ret;
        int top = r0, bottom = r0, left = c0, right = c0;
        while (ret.size() < R * C) {
            for (int i = (right++, left); i < right; i++) {
                tryToAdd(ret, R, C, top, i);
            }
            for (int i = (bottom++, top); i < bottom; i++) {
                tryToAdd(ret, R, C, i, right);
            }
            for (int i = (left--, right); i > left; i--) {
                tryToAdd(ret, R, C, bottom, i);
            }
            for (int i = (top--, bottom); i > top; i--) {
                tryToAdd(ret, R, C, i, left);
            }
        }
        return ret;
    }
};