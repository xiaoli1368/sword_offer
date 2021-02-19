class Solution {
public:
    int longestOnes(vector<int>& A, int K) {
        int ret = 0, l = -1;
        for (int h = 0; h < A.size(); h++) {
            // 区间满足条件，则更新状态
            if (A[h] == 1 || K > 0) {
                ret = max(ret, h - l);
                if (A[h] == 0) K -= 1;
                continue;
            }
            // 区间不满足条件，则滑动l来抵消一个0
            while (l++ < h && A[l] != 0);
        }
        return ret;
    }
};