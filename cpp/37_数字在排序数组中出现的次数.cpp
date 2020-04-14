#include <iostream>
#include <vector>

class Solution {
public:
    // 二分查找方法
    int GetNumberOfK(std::vector<int> data ,int k) {
        if (data.empty()) {
            return 0;
        }
        
        // 二分查找是否存在，返回任意一个等于k的索引
        int l = 0;
        int h = data.size() - 1;
        int index = -1;
        while (l <= h) {
            int m = l + (h - l) / 2;
            if (data[m] > k) {
                h = m - 1;
            } else if (data[m] < k) {
                l = m + 1;
            } else if (data[m] == k) {
                index = m;
                break;
            }
        }
        
        // 如果不存在k
        if (index == -1) {
            return 0;
        }
        
        // 如果存在，则从该位置向两端检测出现的次数
        l = index;
        h = index;
        while (data[l] == k || data[h] == k) {
            if (data[l] == k) {
                l--;
            }
            if (data[h] == k) {
                h++;
            }
        }
        
        return h - l - 1;
    }

    // 高效思路，查找[k, k+1]
    int GetNumberOfK2(std::vector<int> data, int k) {
        int first = binarySearch(data, k);
        int last = binarySearch(data, k + 1);
        return (first == data.size() || data[first] != k) ? 0 : last - first;
    }

    // 递归需要调用的函数: 二分查找
    // 返回数组中第一个大于等于k的索引，不存在时返回的是data.size()
    int binarySearch(std::vector<int> data, int k) {
        int l = 0;
        int h = data.size();
        while (l < h) {
            int m = l + (h - l) / 2;
            if (data[m] >= k) {
                h = m;
            } else {
                l = m + 1;
            }
        }
        return l;
    }

};

int main(int argc, char* argv[])
{
    Solution s;
    std::vector<int> vec = {1, 2, 3, 3, 3, 3, 4, 5, 6, 7};

    std::cout << s.GetNumberOfK(vec, 3) << std::endl;
    std::cout << s.GetNumberOfK2(vec, 3) << std::endl;
    return 0;
}