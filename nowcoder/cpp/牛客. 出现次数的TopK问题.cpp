class Solution {
public:
    // 交换vec内两个元素的值
    template <class T>
    void swap(vector<T>& vec, int l, int h) {
        T tmp = vec[l];
        vec[l] = vec[h];
        vec[h] = tmp;
    }
    
    // 大顶堆下沉函数，出现次数越多，字典序越小的，放在前面
    void heapify(vector<string>& strs, vector<int>& cnts, int n, int i) {
        int largest = i;
        int l = 2 * i + 1;
        int r = 2 * i + 2;
        if (l < n && (cnts[l] > cnts[largest] || (cnts[l] == cnts[largest] && strs[l] < strs[largest]))) {
            largest = l;
        }
        if (r < n && (cnts[r] > cnts[largest] || (cnts[r] == cnts[largest] && strs[r] < strs[largest]))) {
            largest = r;
        }
        if (largest != i) {
            swap(strs, i, largest);
            swap(cnts, i, largest);
            heapify(strs, cnts, n, largest);
        }
    }
    
    /**
     * return topK string
     * @param strings string字符串vector strings
     * @param k int整型 the k
     * @return string字符串vector<vector<>>
     */
    vector<vector<string> > topKstrings(vector<string>& strings, int k) {
        // write code here
        // 特殊情况
        if (strings.empty() || k <= 0) {
            return vector<vector<string>>{};
        }
        // 确定每个字符串出现的次数
        std::map<std::string, int> map;
        for (auto & s : strings) {
            map[s] += 1;
        }
        // 转换为两个数组，分别存储cnts, strs
        int n = map.size();
        std::vector<int> cnts;
        std::vector<std::string> strs;
        for (auto it = map.begin(); it != map.end(); it++) {
            strs.push_back(it->first);
            cnts.push_back(it->second);
        }
        // 建立大顶堆
        for (int i = n - 1; i >= 0; i--) {
            heapify(strs, cnts, n, i);
        }
        // 进行堆排序，获取前k个元素，搬移到末尾，并保存到ret
        vector<vector<string>> ret;
        for (int i = n - 1; i > n - 1 - k; i--) {
            vector<string> tmp = {strs[0], std::to_string(cnts[0])};
            ret.push_back(tmp);
            swap(strs, 0, i);
            swap(cnts, 0, i);
            heapify(strs, cnts, i, 0);
        }
        // 返回结果
        return ret;
    }
};