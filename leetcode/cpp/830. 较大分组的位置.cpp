class Solution {
public:
    vector<vector<int>> largeGroupPositions(string s) {
        // 特殊情况
        int n = s.size();
        vector<vector<int>> ret;
        if (n < 3) {
            return ret;
        }

        // 滑窗法
        int l = 0, h = 0;
        while (h < n) {
            // 移动右指针
            while (h + 1 < n && s[l] == s[h + 1]) {
                h += 1;
            }
            // 保存结果
            if (h - l >= 2) {
                ret.push_back(vector<int>{l, h});
            }
            // 移动左右指针 
            h += 1;
            l = h;
        }
        return ret;
    }
};