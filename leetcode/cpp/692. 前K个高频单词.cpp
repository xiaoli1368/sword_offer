class Solution {
public:
    // 自定义类型
    typedef std::vector<std::pair<std::string, int>> numFre;

    // 交换函数
    void swap(numFre& ret, int a, int b) {
        auto tmp = ret[a];
        ret[a] = ret[b];
        ret[b] = tmp;
        return;
    }

    // 快排分区函数
    int partition(numFre& vec, int l, int h) {
        int start = l - 1;
        for (int i = l; i < h; i++) {
            if (vec[i].second > vec[h].second || (vec[i].second == vec[h].second && vec[i].first < vec[h].first)) {
                swap(vec, i, ++start);
            }
        }
        swap(vec, h, ++start);
        return start;
    }

    // 快排递归函数
    void quickSort(numFre& vec, int l, int h) {
        if (l >= h) {
            return;
        }
        int m = partition(vec, l, h);
        quickSort(vec, l, m - 1);
        quickSort(vec, m + 1, h);
        return;
    }

    vector<string> topKFrequent(vector<string>& words, int k) {
        // 生成频次字典
        std::map<std::string, int> map;
        for (auto & word : words) {
            map[word]++;
        }

        // 生成频次二维数组
        numFre vec;
        for (auto it = map.begin(); it != map.end(); it++) {
            vec.push_back(std::make_pair(it->first, it->second));
        }

        // 特殊情况
        if (k <= 0 || k > vec.size()) {
            return std::vector<std::string>{};
        }

        // 二分找到topk，然后排序
        int l = 0, h = vec.size() - 1;
        while (l <= h) {
            int m = partition(vec, l, h);
            if (m == k - 1) {
                quickSort(vec, 0, k - 1);
                break;
            } else if (m > k - 1) {
                h = m - 1;
            } else if (m < k - 1) {
                l = m + 1;
            }
        }

        // 提取topk结果
        std::vector<std::string> ret;
        for (int i = 0; i < k; i++) {
            ret.push_back(vec[i].first);
        }
        return ret;
    }

	// ===== 另一种方式（堆排序）=====
    // 堆化函数，大顶堆
    void heapify(numFre& vec, int n, int i) {
        int largest = i;
        int l = 2 * i + 1;
        int r = 2 * i + 2;
        if (l < n && (vec[l].second > vec[largest].second || (vec[l].second == vec[largest].second && vec[l].first < vec[largest].first))) {
            largest = l;
        }
        if (r < n && (vec[r].second > vec[largest].second || (vec[r].second == vec[largest].second && vec[r].first < vec[largest].first))) {
            largest = r;
        }
        if (largest != i) {
            swap(vec, i, largest);
            heapify(vec, n, largest);
        }
    }

    vector<string> topKFrequent(vector<string>& words, int k) {
        // 生成频次字典
        std::map<std::string, int> map;
        for (auto & word : words) {
            map[word]++;
        }

        // 生成频次二维数组
        numFre vec;
        for (auto it = map.begin(); it != map.end(); it++) {
            vec.push_back(std::make_pair(it->first, it->second));
        }

        // 特殊情况
        if (k <= 0 || k > vec.size()) {
            return std::vector<std::string>{};
        }

        // 建立大顶堆
        int n = vec.size();
        for (int i = n/2-1; i >= 0; i--) {
            heapify(vec, n, i);
        }

        // 获取topk到末尾，末尾最大
        for (int i = n - 1; i >= n - k; i--) {
            swap(vec, 0, i);
            heapify(vec, i, 0);
        }

        // 提取topk结果
        std::vector<std::string> ret;
        for (int i = 0; i < k; i++) {
            ret.push_back(vec[n - 1 - i].first);
        }
        return ret;
    }
};