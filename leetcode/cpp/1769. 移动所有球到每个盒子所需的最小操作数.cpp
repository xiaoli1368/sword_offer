class Solution {
public:
    // 思路:
    //     小球只能移动到相邻的盒子中，因此要将所有的小球移动到box[i]处分两个步骤：
    //     将左侧所有移动到box[i-1], 将右侧所有移动到box[i+1], 然后二者分别移动到box[i]
    //     整体上看是一个前缀和的题目，从左到右遍历一次，从右往左再遍历一次，然后对应位置累加
    //     但是考虑递推关系，也有点动态规划内味儿了
    // DP:
    //     dp[i]表示[:i]上的小球汇总到i处的操作数，ssum表示[:i-1]的小球总和
    //     dp[i] = dp[i - 1] + ssum，同理右侧
    // 示意:
    //     ====================
    //         0  0  1  0  1  1
    //     左  0  0  0  1  2  4
    //     右  11 8  5  3  1  0 
    //     和  11 8  5  4  3  4
    //     ====================
    // 优化:
    //     由于dp只和相邻的左侧或者右侧有关，因此可以使用变量迭代进行空间压缩
    //     sum表示一侧的元素前缀和，opt表示一侧的操作数前缀和
    //     最终的复杂度为：O(2n) + O(n)
    vector<int> minOperations(string boxes) {
        int n = boxes.size();
        int left_sum = 0, left_opt = 0, right_sum = 0, right_opt = 0;
        vector<int> dp(n, 0);
        for (int j, i = 0; i < n; i++) {
            // 左侧
            left_opt += left_sum;
            left_sum += (boxes[i] == '1' ? 1 : 0);
            dp[i] += left_opt;
            // 右侧
            j = n - 1 - i;
            right_opt += right_sum;
            right_sum += (boxes[j] == '1' ? 1 : 0);
            dp[j] += right_opt;
        }
        return dp;
    }
};