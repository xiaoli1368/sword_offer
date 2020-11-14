class Solution {
public:
    // 交换函数
    void swap(vector<int>& vec, int a, int b) {
        int tmp = vec[a];
        vec[a] = vec[b];
        vec[b] = tmp;
    }

    // 归并合并函数
    void merge(vector<int>& vec, map<int, int>& d, int l, int m, int h) {
        vector<int> tmp(h - l + 1);
        for (int i = l; i <= h; i++) {
            tmp[i - l] = vec[i];
        }
        int p = l, q = m + 1;
        for (int i = l; i <= h; i++) {
            // 事先生成不越界情况下的中间值
            bool s1, s2, s3;
            if (p <= m && q <= h) {
                int vp = tmp[p - l];
                int vq = tmp[q - l];
                s1 = d.count(vp) && d.count(vq) && d[vp] < d[vq];
                s2 = d.count(vp) && !d.count(vq);
                s3 = !d.count(vp) && !d.count(vq) && vp < vq;
            }
            if (p <= m && (q > h || s1 || s2 || s3)) {
                vec[i] = tmp[p - l];
                p += 1;
            } else {
                vec[i] = tmp[q - l];
                q += 1;
            }
        }
        return;
    }

    // 归并内部递归函数
    void mergeSort(vector<int>& vec, map<int, int>& d, int l, int h) {
        if (l >= h) {
            return;
        }
        int m = l + (h - l) / 2;
        mergeSort(vec, d, l, m);
        mergeSort(vec, d, m + 1, h);
        merge(vec, d, l, m, h);
        return;
    }

    // 归并排序
    vector<int> relativeSortArray(vector<int>& arr1, vector<int>& arr2) {
        if (arr1.empty()) {
            return arr1;
        }

        // 构建哈希表
        map<int, int> d;
        for (int i = 0; i < arr2.size(); i++) {
            d[arr2[i]] = i;
        }

        // 归并排序并输出
        mergeSort(arr1, d, 0, arr1.size() - 1);
        return arr1;
    }

	// ===== 其它方法后续有空再添加 =====
};