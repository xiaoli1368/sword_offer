class Solution {
public:
    // 交换函数
    void swap(std::vector<std::vector<int>>& vec, int a, int b) {
        auto tmp = vec[a];
        vec[a] = vec[b];
        vec[b] = tmp;
    }

    // 获取点到原点的距离平方
    int getDistance(std::vector<int>& point) {
        return point[0]*point[0] + point[1]*point[1];
    }

    // 堆化函数，小顶堆
    void heapify(std::vector<std::vector<int>>& vec, int n, int i) {
        int largest = i;
        int l = 2 * i + 1;
        int r = 2 * i + 2;
        if (l < n && getDistance(vec[l]) < getDistance(vec[largest])) {
            largest = l;
        }
        if (r < n && getDistance(vec[r]) < getDistance(vec[largest])) {
            largest = r;
        }
        if (largest != i) {
            swap(vec, i, largest);
            heapify(vec, n, largest);
        }
    }

    vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
        // 特殊情况
        if (k <= 0 || k > points.size()) {
            return std::vector<std::vector<int>>{};
        }

        // 建立小顶堆
        int n = points.size();
        for (int i = n/2-1; i >= 0; i--) {
            heapify(points, n, i);
        }

        // 获取topk，移动前k小到末尾，末尾最小
        for (int i = n - 1; i >= n - k; i--) {
            swap(points, 0, i);
            heapify(points, i, 0);
        }

        // 获取结果
        std::vector<std::vector<int>> ret;
        for (int i = 0; i < k; i++) {
            ret.push_back(points[n - 1 - i]);
        }
        return ret;
    }

	// ===== 另一种方式（快排）=====
    // 快排递归函数
    void quickSort(std::vector<std::vector<int>>& vec, int l, int h) {
        if (l >= h) {
            return;
        }
        int m = partition(vec, l, h);
        quickSort(vec, l, m - 1);
        quickSort(vec, m + 1, h);
        return;
    }

    vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
        // 特殊情况
        if (k <= 0 || k > points.size()) {
            return std::vector<std::vector<int>>{};
        }

        // 二分得到topk，索引为k-1，找到后排序
        int l = 0, h = points.size() - 1;
        while (l <= h) {
            int m = partition(points, l, h);
            if (m == k - 1) {
                quickSort(points, 0, k - 1);
                break;
            } else if (m > k - 1) {
                h = m - 1;
            } else if (m < k - 1) {
                l = m + 1;
            }
        }

        // 获取结果
        std::vector<std::vector<int>> ret;
        for (int i = 0; i < k; i++) {
            ret.push_back(points[i]);
        }
        return ret;
    }
};