class Solution {
public:
    // 交换函数
    void swap(vector<pair<int, char>>& vec, int a, int b) {
        auto tmp = vec[a];
        vec[a] = vec[b];
        vec[b] = tmp;
    }
    
    // 快排分区函数
    int partition(vector<pair<int, char>>& vec, int l, int h) {
        int start = l - 1;
        for (int i = l; i < h; i++) {
            if (vec[i].first > vec[h].first) {
                swap(vec, i, ++start);
            }
        }
        swap(vec, h, ++start);
        return start;
    }

    // 快排
    void quickSort(vector<pair<int, char>>& vec, int l, int h) {
        if (l < h) {
            int m = partition(vec, l, h);
            quickSort(vec, l, m - 1);
            quickSort(vec, m + 1, h);
        }
    }

    // 根据字符出现频率排序
    string frequencySort(string s) {
        // 特殊情况
        if (s.empty()) {
            return s;
        }

        // 统计hash并且
        unordered_map<char, int> d;
        for (const auto & chr : s) {
            d[chr] += 1;
        }

        // 生成新list
        vector<pair<int, char>> vec;
        for (const auto & it : d) {
            vec.push_back(make_pair(it.second, it.first));
        }

        // 进行排序
        quickSort(vec, 0, vec.size() - 1);

        // 返回结果
        string ret;
        for (const auto & p : vec) {
            string tmp(p.first, p.second);
            ret += tmp;
        }
        return ret;
    }

	// ===== 桶排序 =====
    string frequencySort(string s) {
        // 特殊情况
        if (s.empty()) {
            return s;
        }

        // 统计hash以及出现的最大频次
        int max_cnt = 0;
        unordered_map<char, int> d;
        for (const auto & chr : s) {
            max_cnt = max(max_cnt, ++d[chr]);
        }

        // 进行桶排序
        vector<vector<char>> buckets(max_cnt + 1);
        for (const auto & it : d) {
            buckets[it.second].push_back(it.first);
        }

        // 从后往前合并结果
        string ret;
        for (auto cnt = max_cnt; cnt >= 0; cnt--) {
            for (const auto & chr : buckets[cnt]) {
                string tmp(cnt, chr);
                ret += tmp;
            }
        }
        return ret;
    }
};