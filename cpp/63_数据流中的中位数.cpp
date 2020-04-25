#include <algorithm>
class Solution {
public:
    std::vector<int> data;
    
    void Insert(int num) {
        data.push_back(num);
        sort(data.begin(), data.end());
    }

    double GetMedian() {
        int length = data.size();
        if (length == 0) {
            return 0.0;
        }
        
        if (length % 2 == 1) {
            return data[length / 2];
        } else {
            return double(data[length / 2] + data[length / 2 - 1]) / 2;
        }
    }
};

//以下是自行排序的方式：
//二分排序查找比较麻烦，这里没有实现。
class Solution {
public:
    std::vector<int> data;
    
    void Insert(int num) {
        int length = data.size();
        if (length == 0) {
            data.push_back(num);
            return;
        }
        
        int index = 0;
        if (num <= data[0]) {
            index = 0;
        } else if (num >= data[length - 1]) {
            index = length - 1;
        } else {
            for (int i = 0;i < length - 1; i++) {
                if (data[i] <= num && num < data[i + 1]) {
                    index = i + 1;
                    break;
                }
            }
        }
        data.insert(data.begin() + index, num);
    }

    double GetMedian() {
        int length = data.size();
        if (length == 0) {
            return 0.0;
        }
        
        if (length % 2 == 1) {
            return data[length / 2];
        } else {
            return double(data[length / 2] + data[length / 2 - 1]) / 2;
        }
    }
};