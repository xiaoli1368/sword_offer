#include <stdio.h>
#include <vector>
#include <algorithm>

#define MAX(x, y) ((x) > (y) ? (x) : (y))
#define MIN(x, y) ((x) < (y) ? (x) : (y))
#define MAX_INT 0x7fffffff
#define MIN_INT 0x80000000

class Solution {
public:
    // 直接合并，排序，寻找中位数
    double findMedianSortedArray1(std::vector<int>& nums1, std::vector<int>& nums2) {
        int length = nums1.size() + nums2.size();
        std::vector<int> nums3 = nums1;
        nums3.insert(nums3.end(), nums2.begin(), nums2.end());
        sort(nums3.begin(), nums3.end());
        if (length % 2 == 1) {
            return nums3[length / 2];
        } else {
            return (nums3[length / 2] + nums3[length / 2 - 1]) / 2.0;
        }
    }

    // 归并排序，得到前k个有序元素，寻找中位数
    double findMedianSortedArray2(std::vector<int>& nums1, std::vector<int>& nums2) {
        int s1 = nums1.size(), s2 = nums2.size();
        int length = s1 + s2;
        int* tmp = new int[length / 2 + 1];
        int p = 0, q = 0;
        for (int i = 0; i < length / 2 + 1; i++) {
            if (p < s1 && (q >= s2 || nums1[p] <= nums2[q])) {
                tmp[i] = nums1[p++];
            } else {
                tmp[i] = nums2[q++];
            }
        }
        if (length % 2 == 1) {
            return tmp[length / 2];
        } else {
            return (tmp[length / 2] + tmp[length / 2 - 1]) / 2.0;
        }
    }

    // 归并排序，使用计数，保存两个值即可
    double findMedianSortedArray3(std::vector<int>& nums1, std::vector<int>& nums2) {
        int curr, left, right, p = 0, q = 0, cnt = 0;
        int s1 = nums1.size(), s2 = nums2.size();
        int length = s1 + s2;
        for (int i = 0; i < length / 2 + 1; i++) {
            cnt += 1;
            if (p < s1 && (q >= s2 || nums1[p] <= nums2[q])) {
                curr = nums1[p++];
            } else {
                curr = nums2[q++];
            }
            if (cnt == length / 2) {
                left = curr;
            } else if (cnt == length / 2 + 1) {
                right = curr;
            }
        }
        if (length % 2 == 1) {
            return right;
        } else {
            return (left + right) / 2.0;
        }
    }

    // 找到两个有序数组中的topk小元素
    // 不断二分，更新当前的index，注意k也在更新
    // index的含义：指向当前数组某位置的指针，同时表面之前的元素都不会是topk小，被排除了
    int getKth(std::vector<int>& nums1, std::vector<int>& nums2, int m, int n, int k) {
        int index1 = 0, index2 = 0, newIndex1, newIndex2;
        while (1) {
            // 特殊情况
            if (index1 == m) {
                return nums2[index2 + k - 1];
            }
            if (index2 == n) {
                return nums1[index1 + k - 1];
            }
            if (k == 1) {
                return MIN(nums1[index1], nums2[index2]);
            }
            // 正常情况，二分然后缩小区间
            newIndex1 = MIN(index1 + k / 2 - 1, m - 1);
            newIndex2 = MIN(index2 + k / 2 - 1, n - 1);
            if (nums1[newIndex1] <= nums2[newIndex2]) {
                k -= newIndex1 - index1 + 1;
                index1 = newIndex1 + 1;
            } else {
                k -= newIndex2 - index2 + 1;
                index2 = newIndex2 + 1;
            }
        }
    }

    // 二分法
    double findMedianSortedArray4(std::vector<int>& nums1, std::vector<int>& nums2) {
        int m = nums1.size();
        int n = nums2.size();
        int length = m + n;
        int left, right;
        left = getKth(nums1, nums2, m, n, (length + 1) / 2);
        if (length % 2 == 1) {
            right = left;
        } else {
            right = getKth(nums1, nums2, m, n, (length + 2) / 2);
        }
        return (left + right) / 2.0;
    }

    // 更加高效的二分法
    double findMedianSortedArray5(std::vector<int>& nums1, std::vector<int>& nums2) {
        // 保证长度大小关系
        if (nums1.size() > nums2.size()) {
            return findMedianSortedArray5(nums2, nums1);
        }
        // 初始化
        int m = nums1.size(), n = nums2.size();
        int left = 0, right = m;
        int median1 = 0, median2 = 0;
        // 主循环
        while (left <= right) {
            int i = (left + right + 1) / 2;
            int j = (m + n + 1) / 2 - i;
            int nums_im1 = (i == 0 ? MIN_INT : nums1[i - 1]);
            int nums_i = (i == m ? MAX_INT : nums1[i]);
            int nums_jm1 = (j == 0 ? MIN_INT : nums2[j - 1]);
            int nums_j = (j == n ? MAX_INT : nums2[j]);
            if (nums_im1 <= nums_j) {
                median1 = MAX(nums_im1, nums_jm1);
                median2 = MIN(nums_i, nums_j);
                left = i + 1;
            } else {
                right = i - 1;
            }
        }
        // 输出结果
        return (m + n % 2 == 1) ? median1 : (median1 + median2) / 2.0;
    }

	// 更加简洁的方法（以下建议全文背诵）
	double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        // 保证先小后大的顺序
        int n1 = nums1.size();
        int n2 = nums2.size();
        if (n1 > n2) {
            return findMedianSortedArrays(nums2, nums1);
        }

        // 初始化并进行二分
        int l = 0, h = n1, m1, m2;
        int k = (n1 + n2 + 1) / 2;
        while (l < h) {
            m1 = l + (h - l) / 2;
            m2 = k - m1;
            if (nums1[m1] < nums2[m2 - 1]) {
                l = m1 + 1;
            } else {
                h = m1;
            }
        }
        m1 = l;
        m2 = k - l;

        // 获取中间的两个元素
        int left1 = (m1 > 0 ? nums1[m1 - 1] : INT_MIN);
        int left2 = (m2 > 0 ? nums2[m2 - 1] : INT_MIN);
        int right1 = (m1 < n1 ? nums1[m1] : INT_MAX);
        int right2 = (m2 < n2 ? nums2[m2] : INT_MAX);
        int left = max(left1, left2);
        int right = min(right1, right2);

        // 更加总元素个数，返回结果
        return (n1 + n2) % 2 == 1 ? left : (left + right) / 2.0;
    }
};

int main(int argc, char* argv[])
{
    Solution s;
    std::vector<int> nums1 = {1, 2};
    std::vector<int> nums2 = {3, 4};
    printf("%f\n", s.findMedianSortedArray1(nums1, nums2));
    printf("%f\n", s.findMedianSortedArray2(nums1, nums2));
    printf("%f\n", s.findMedianSortedArray3(nums1, nums2));
    printf("%f\n", s.findMedianSortedArray4(nums1, nums2));
    printf("%f\n", s.findMedianSortedArray5(nums1, nums2));
    return 0;
}