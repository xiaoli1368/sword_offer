class Solution {
public:
    int cnt = 0; // 全局变量

    // 归并合并函数
    void merge(vector<int>& vec, int l, int m, int h) {
        // 先统计重要翻转对
        int p = l, q = m + 1;
        while (p <= m && q <= h) {
            //if (vec[p] > 2 * vec[q]) { // 这种写法可能会int溢出
            long pp = vec[p], qq = vec[q];
            if (pp > 2 * qq) {
                cnt += m - p + 1;
                q += 1;
            } else {
                p += 1;
            }
        }
        // 然后合并两个有序数组
        p = l, q = m + 1;
        int* tmp = new int[h - l + 1];
        for (int i = l; i <= h; i++) {
            tmp[i - l] = vec[i];
        }
        for (int i = l; i <= h; i++) {
            if (p <= m && (q > h || tmp[p - l] <= tmp[q - l])) {
                vec[i] = tmp[p - l];
                p += 1;
            } else {
                vec[i] = tmp[q - l];
                q += 1;
            }
        }
        delete [] tmp;
        return;
    }

    // 归并递归函数
    void mergeSort(vector<int>& vec, int l, int h) {
        if (l >= h) {
            return;
        }
        int m = l + (h - l) / 2;
        mergeSort(vec, l, m);
        mergeSort(vec, m + 1, h);
        merge(vec, l, m, h);
        return;
    }

    int reversePairs(vector<int>& nums) {
        if (nums.empty()) {
            return 0;
        }
        mergeSort(nums, 0, nums.size() - 1);
        return cnt;
    }
};