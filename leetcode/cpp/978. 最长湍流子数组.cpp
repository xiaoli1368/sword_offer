class Solution {
public:
    // 直接使用 last * curr 可能会越界
    int maxTurbulenceSize(vector<int>& arr) {
        int n = arr.size();
        if (n <= 1) {
            return n;
        }

        int l = 0, last = 0, ret = 1, curr;

        for (int h = 1; h < n; h++) {
            curr = arr[h] - arr[h - 1];
            if ((last > 0 && curr < 0) || (last < 0 && curr > 0) || (last == 0 && curr != 0)) {
                ret = max(ret, h - l + 1);
            } else {
                l = (curr == 0 ? h : h - 1);
            }
            last = curr;
        }
        return ret;
    }
};