class Solution {
public:
    // 类内全局变量
    int cnt = 0;
    long lower = lower;
    long upper = upper;

    // 归并合并函数
    void merge(vector<long>& vec, int l, int m, int h) {
        // 统计区间个数，[left, right)
        int left = m + 1, right = m + 1;
        for (int i = l; i <= m; i++) {
            while (left <= h && vec[left] - vec[i] < lower) {
                left += 1;
            }
            while (right <= h && vec[right] - vec[i] <= upper) {
                right += 1;
            }
            // 累加
            cnt += right - left;
            //printf("%d, %d, %d\n", left, right, right - left);
        }
        // 排序
        long* tmp = new long[h - l + 1];
        for (int i = l; i <= h; i++) {
            tmp[i - l] = vec[i];
        }
        int p = l, q = m + 1;
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
    void mergeSort(vector<long>& vec, int l, int h) {
        if (l >= h) {
            return;
        }
        int m = l + (h - l) / 2;
        mergeSort(vec, l, m);
        mergeSort(vec, m + 1, h);
        merge(vec, l, m, h);
        return;
    }

    // 主函数
    int countRangeSum(vector<int>& nums, int lower, int upper) {
        if (nums.empty()) {
            return 0;
        }
        // 一维前缀和，注意使用long，不然会溢出报错
        vector<long> vec(nums.size() + 1, 0);
        for (int i = 1; i < vec.size(); i++) {
            vec[i] = vec[i - 1] + nums[i - 1];
        }
        // 归并并且得出结果
        this->lower = lower;
        this->upper = upper;
        mergeSort(vec, 0, vec.size() - 1);
        return cnt;
    }
};