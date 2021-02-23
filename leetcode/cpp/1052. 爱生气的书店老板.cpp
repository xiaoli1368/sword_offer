class Solution {
public:
    // 固定滑窗统计两个数量即可
    // 一方面统计所有本来就不生气的累加和
    // 另一方面统计长度为x的窗口中最大可以挽回的累加和
    int maxSatisfied(vector<int>& customers, vector<int>& grumpy, int x) {
        // 特殊情况
        if (customers.empty() && grumpy.empty() && x < 0) {
            return 0;
        }

        // 滑窗法[low, high]
        int l = 0, ssum = 0, curr_extra = 0, max_extra = 0;
        for (int h = 0; h < grumpy.size(); h++) {
            if (h - l >= x) { // 安抚老板的技巧已过期？问题不大，进行滑窗。
                if (grumpy[l] == 1) {
                    curr_extra -= customers[l];
                }
                l += 1;
            }
            if (grumpy[h] == 0) { // 老板不生气？那感情好，直接累加。
                ssum += customers[h];
            } else { // 老板生气？不慌，我事先准备好了技巧，累加到额外统计。
                curr_extra += customers[h];
                max_extra = max(max_extra, curr_extra);
            }
        }
        return ssum + max_extra;
    }
};