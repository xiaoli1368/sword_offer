class KthLargest {
public:
    // 全局的数据结构
    int k;
    vector<int> vec;
    
    // 初始化
    KthLargest(int k, vector<int>& nums) {
        this->k = k;
        for (const auto & item : nums) {
            add(item);
        }
    }

    // 交换元素
    void swap(int i, int j) {
        int tmp = vec[i];
        vec[i] = vec[j];
        vec[j] = tmp;
    }

    // 添加元素
    void push(int item, bool fromBack=false) {
        if (fromBack) {
            vec.push_back(item);
            _shift_up(vec.size() - 1);
        } else {
            vec[0] = item;
            _shift_down(0);
        }
    }

    // 上浮函数
    void _shift_up(int index) {
        while (index) {
            int parent = (index - 1) / 2;
            if (vec[parent] < vec[index]) {
                break;
            }
            swap(parent, index);
            index = parent;
        }
    }

    // 下沉函数
    void _shift_down(int index) {
        int i = index, n = vec.size();
        while (2 * i + 1 < n) {
            int smallest = i;
            int l = 2 * i + 1;
            int r = 2 * i + 2;
            if (l < n && vec[l] < vec[smallest]) {
                smallest = l;
            }
            if (r < n && vec[r] < vec[smallest]) {
                smallest = r;
            }
            if (smallest != i) {
                swap(i, smallest);
                i = smallest;
            } else {
                break;
            }
        }
    }
    
    int add(int val) {
        if (vec.size() < k) {
            push(val, true);
        } else if (val > vec[0]) {
            push(val, false);
        }
        return (vec.empty() ? -1 : vec[0]);
    }
};

/**
 * Your KthLargest object will be instantiated and called as such:
 * KthLargest* obj = new KthLargest(k, nums);
 * int param_1 = obj->add(val);
 */