class Solution {
public:
    // 获取一个整数的二进制位中1的个数
    int getOnes(int n) {
        int ret = 0;
        while (n != 0) {
            ret += 1;
            n &= n - 1;
        }
        return ret;
    }
    
    // 自定义的排序函数
    static bool compare(std::pair<int, int> a, std::pair<int, int> b) {
        return a.second < b.second || (a.second == b.second && a.first < b.first);
    }

    vector<int> sortByBits(vector<int>& arr) {
        if (arr.empty()) {
            return arr;
        }

        // 生成pair并排序
        std::vector<std::pair<int, int>> tmp;
        for (auto & i : arr) {
            tmp.push_back(std::make_pair(i, getOnes(i)));
        }
        sort(tmp.begin(), tmp.end(), compare);

        // 生成新的arr
        std::vector<int> ret;
        for (auto & i : tmp) {
            ret.push_back(i.first);
        }
        return ret;
    }

	// ===== 另一种方法 =====
	    // 获取一个整数的二进制位中1的个数
    int getOnes(int n) {
        int ret = 0;
        while (n != 0) {
            ret += 1;
            n &= n - 1;
        }
        return ret;
    }

    // 交换vec两个元素的函数
    void swap(vector<int>& vec, int l, int h) {
        int tmp = vec[l];
        vec[l] = vec[h];
        vec[h] = tmp;
    }

    // 快排分区函数
    int partition(vector<int>& vec, vector<int>& ones, int l, int h) {
        int start = l - 1;
        for (int i = l; i < h; i++) {
            if (ones[i] < ones[h] || (ones[i] == ones[h] && vec[i] < vec[h])) {
                start += 1;
                swap(vec, i, start);
                swap(ones, i, start);
            }
        }
        start += 1;
        swap(vec, h, start);
        swap(ones, h, start);
        return start;
    }

    // 快排内部递归函数
    void _quickSort(vector<int>& vec, vector<int>& ones, int l, int h) {
        if (l >= h) {
            return;
        }
        int m = partition(vec, ones, l, h);
        _quickSort(vec, ones, l, m - 1);
        _quickSort(vec, ones, m + 1, h);
        return;
    }
    
    vector<int> sortByBits(vector<int>& arr) {
        if (arr.empty()) {
            return arr;
        }

        // 生成对应1的个数的数组
        std::vector<int> ones;
        for (auto & i : arr) {
            ones.push_back(getOnes(i));
        }

        // 快排内部递归函数
        _quickSort(arr, ones, 0, arr.size() - 1);
        return arr;
    }
};