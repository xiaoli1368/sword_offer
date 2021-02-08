class Solution {
public:
    void dfs(vector<int>& ret, int n, int k, int num, int last, int i) {
        if (n < 2 || k < 0) { // 特殊情况，不满足，直接返回
            return;
        } else if (i > n) { // 满足长度要求，直接添加
            ret.push_back(num);
        } else if (i == 1) { // 其它情况需要向下一层遍历
            for (int j = 1; j <= 9; j++) {
                dfs(ret, n, k, j, j, i + 1);
            }
        } else {
            if (last + k <= 9) {
                dfs(ret, n, k, num * 10 + last + k, last + k, i + 1);
            }
            if (last - k >= 0 && k != 0) {
                dfs(ret, n, k, num * 10 + last - k, last - k, i + 1);
            }
        }
        return;
    }

    vector<int> numsSameConsecDiff(int n, int k) {
        vector<int> ret;
        dfs(ret, n, k, 0, 0, 1);
        return ret;
    }
};