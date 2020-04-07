// 折半查找，递归，注意特殊情况，以及返回值

#include <iostream>
#include <vector>

class Solution {
public:
    int minNumberInRotateArray(std::vector<int> array) {
        int length = array.size();
        if (length == 0) {
            return 0;
        }
        for (int i = 0; i < length - 1; i++) {
            if (array[i] > array[i + 1]) {
                return array[i + 1];
            }
        }
        return array[0];
    }

    // 正常的二分查找最小值
    int minNumber(std::vector<int> array, int low, int high) {
        int tmp = array[low];
        for (int i = low; i <= high; i++) {
            if (array[i] < tmp) {
                tmp = array[i];
            }
        }
        return tmp;
    }

    int minNumberInRotateArray2(std::vector<int> array) {
        int length = array.size();
        if (array.size() == 0) {
            return 0;
        }

        // 进行二分查找
        int low = 0;
        int high = length - 1;
        while (low < high) {
            int middle = (low + high) / 2;
            // 考虑特殊情况
            if (array[low] == array[middle] && array[middle] == array[high]) {
                return minNumber(array, low, high);

            }
            else if (array[middle] <= array[high]) {
                high = middle;
            } else {
                low = middle + 1;
            }
        }
        return array[low];
    }

};

int main(int argc, char* argv[])
{
    std::vector<int> vec = {3, 4, 5, 1, 2};
    //std::vector<int> vec = {1, 1, 1, 0, 1};

    Solution s;
    int result = s.minNumberInRotateArray2(vec);


    std::cout << result << std::endl;

    return 0;
}