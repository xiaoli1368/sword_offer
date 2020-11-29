class Solution {
public:
    // 类内的全局变量
    vector<int> counts;
    vector<int> indexs;

    // 归并函数
    void merge(vector<int>& vec, int l, int m, int h) {
        int* tmp_vec = new int[h - l + 1];
        int* tmp_ind = new int[h - l + 1];
        for (int i = l; i <= h; i++) {
            tmp_vec[i - l] = vec[i];
            tmp_ind[i - l] = indexs[i];
        }
        int p = l, q = m + 1;
        for (int i = l; i <= h; i++) {
            if (p <= m && q <= h && tmp_vec[p - l] > tmp_vec[q - l]) {
                counts[tmp_ind[p - l]] += h - q + 1;
            }
            if (p <= m && (q > h || tmp_vec[p - l] > tmp_vec[q - l])) {
                vec[i] = tmp_vec[p - l];
                indexs[i] = tmp_ind[p - l];
                p += 1;
            } else {
                vec[i] = tmp_vec[q - l];
                indexs[i] = tmp_ind[q - l];
                q += 1;
            }
        }
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

    // 主函数
    vector<int> countSmaller(vector<int>& nums) {
        if (nums.empty()) {
            return counts;
        }
        // 初始化
        for (int i = 0; i < nums.size(); i++) {
            counts.push_back(0);
            indexs.push_back(i);
        }
        // 归并并返回结果
        mergeSort(nums, 0, nums.size() - 1);
        return counts;
    }
};