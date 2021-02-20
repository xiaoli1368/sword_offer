template <class T>
inline T Max(T a, T b) {
    return a > b ? a : b;
}

template <class T>
inline T Min(const T& a, const T& b, const T& c) {
    T tmp = a < b ? a : b;
    return tmp < c ? tmp : c;
}

class Solution {
public:
    int maximalSquare(vector<vector<char>>& matrix) {
        if (matrix.empty() || matrix[0].empty()) {
            return 0;
        }

        int ret = 0;
        int row = matrix.size();
        int col = matrix[0].size();
        vector<vector<int>> dp(row, vector<int>(col, 0));

        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                if (matrix[i][j] == '1') {
                    if (i == 0 || j == 0) {
                        dp[i][j] = 1;
                    } else {
                        dp[i][j] = 1 + Min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]);
                    }
                    ret = Max(ret, dp[i][j] * dp[i][j]);
                }
            }
        }

        return ret;
    }

	// ===== 个人优化版 =====
    inline int min3(const int& a, const int& b, const int& c) {
        return min(a, min(b, c));
    }

    int maximalSquare(vector<vector<char>>& matrix) {
        if (matrix.empty() || matrix[0].empty()) {
            return 0;
        }

        int ret = 0, row = matrix.size(), col = matrix[0].size();
        vector<vector<int>> dp(row, vector<int>(col, 0));

        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                dp[i][j] = (matrix[i][j] == '1' ? 1 : 0);
                if (i > 0 && j > 0 && dp[i][j] == 1) {
                    dp[i][j] = 1 + min3(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]);
                }
                ret = max(ret, dp[i][j] * dp[i][j]);
            }
        }
        return ret;
    }
	
	// ===== 究极优化版 =====
    int maximalSquare(vector<vector<char>>& matrix) {
        if (matrix.empty() || matrix[0].empty()) {
            return 0;
        }

        int ret = 0, row = matrix.size(), col = matrix[0].size();
        vector<vector<int>> dp(row + 1, vector<int>(col + 1, 0));

        for (int i = 1; i <= row; i++) {
            for (int j = 1; j <= col; j++) {
                if (matrix[i-1][j-1] == '1') {
                    dp[i][j] = 1 + min(dp[i-1][j-1], min(dp[i-1][j], dp[i][j-1]));
                }
                ret = max(ret, dp[i][j] * dp[i][j]);
            }
        }
        return ret;
    }
};