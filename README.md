# sword_offer

作者：xiaoli1368
日期：2020/09/16 —— 2021/??/??
邮箱：xiaoli1644@qq.com

## 前言

> 记录个人在找工作时，所刷算法题的汇总，主要使用了Python和C++。

包括五个文件夹：

- sword_offer：《剑指offer》第一版、第二版
- cracking _the_coding_interview：《程序员面试金典》
- leetcode：程序员刷题圣地
- nowcoder：另一个程序员刷题圣地
- codewar：国外的刷题网站
- cheat_sheet：常见算法题的备忘单小抄

后续按照题目类型进行了分类。

## 目录

[TOC]

## 第一部分：数据结构

### 字符串

| 题目链接                                                     | 难度   | 个人题解   | 说明                    |
| ------------------------------------------------------------ | ------ | ---------- | ----------------------- |
| [242. 有效的字母异位词](https://leetcode-cn.com/problems/valid-anagram/) | easy   | cpp,python | 字符串比较，哈希        |
| [205. 同构字符串](https://leetcode-cn.com/problems/isomorphic-strings/) | easy   | cpp,python | 字符串比较，哈希        |
| [647. 回文子串](https://leetcode-cn.com/problems/palindromic-substrings/) | medium | cpp,python | 回文串，中心延拓DP      |
| [409. 最长回文串](https://leetcode-cn.com/problems/longest-palindrome/) | easy   | cpp,python | 回文串，中心延拓DP      |
| [5. 最长回文子串](https://leetcode-cn.com/problems/longest-palindromic-substring/) | medium | cpp,python | 回文串，中心延拓DP      |
| [696. 计数二进制子串](https://leetcode-cn.com/problems/count-binary-substrings/) | easy   | cpp,python | 其它                    |
| [224. 基本计算器](https://leetcode-cn.com/problems/basic-calculator/) | hard   |            | 字符串理解（跳过）      |
| [227. 基本计算器 II](https://leetcode-cn.com/problems/basic-calculator-ii/) | medium |            | 字符串理解（跳过）      |
| 772（基本计算器3，没有权限）                                 | medium |            | 字符串理解（跳过）      |
| [28. 实现 strStr()](https://leetcode-cn.com/problems/implement-strstr/) | easy   |            | 字符串匹配，KMP（跳过） |
| [3. 无重复字符的最长子串](https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/) | medium | cpp,python | 子串，滑窗              |

### 数组

| 题目链接                                                     | 难度   | 个人题解   | 说明     |
| ------------------------------------------------------------ | ------ | ---------- | -------- |
| [448. 找到所有数组中消失的数字](https://leetcode-cn.com/problems/find-all-numbers-disappeared-in-an-array/) | easy   | cpp,python | 原地hash |
| [287. 寻找重复数](https://leetcode-cn.com/problems/find-the-duplicate-number/) | medium | cpp,python | 原地hash |
| [442. 数组中重复的数据](https://leetcode-cn.com/problems/find-all-duplicates-in-an-array/) | medium | cpp,python | 原地hash |
| [41. 缺失的第一个正数](https://leetcode-cn.com/problems/first-missing-positive/) | hard   | cpp,python | 原地hash |
| [48. 旋转图像](https://leetcode-cn.com/problems/rotate-image/) | medium | cpp,python | 二维数组 |
| [54. 螺旋矩阵](https://leetcode-cn.com/problems/spiral-matrix/) | medium | cpp,python | 二维数组 |
| [59. 螺旋矩阵 II](https://leetcode-cn.com/problems/spiral-matrix-ii/) | medium | cpp,python | 二维数组 |
| [885. 螺旋矩阵 III](https://leetcode-cn.com/problems/spiral-matrix-iii/) | medium | cpp,python | 二维数组 |
| [566. 重塑矩阵](https://leetcode-cn.com/problems/reshape-the-matrix/) | easy   | cpp,python | 二维数组 |
| [769. 最多能完成排序的块](https://leetcode-cn.com/problems/max-chunks-to-make-sorted/) | medium | cpp,python | 其它     |

### 前缀和与积分图

| 题目链接                                                     | 难度   | 个人题解   | 说明       |
| ------------------------------------------------------------ | ------ | ---------- | ---------- |
| [303. 区域和检索 - 数组不可变](https://leetcode-cn.com/problems/range-sum-query-immutable/) | easy   | cpp,python | 一维前缀和 |
| [304. 二维区域和检索 - 矩阵不可变](https://leetcode-cn.com/problems/range-sum-query-2d-immutable/) | medium | cpp,python | 二维前缀和 |
| 560                                                          |        |            |            |
| 307                                                          |        |            |            |
| [308. 二维区域和检索 - 可变](https://michael.blog.csdn.net/article/details/107417676?utm_medium=distribute.pc_relevant.none-task-blog-searchFromBaidu-8.control&dist_request_id=&depth_1-utm_source=distribute.pc_relevant.none-task-blog-searchFromBaidu-8.control) | medium | 有思路     | 无权限     |
| [1769. 移动所有球到每个盒子所需的最小操作数](https://leetcode-cn.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/) |        |            |            |

### 栈和队列

| 题目链接                                                     | 难度   | 个人题解   | 说明             |
| ------------------------------------------------------------ | ------ | ---------- | ---------------- |
| [232. 用栈实现队列](https://leetcode-cn.com/problems/implement-queue-using-stacks/) | easy   | cpp,python | 栈与队列         |
| [225. 用队列实现栈](https://leetcode-cn.com/problems/implement-stack-using-queues/) | easy   | cpp,python | 栈与队列         |
| [649. Dota2 参议院](https://leetcode-cn.com/problems/dota2-senate/) | medium | cpp,python | 普通队列         |
| [155. 最小栈](https://leetcode-cn.com/problems/min-stack/)   | easy   | cpp,python | 普通栈           |
| [735. 行星碰撞](https://leetcode-cn.com/problems/asteroid-collision/) | medium | cpp,python | 普通栈           |
| [20. 有效的括号](https://leetcode-cn.com/problems/valid-parentheses/) | easy   | cpp,python | 普通栈，括号匹配 |
| [32. 最长有效括号](https://leetcode-cn.com/problems/longest-valid-parentheses/) | hard   | cpp,python | 普通栈，括号匹配 |
| [496. 下一个更大元素 I](https://leetcode-cn.com/problems/next-greater-element-i/) | easy   | cpp,python | 单调栈           |
| [503. 下一个更大元素 II](https://leetcode-cn.com/problems/next-greater-element-ii/) | medium | cpp,python | 单调栈           |
| [739. 每日温度](https://leetcode-cn.com/problems/daily-temperatures/) | medium | cpp,python | 单调栈           |
| [901. 股票价格跨度](https://leetcode-cn.com/problems/online-stock-span/) | medium | cpp,python | 单调栈           |
| [42. 接雨水](https://leetcode-cn.com/problems/trapping-rain-water/) | hard   | cpp,python | 单调栈           |
| [84. 柱状图中最大的矩形](https://leetcode-cn.com/problems/largest-rectangle-in-histogram/) | hard   | cpp,python | 单调栈           |
| [1793. 好子数组的最大分数](https://leetcode-cn.com/problems/maximum-score-of-a-good-subarray/) | hard   | cpp,python | 单调栈           |
| [239. 滑动窗口最大值](https://leetcode-cn.com/problems/sliding-window-maximum/) | hard   | cpp,python | 双端队列         |
| [1438. 绝对差不超过限制的最长连续子数组](https://leetcode-cn.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/) | medium | cpp,python | 双端队列         |
| 思考单端增长/滑动窗口的最小/大值（单调栈/队列）              |        |            |                  |

**单调栈/队列总结：**

- 求数组内某个元素的 [left, right] 方向下，最近的更 [min, max] 的元素。（使用单调栈）
- 求滑动窗口下的最小值/最大值。（使用双端单调队列）
- 求区间内部所有元素中的最小值/最大值。（使用单调栈）
- 求单端增长的数组的最小值/最大值。（使用单调栈）
- 求区间两端中的最小值/最大值。（使用双指针）

### 堆和优先队列

| 题目链接                                                     | 难度 | 个人题解   | 说明   |
| ------------------------------------------------------------ | ---- | ---------- | ------ |
| 23                                                           |      |            |        |
| 218                                                          |      |            |        |
| 313                                                          |      |            |        |
| [1792. 最大平均通过率](https://leetcode-cn.com/problems/maximum-average-pass-ratio/) |      |            |        |
| [1046. 最后一块石头的重量](https://leetcode-cn.com/problems/last-stone-weight/) | easy | cpp,python | 大顶堆 |
| [堆总结](https://mp.weixin.qq.com/s?__biz=MzI4MzUxNjI3OA==&mid=2247486985&idx=1&sn=4c0275e5ef02e0b9b8e4e99ba57b58dc&chksm=eb88c210dcff4b062cf5d72d86733e7b0ec087adbc714e112db083c683161320e3dcbf1d87f7&token=706287068&lang=zh_CN#rd) |      |            |        |

### 哈希表

| 题目链接                                                     | 难度   | 个人题解   | 说明           |
| ------------------------------------------------------------ | ------ | ---------- | -------------- |
| [697. 数组的度](https://leetcode-cn.com/problems/degree-of-an-array/) | easy   | cpp,python | 哈希           |
| [705. 设计哈希集合](https://leetcode-cn.com/problems/design-hashset/) | easy   | cpp,python | 手写哈希       |
| 1                                                            |        |            |                |
| 128                                                          |        |            |                |
| 149                                                          |        |            |                |
| 217                                                          |        |            |                |
| 697                                                          |        |            |                |
| 594                                                          |        |            |                |
| 287                                                          |        |            |                |
| 332                                                          |        |            | 多重集合和映射 |
| [870. 优势洗牌](https://leetcode-cn.com/problems/advantage-shuffle/) | medium | cpp,python | 普通哈希？     |

### 链表

| 题目链接                                                     | 难度   | 个人题解   | 说明 |
| ------------------------------------------------------------ | ------ | ---------- | ---- |
| [206. 反转链表](https://leetcode-cn.com/problems/reverse-linked-list/) | easy   | cpp,python | 翻转 |
| [92. 反转链表 II](https://leetcode-cn.com/problems/reverse-linked-list-ii/) | medium | cpp,python | 翻转 |
| leetcode143                                                  |        |            |      |
| leetcode148                                                  |        |            |      |
|                                                              |        |            |      |
|                                                              |        |            |      |
|                                                              |        |            |      |
|                                                              |        |            |      |
|                                                              |        |            |      |

### 树

| 题目链接                                                     | 难度   | 个人题解   | 说明 |
| ------------------------------------------------------------ | ------ | ---------- | ---- |
| [331. 验证二叉树的前序序列化](https://leetcode-cn.com/problems/verify-preorder-serialization-of-a-binary-tree/) | medium | cpp,python | 堆栈 |

23.二叉树查找两个节点的最近公共祖先。
（如果是二叉搜索树，怎么查找最近公共祖先。）
（见236. 二叉树的最近公共祖先）
（根据递归去做）
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        if root == None or root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if not left: return right
        if not right: return left
        return root

### 图

| 题目链接                                                     | 难度 | 个人题解 | 说明   |
| ------------------------------------------------------------ | ---- | -------- | ------ |
| [765. 情侣牵手](https://leetcode-cn.com/problems/couples-holding-hands/) |      |          | 并查集 |

### 更加复杂的数据结构

## 第二部分：算法

### 贪心

| 题目链接                                                     | 难度   | 个人题解    | 说明     |
| ------------------------------------------------------------ | ------ | ----------- | -------- |
| [605. 种花问题](https://leetcode-cn.com/problems/can-place-flowers/) | easy   | cpp, python | 分配问题 |
| [135. 分发糖果](https://leetcode-cn.com/problems/candy/)     | hard   | cpp, python | 分配问题 |
| [455. 分发饼干](https://leetcode-cn.com/problems/assign-cookies/) | easy   | cpp, python | 分配问题 |
| [435. 无重叠区间](https://leetcode-cn.com/problems/non-overlapping-intervals/) | medium | cpp,python  | 区间问题 |
| [452. 用最少数量的箭引爆气球](https://leetcode-cn.com/problems/minimum-number-of-arrows-to-burst-balloons/) | medium | cpp,python  | 区间问题 |
| [763. 划分字母区间](https://leetcode-cn.com/problems/partition-labels/) | medium | cpp,python  | 区间问题 |
| [122. 买卖股票的最佳时机 II](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/) | easy   | cpp,python  | 其它     |
| [665. 非递减数列](https://leetcode-cn.com/problems/non-decreasing-array/) | easy   | cpp,python  | 其它     |
| [406. 根据身高重建队列](https://leetcode-cn.com/problems/queue-reconstruction-by-height/) | medium | cpp,python  | 其它     |
| [300. 最长递增子序列](https://leetcode-cn.com/problems/longest-increasing-subsequence/) | medium | cpp,python  | DP+贪心  |
| 后续待刷的题目：                                             |        |             |          |
| [5691. 通过最少操作次数使数组的和相等](https://leetcode-cn.com/problems/equal-sum-arrays-with-minimum-number-of-operations/) | medium | cpp,python  | 其它     |
| [860. 柠檬水找零](https://leetcode-cn.com/problems/lemonade-change/) | easy   |             | 其它     |
| [402. 移掉K位数字](https://leetcode-cn.com/problems/remove-k-digits/) |        |             |          |
| [1288. 删除被覆盖区间](https://leetcode-cn.com/problems/remove-covered-intervals/) |        |             | 区间问题 |
| [649. Dota2 参议院](https://leetcode-cn.com/problems/dota2-senate/) |        |             |          |
| [316. 去除重复字母](https://leetcode-cn.com/problems/remove-duplicate-letters/) |        |             |          |
| [55. 跳跃游戏](https://leetcode-cn.com/problems/jump-game/)  |        |             |          |
| [134. 加油站](https://leetcode-cn.com/problems/gas-station/) |        |             |          |
| 石子游戏                                                     |        |             |          |
| [12. 整数转罗马数字](https://leetcode-cn.com/problems/integer-to-roman/) |        |             |          |
| [13. 罗马数字转整数](https://leetcode-cn.com/problems/roman-to-integer/) |        |             |          |
| [不错的贪心讲解](https://leetcode-cn.com/problems/minimum-number-of-taps-to-open-to-water-a-garden/solution/xi-fa-jiao-ni-xue-suan-fa-tan-xin-1326-guan-gai-hu/) |        |             |          |
| [738. 单调递增的数字](https://leetcode-cn.com/problems/monotone-increasing-digits/) |        |             |          |
| [1363. 形成三的最大倍数](https://leetcode-cn.com/problems/largest-multiple-of-three/) | hard   |             |          |
| [767. 重构字符串](https://leetcode-cn.com/problems/reorganize-string/) |        |             |          |

27.比较经典的贪心题
（以leetcode 跳跃游戏为例吧）

### 双指针

| 题目链接                                                     | 难度   | 个人题解                                                     | 说明      |
| ------------------------------------------------------------ | ------ | ------------------------------------------------------------ | --------- |
| [1. 两数之和](https://leetcode-cn.com/problems/two-sum/)     |        |                                                              | N数之和   |
| [167. 两数之和 II - 输入有序数组](https://leetcode-cn.com/problems/two-sum-ii-input-array-is-sorted/) | easy   | cpp,python                                                   | N数之和   |
| [633. 平方数之和](https://leetcode-cn.com/problems/sum-of-square-numbers/) | medium | cpp,python                                                   | N数之和   |
| [15. 三数之和](https://leetcode-cn.com/problems/3sum/)       |        |                                                              | N数之和   |
| [16. 最接近的三数之和](https://leetcode-cn.com/problems/3sum-closest/) |        |                                                              | N数之和   |
| [18. 四数之和](https://leetcode-cn.com/problems/4sum/)       |        |                                                              | N数之和   |
| [454. 四数相加 II](https://leetcode-cn.com/problems/4sum-ii/) |        |                                                              | N数之和   |
| [142. 环形链表 II](https://leetcode-cn.com/problems/linked-list-cycle-ii/) | medium | cpp,python                                                   | 快慢指针  |
| [141. 环形链表](https://leetcode-cn.com/problems/linked-list-cycle/) |        |                                                              | 快慢指针  |
| [876. 链表的中间结点](https://leetcode-cn.com/problems/middle-of-the-linked-list/) |        |                                                              | 快慢指针  |
| [202. 快乐数](https://leetcode-cn.com/problems/happy-number/) |        |                                                              | 快慢指针  |
| 倒数第k个节点                                                |        |                                                              | 快慢指针  |
| [3. 无重复字符的最长子串](https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/) | medium | cpp,python                                                   | 滑动窗口  |
| [76. 最小覆盖子串](https://leetcode-cn.com/problems/minimum-window-substring/) | hard   | cpp,python                                                   | 滑动窗口  |
| 340. 至多包含 K 个不同字符的最长子串                         | hard   | cpp,python                                                   | 滑动窗口  |
| [395. 至少有 K 个重复字符的最长子串](https://leetcode-cn.com/problems/longest-substring-with-at-least-k-repeating-characters/) | medium |                                                              |           |
| [1208. 尽可能使字符串相等](https://leetcode-cn.com/problems/get-equal-substrings-within-budget/) | medium | 已AC                                                         | 滑动窗口  |
| [485. 最大连续1的个数](https://leetcode-cn.com/problems/max-consecutive-ones/) | easy   | cpp,python                                                   | 滑动窗口  |
| [487. 最大连续1的个数 II](https://leetcode-cn.com/problems/max-consecutive-ones-ii/) | medium | 没有权限                                                     | 滑动窗口  |
| [1004. 最大连续1的个数 III](https://leetcode-cn.com/problems/max-consecutive-ones-iii/) | medium | cpp,python                                                   | 滑动窗口  |
| [125. 验证回文串](https://leetcode-cn.com/problems/valid-palindrome/) | easy   | cpp,python                                                   | 回文串    |
| [680. 验证回文字符串 Ⅱ](https://leetcode-cn.com/problems/valid-palindrome-ii/) | easy   | cpp,python                                                   | 回文串    |
| [524. 通过删除字母匹配到字典里最长单词](https://leetcode-cn.com/problems/longest-word-in-dictionary-through-deleting/) | medium | cpp,python                                                   | 字符串    |
| [88. 合并两个有序数组](https://leetcode-cn.com/problems/merge-sorted-array/) | easy   | cpp,python                                                   | 归并排序  |
| [845. 数组中的最长山脉](https://leetcode-cn.com/problems/longest-mountain-in-array/) |        |                                                              |           |
| [830. 较大分组的位置](https://leetcode-cn.com/problems/positions-of-large-groups/) |        |                                                              |           |
| [42. 接雨水](https://leetcode-cn.com/problems/trapping-rain-water/) | hard   | cpp,python                                                   | 区间最值  |
| [11. 盛最多水的容器](https://leetcode-cn.com/problems/container-with-most-water/) | medium | cpp,python                                                   | 区间最值  |
| [844. 比较含退格的字符串](https://leetcode-cn.com/problems/backspace-string-compare/) |        |                                                              |           |
| [925. 长按键入](https://leetcode-cn.com/problems/long-pressed-name/) |        |                                                              |           |
| [1423. 可获得的最大点数](https://leetcode-cn.com/problems/maximum-points-you-can-obtain-from-cards/) |        |                                                              | 滑动窗口  |
| [978. 最长湍流子数组](https://leetcode-cn.com/problems/longest-turbulent-subarray/) | medium | cpp,python                                                   | 滑动窗口  |
| [992. K 个不同整数的子数组](https://leetcode-cn.com/problems/subarrays-with-k-different-integers/) | hard   | [把这个题解看了](https://leetcode-cn.com/problems/subarrays-with-k-different-integers/solution/k-ge-bu-tong-zheng-shu-de-zi-shu-zu-by-l-ud34/) | 滑动窗口  |
| [567. 字符串的排列](https://leetcode-cn.com/problems/permutation-in-string/) | medium | cpp,python                                                   | 滑窗+哈希 |
| [1438. 绝对差不超过限制的最长连续子数组](https://leetcode-cn.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/) | medium | cpp,python                                                   | 滑窗+ST   |
| [1052. 爱生气的书店老板](https://leetcode-cn.com/problems/grumpy-bookstore-owner/) | medium | cpp,python                                                   | 滑动窗口  |
| [228. 汇总区间](https://leetcode-cn.com/problems/summary-ranges/) |        |                                                              | 区间问题  |

滑窗法经典问题：

- 【至多/至少】+【k个不同/k个相同/每个字符出现k次】+【最长/最短】+字符串
- 至多包括k个不同字符的最长字符串（leetcode340，滑窗法）
- 至多包括k个不同字符的最短字符串（0，无意义）
- 至多包括k个相同字符的最长字符串（其实就是每个字符至多出现k次，滑窗法，leetcode3的拓展）
- 至多包括k个相同字符的最短字符串（0，无意义）
- 至少包括k个不同字符的最长字符串（不存在，或者str.size()）
- 至少包括k个不同字符的最短字符串（滑窗法）
- 至少包括k个相同字符的最长字符串（不存在，或者str.size()）
- 至少包括k个相同字符的最短字符串（滑窗法）
- 每个字符至少出现k次的最长字符串（leetcode395，这个比较特殊）

### 二分查找

| 题目链接                                                     | 难度   | 个人题解   | 说明        |
| ------------------------------------------------------------ | ------ | ---------- | ----------- |
| [69. x 的平方根](https://leetcode-cn.com/problems/sqrtx/)    | easy   | cpp,python | 常规二分    |
| [34. 在排序数组中查找元素的第一个和最后一个位置](https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/) | medium | cpp,python | 区间二分    |
| [33. 搜索旋转排序数组](https://leetcode-cn.com/problems/search-in-rotated-sorted-array/) | medium | cpp,python | 旋转二分    |
| [81. 搜索旋转排序数组 II](https://leetcode-cn.com/problems/search-in-rotated-sorted-array-ii/) | medium | cpp,python | 旋转二分    |
| [153. 寻找旋转排序数组中的最小值](https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array/) | medium | cpp,python | 旋转二分    |
| [154. 寻找旋转排序数组中的最小值 II](https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array-ii/) | hard   | cpp,python | 旋转二分    |
| [540. 有序数组中的单一元素](https://leetcode-cn.com/problems/single-element-in-a-sorted-array/) | medium | cpp,python | 按值二分    |
| [4. 寻找两个正序数组的中位数](https://leetcode-cn.com/problems/median-of-two-sorted-arrays/) | hard   | cpp,python | 两路二分    |
| [74. 搜索二维矩阵](https://leetcode-cn.com/problems/search-a-2d-matrix/) | medium | cpp,python | coo二维数组 |
| [240. 搜索二维矩阵 II](https://leetcode-cn.com/problems/search-a-2d-matrix-ii/) | medium | cpp,python | 二维数组    |
| [378. 有序矩阵中第K小的元素](https://leetcode-cn.com/problems/kth-smallest-element-in-a-sorted-matrix/)（难，重点学习） |        |            |             |
| [475. 供暖器](https://leetcode-cn.com/problems/heaters/)     |        |            |             |
| [162. 寻找峰值](https://leetcode-cn.com/problems/find-peak-element/) |        |            | 有空做一下  |
| [牛客比赛中出现的二分题目](https://blog.csdn.net/qq_44900959/article/details/110284829?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-2.control&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-2.control) |        |            |             |
| 寻找单个元素，寻找左边界，寻找右边界                         |        |            |             |
| [总结](https://leetcode-cn.com/problems/search-a-2d-matrix/solution/yi-wen-dai-ni-gao-ding-duo-ge-er-fen-cha-2hl9/) |        |            |             |

### 排序

摆动排序，设计到了三分法，快排分区

- 280摆动排序，https://www.cnblogs.com/grandyang/p/5177285.html
- [324. 摆动排序 II](https://leetcode-cn.com/problems/wiggle-sort-ii/)
- 荷兰国旗，三分法，https://www.cnblogs.com/zhoug2020/p/6780604.html
- https://www.cnblogs.com/zhoug2020/p/6780604.html
- https://leetcode-cn.com/problems/wiggle-sort-ii/solution/onshi-jian-fu-za-du-zhong-wei-shu-he-lan-qi-by-jus/

| 题目链接                                                     | 难度   | 个人题解   | 说明             |
| ------------------------------------------------------------ | ------ | ---------- | ---------------- |
| [215. 数组中的第K个最大元素](https://leetcode-cn.com/problems/kth-largest-element-in-an-array/) | medium | cpp,python | topk, 快排, 二分 |
| [347. 前 K 个高频元素](https://leetcode-cn.com/problems/top-k-frequent-elements/) | medium | cpp,python | topk, 桶排序     |
| [692. 前K个高频单词](https://leetcode-cn.com/problems/top-k-frequent-words/) |        |            | topk             |
| [973. 最接近原点的 K 个点](https://leetcode-cn.com/problems/k-closest-points-to-origin/) |        |            | topk             |
| [牛客. 出现次数的TopK问题](https://www.nowcoder.com/practice/fd711bdfa0e840b381d7e1b82183b3ee?tpId=117&&tqId=35559&rp=1&ru=/ta/job-code-high&qru=/ta/job-code-high/question-ranking) |        |            | topk, 二分       |
| [4. 寻找两个正序数组的中位数](https://leetcode-cn.com/problems/median-of-two-sorted-arrays/) | hard   | cpp,python | topk             |
| [703. 数据流中的第 K 大元素](https://leetcode-cn.com/problems/kth-largest-element-in-a-stream/) | easy   | cpp,python | topk             |
| 无序数组，找min和max（nowcoder/get_min_max）                 |        |            | topk             |
| 无序数组，找max和max2（nowcoder/get_max_max2）               |        |            | topk             |
| 无序数组，找第k大的值（nowcoder/get_topk）                   |        |            | topk             |
| 无序数组，找前k大的值（nowcoder/get_all_topk）               |        |            | topk             |
| [451. 根据字符出现频率排序](https://leetcode-cn.com/problems/sort-characters-by-frequency/) | medium | cpp,python | 快排，桶排序     |
| [75. 颜色分类](https://leetcode-cn.com/problems/sort-colors/) | medium | cpp,python | 快排，荷兰国旗   |
| [283. 移动零](https://leetcode-cn.com/problems/move-zeroes/) |        |            | 快排，荷兰国旗   |
| [27. 移除元素](https://leetcode-cn.com/problems/remove-element/) |        |            | 快排，快排分区   |
| [1768. 交替合并字符串](https://leetcode-cn.com/problems/merge-strings-alternately/) |        |            | 归并排序         |
| [88. 合并两个有序数组](https://leetcode-cn.com/problems/merge-sorted-array/) |        |            | 归并排序         |
| [21. 合并两个有序链表](https://leetcode-cn.com/problems/merge-two-sorted-lists/) |        |            | 归并排序         |
| [23. 合并K个升序链表](https://leetcode-cn.com/problems/merge-k-sorted-lists/) |        |            | 归并排序         |
| [剑指 Offer 51. 数组中的逆序对](https://leetcode-cn.com/problems/shu-zu-zhong-de-ni-xu-dui-lcof/) |        |            | 归并排序         |
| [493. 翻转对](https://leetcode-cn.com/problems/reverse-pairs/) |        |            | 归并排序         |
| [315. 计算右侧小于当前元素的个数](https://leetcode-cn.com/problems/count-of-smaller-numbers-after-self/) |        |            | 归并排序         |
| [327. 区间和的个数](https://leetcode-cn.com/problems/count-of-range-sum/) |        |            | 归并排序         |
| [977. 有序数组的平方](https://leetcode-cn.com/problems/squares-of-a-sorted-array/) |        |            | 归并排序         |
| [147. 对链表进行插入排序](https://leetcode-cn.com/problems/insertion-sort-list/) |        |            | 链表排序         |
| [148. 排序链表](https://leetcode-cn.com/problems/sort-list/) |        |            | 链表排序         |
| [剑指 Offer 21. 调整数组顺序使奇数位于偶数前面](https://leetcode-cn.com/problems/diao-zheng-shu-zu-shun-xu-shi-qi-shu-wei-yu-ou-shu-qian-mian-lcof/) |        |            | 奇偶排序         |
| [905. 按奇偶排序数组](https://leetcode-cn.com/problems/sort-array-by-parity/) |        |            | 奇偶排序         |
| [922. 按奇偶排序数组 II](https://leetcode-cn.com/problems/sort-array-by-parity-ii/) |        |            | 奇偶排序         |
| [1356. 根据数字二进制下 1 的数目排序](https://leetcode-cn.com/problems/sort-integers-by-the-number-of-1-bits/) |        |            | 其它             |
| [324. 摆动排序 II](https://leetcode-cn.com/problems/wiggle-sort-ii/) |        |            | 其它             |

### 搜索

| 题目链接                                                     | 难度       | 个人题解   | 说明               |
| ------------------------------------------------------------ | ---------- | ---------- | ------------------ |
| [463. 岛屿的周长](https://leetcode-cn.com/problems/island-perimeter/) | easy       | cpp,python | DFS，岛屿问题      |
| [200. 岛屿数量](https://leetcode-cn.com/problems/number-of-islands/) | medium     | cpp,python | DFS，岛屿问题，BFS |
| 岛屿数量2，没权限                                            | hard       |            | DFS，岛屿问题      |
| [695. 岛屿的最大面积](https://leetcode-cn.com/problems/max-area-of-island/) | medium     | cpp,python | DFS，岛屿问题      |
| [130. 被围绕的区域](https://leetcode-cn.com/problems/surrounded-regions/) | medium     | cpp,python | DFS，岛屿问题，BFS |
| [547. 省份数量](https://leetcode-cn.com/problems/number-of-provinces/) | medium     | cpp,python | DFS，连通域个数    |
| [417. 太平洋大西洋水流问题](https://leetcode-cn.com/problems/pacific-atlantic-water-flow/) | medium     | cpp,python | DFS，其它          |
| [46. 全排列](https://leetcode-cn.com/problems/permutations/) | medium     | cpp,python | DFS，回溯法        |
| [47. 全排列 II](https://leetcode-cn.com/problems/permutations-ii/) | medium     | cpp,python | DFS，回溯法        |
| [784. 字母大小写全排列](https://leetcode-cn.com/problems/letter-case-permutation/) | medium     | cpp,python | DFS，回溯法        |
| [78. 子集](https://leetcode-cn.com/problems/subsets/)        | medium     | cpp,python | DFS，回溯法        |
| [90. 子集 II](https://leetcode-cn.com/problems/subsets-ii/)  | medium     | cpp,python | DFS，回溯法        |
| [77. 组合](https://leetcode-cn.com/problems/combinations/)   | medium     | cpp,python | DFS，回溯法        |
| [39. 组合总和](https://leetcode-cn.com/problems/combination-sum/) | medium     | cpp,python | DFS，回溯法        |
| [40. 组合总和 II](https://leetcode-cn.com/problems/combination-sum-ii/) | medium     | cpp,python | DFS，回溯法        |
| [216. 组合总和 III](https://leetcode-cn.com/problems/combination-sum-iii/) | medium     | cpp,python | DFS，回溯法        |
| [377. 组合总和 Ⅳ](https://leetcode-cn.com/problems/combination-sum-iv/) | medium     | cpp,python | DFS，回溯法        |
| [79. 单词搜索](https://leetcode-cn.com/problems/word-search/) | medium     | cpp,python | DFS，回溯法        |
| [212. 单词搜索 II](https://leetcode-cn.com/problems/word-search-ii/) | hard       | 难但有思路 | DFS，回溯法        |
| [17. 电话号码的字母组合](https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number/) | medium     |            | DFS，回溯法        |
| [980. 不同路径 III](https://leetcode-cn.com/problems/unique-paths-iii/) | hard       |            | DFS，回溯法        |
| [1219. 黄金矿工](https://leetcode-cn.com/problems/path-with-maximum-gold/) | medium     |            | DFS，回溯法        |
| [51. N 皇后](https://leetcode-cn.com/problems/n-queens/)     | hard       | cpp,python | DFS，回溯法        |
| [52. N皇后 II](https://leetcode-cn.com/problems/n-queens-ii/) | hard       | cpp,python | DFS，回溯法        |
| [37. 解数独](https://leetcode-cn.com/problems/sudoku-solver/) | medium     | cpp,python | DFS，回溯法        |
| [剑指 Offer 12. 矩阵中的路径](https://leetcode-cn.com/problems/ju-zhen-zhong-de-lu-jing-lcof/) | medium     | cpp,python | DFS，回溯法        |
| [剑指 Offer 13. 机器人的运动范围](https://leetcode-cn.com/problems/ji-qi-ren-de-yun-dong-fan-wei-lcof/) | medium     | cpp,python | DFS，回溯法        |
| [140. 单词拆分 II](https://leetcode-cn.com/problems/word-break-ii/) | hard       | cpp,python | DFS，回溯法        |
| [《回溯法总结分析》](https://leetcode-cn.com/problems/permutations/solution/hui-su-suan-fa-python-dai-ma-java-dai-ma-by-liweiw/) |            |            |                    |
| [967. 连续差相同的数字](https://leetcode-cn.com/problems/numbers-with-same-consecutive-differences/) | medium     | cpp,python | DFS，其它          |
| [733. 图像渲染](https://leetcode-cn.com/problems/flood-fill/) |            |            | DFS，其它          |
| [1034. 边框着色](https://leetcode-cn.com/problems/coloring-a-border/) |            |            | DFS，其它          |
| [22. 括号生成](https://leetcode-cn.com/problems/generate-parentheses/) |            |            | DFS，括号匹配      |
| [301. 删除无效的括号](https://leetcode-cn.com/problems/remove-invalid-parentheses/) |            |            | DFS，括号匹配      |
| [257. 二叉树的所有路径](https://leetcode-cn.com/problems/binary-tree-paths/) | 放到树专题 |            | DFS，二叉树        |
| [310. 最小高度树](https://leetcode-cn.com/problems/minimum-height-trees/) | 放到图专题 |            | DFS，图            |
| [934. 最短的桥](https://leetcode-cn.com/problems/shortest-bridge/) | medium     | cpp,python | BFS，岛屿问题      |
| [542. 01 矩阵](https://leetcode-cn.com/problems/01-matrix/)  | medium     | cpp,python | BFS                |
| [994. 腐烂的橘子](https://leetcode-cn.com/problems/rotting-oranges/) | medium     | cpp,python | BFS                |
| [127. 单词接龙](https://leetcode-cn.com/problems/word-ladder/) | hard       | cpp,python | BFS，双向          |
| [126. 单词接龙 II](https://leetcode-cn.com/problems/word-ladder-ii/) | hard       | cpp,python | BFS，双向          |
| [433. 最小基因变化](https://leetcode-cn.com/problems/minimum-genetic-mutation/) | medium     | cpp,python | BFS，双向          |
| [752. 打开转盘锁](https://leetcode-cn.com/problems/open-the-lock/) | medium     |            | BFS，双向          |

### 动态规划

| 题目链接                                                     | 难度   | 个人题解   | 说明               |
| ------------------------------------------------------------ | ------ | ---------- | ------------------ |
| [70. 爬楼梯](https://leetcode-cn.com/problems/climbing-stairs/) | easy   | cpp,python | DP，一维           |
| [198. 打家劫舍](https://leetcode-cn.com/problems/house-robber/) | medium | cpp,python | DP，一维，打家劫舍 |
| [213. 打家劫舍 II](https://leetcode-cn.com/problems/house-robber-ii/) | medium | cpp,python | DP，一维，打家劫舍 |
| [413. 等差数列划分](https://leetcode-cn.com/problems/arithmetic-slices/) | medium | cpp,python | DP，一维           |
| [64. 最小路径和](https://leetcode-cn.com/problems/minimum-path-sum/) | medium | cpp,python | DP，二维           |
| [62. 不同路径](https://leetcode-cn.com/problems/unique-paths/) | medium | cpp,python | DP，二维           |
| [63. 不同路径 II](https://leetcode-cn.com/problems/unique-paths-ii/) | medium | cpp,python | DP，二维           |
| [542. 01 矩阵](https://leetcode-cn.com/problems/01-matrix/)  | medium | cpp,python | DP，二维           |
| [221. 最大正方形](https://leetcode-cn.com/problems/maximal-square/) | medium | cpp,python | DP，二维           |
| [85. 最大矩形](https://leetcode-cn.com/problems/maximal-rectangle/) | hard   | cpp,python | DP，二维           |
| [279. 完全平方数](https://leetcode-cn.com/problems/perfect-squares/) | medium | cpp,python | DP，分割类型       |
| [91. 解码方法](https://leetcode-cn.com/problems/decode-ways/) | medium | cpp,python | DP，分割类型       |
| [139. 单词拆分](https://leetcode-cn.com/problems/word-break/) | medium | cpp,python | DP，分割类型       |
| [343. 整数拆分](https://leetcode-cn.com/problems/integer-break/) | medium | cpp,python | DP，分割类型       |
| [313. 超级丑数](https://leetcode-cn.com/problems/super-ugly-number/) | medium | cpp,python | DP，分割类型       |
| [53. 最大子序和](https://leetcode-cn.com/problems/maximum-subarray/) | easy   | cpp,python | DP，子序列问题     |
| [300. 最长递增子序列](https://leetcode-cn.com/problems/longest-increasing-subsequence/) | medium | cpp,python | DP，子序列问题     |
| [354. 俄罗斯套娃信封问题](https://leetcode-cn.com/problems/russian-doll-envelopes/) | hard   | cpp,python | DP，子序列问题     |
| [1143. 最长公共子序列](https://leetcode-cn.com/problems/longest-common-subsequence/) | medium | cpp,python | DP，子序列问题     |
| [516. 最长回文子序列](https://leetcode-cn.com/problems/longest-palindromic-subsequence/) | medium | cpp,python | DP，子序列问题     |
| [1771. 由子序列构造的最长回文串的长度](https://leetcode-cn.com/problems/maximize-palindrome-length-from-subsequences/) | hard   | cpp,python | DP，子序列问题     |
| [115. 不同的子序列](https://leetcode-cn.com/problems/distinct-subsequences/) | hard   | cpp,python | DP，子序列问题     |
| [1218. 最长定差子序列](https://leetcode-cn.com/problems/longest-arithmetic-subsequence-of-given-difference/) | medium | cpp,python | DP，子序列问题     |
| [446. 等差数列划分 II - 子序列](https://leetcode-cn.com/problems/arithmetic-slices-ii-subsequence/) | hard   | cpp,python | DP，子序列问题     |
| [646. 最长数对链](https://leetcode-cn.com/problems/maximum-length-of-pair-chain/) |        |            |                    |
| [376. 摆动序列](https://leetcode-cn.com/problems/wiggle-subsequence/) |        |            |                    |
| [416. 分割等和子集](https://leetcode-cn.com/problems/partition-equal-subset-sum/) | medium | cpp,python | DP，背包问题       |
| [1049. 最后一块石头的重量 II](https://leetcode-cn.com/problems/last-stone-weight-ii/) | medium | cpp,python | DP，背包问题       |
| [474. 一和零](https://leetcode-cn.com/problems/ones-and-zeroes/) | medium | cpp,python | DP，背包问题       |
| [322. 零钱兑换](https://leetcode-cn.com/problems/coin-change/) | medium | cpp,python | DP，背包问题       |
| [518. 零钱兑换 II](https://leetcode-cn.com/problems/coin-change-2/) | medium | cpp,python | DP，背包问题       |
| [494. 目标和](https://leetcode-cn.com/problems/target-sum/)  | medium | cpp,python | DP，背包问题       |
| [377. 组合总和 Ⅳ](https://leetcode-cn.com/problems/combination-sum-iv/) | medium | cpp,python | DP，背包问题       |
| [背包问题总结](https://leetcode-cn.com/problems/combination-sum-iv/solution/xi-wang-yong-yi-chong-gui-lu-gao-ding-bei-bao-wen-/) |        |            |                    |
| [583. 两个字符串的删除操作](https://leetcode-cn.com/problems/delete-operation-for-two-strings/) | medium | cpp,python | DP，字符串编辑     |
| [712. 两个字符串的最小ASCII删除和](https://leetcode-cn.com/problems/minimum-ascii-delete-sum-for-two-strings/) | medium | cpp,python | DP，字符串编辑     |
| [72. 编辑距离](https://leetcode-cn.com/problems/edit-distance/) | hard   | cpp,python | DP，字符串编辑     |
| [650. 只有两个键的键盘](https://leetcode-cn.com/problems/2-keys-keyboard/) | medium | cpp,python | DP，字符串编辑     |
| [10. 正则表达式匹配](https://leetcode-cn.com/problems/regular-expression-matching/) | hard   | cpp,python | DP，字符串编辑     |
| [131. 分割回文串](https://leetcode-cn.com/problems/palindrome-partitioning/) | medium | cpp,python | DP，回文串         |
| [132. 分割回文串 II](https://leetcode-cn.com/problems/palindrome-partitioning-ii/) | hard   | cpp,python | DP，回文串         |
| [121. 买卖股票的最佳时机](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/) | easy   | cpp,python | DP，股票交易       |
| [122. 买卖股票的最佳时机 II](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/) | easy   | cpp,python | DP，股票交易       |
| [123. 买卖股票的最佳时机 III](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iii/) | hard   | cpp,python | DP，股票交易       |
| [188. 买卖股票的最佳时机 IV](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iv/) | hard   | cpp,python | DP，股票交易       |
| [309. 最佳买卖股票时机含冷冻期](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/) | medium | cpp,python | DP，股票交易       |
| [714. 买卖股票的最佳时机含手续费](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/) | medium | cpp,python | DP，股票交易       |
| [1770. 执行乘法运算的最大分数](https://leetcode-cn.com/problems/maximum-score-from-performing-multiplication-operations/) |        |            | 其它               |

20.给定一个二维01矩阵，返回其中全为1的正方形个数
（首先明确，全为1的概念）
（暴力法，利用滑窗的概念，类似目标检测，设置大小分别为1，2，3等的滑窗边长，进行搜索，判断窗口内是否全为1）
（高效方法，二维dp，同下）
（拓展：输入一个二维01矩阵，判断矩阵中全为1的正方形的最大边长，解决方法是二维dp，dp表示以该点为正方形右下角的结果）
（参考这个：https://www.jianshu.com/p/173b9339a0cd）

区间问题：

区间动态规划
石子合并
能量项链

### 分治法

这里也包括了“递归”的一些题目。

| 题目链接                                                     | 难度   | 个人题解   | 说明             |
| ------------------------------------------------------------ | ------ | ---------- | ---------------- |
| [241. 为运算表达式设计优先级](https://leetcode-cn.com/problems/different-ways-to-add-parentheses/) | medium | cpp,python | 分治，区间DP     |
| [932. 漂亮数组](https://leetcode-cn.com/problems/beautiful-array/) | medium | cpp,python | 分治，记忆化递归 |
| [312. 戳气球](https://leetcode-cn.com/problems/burst-balloons/) | hard   | cpp,python | 分治，区间DP     |
| [1000. 合并石头的最低成本](https://leetcode-cn.com/problems/minimum-cost-to-merge-stones/) | hard   | cpp,python | 分治，区间DP     |

## 第三部分：数学问题

- 快速幂

### 位运算

- 常见位运算操作

## 第四部分：专题

### 团灭股票买卖

**考虑三个条件限制：**

- 买卖次数（有限k次，或者无限次数）
- 冷冻期（卖出后冷冻k天，或者无）
- 手续费（每次卖出后收费，或者无）

**解决思路：**

- 列出所有情况的状态机
- 分析状态跳转
- 完成动态规划
- 进行空间优化

| 题目链接                                                     | 难度   | 个人题解   | 说明         |
| ------------------------------------------------------------ | ------ | ---------- | ------------ |
| [121. 买卖股票的最佳时机](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/) | easy   | cpp,python | DP，股票交易 |
| [122. 买卖股票的最佳时机 II](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/) | easy   | cpp,python | DP，股票交易 |
| [123. 买卖股票的最佳时机 III](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iii/) | hard   | cpp,python | DP，股票交易 |
| [188. 买卖股票的最佳时机 IV](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iv/) | hard   | cpp,python | DP，股票交易 |
| [309. 最佳买卖股票时机含冷冻期](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/) | medium | cpp,python | DP，股票交易 |
| [714. 买卖股票的最佳时机含手续费](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/) | medium | cpp,python | DP，股票交易 |

### 其它待整理

| 题目链接               | 难度   | 个人题解 | 说明     |
| ---------------------- | ------ | -------- | -------- |
|                        |        |          | 石子游戏 |
|                        |        |          | N数之和  |
|                        |        |          | 铺瓷砖   |
| 普通数组，两个有序数组 | 数据流 | 滑动窗口 | 中位数   |
|                        |        |          | LRU      |

### 待搞定的题目

- 基本计算器，224，227
- KMP算法，28
- 马拉车算法，回文串
- 单源最短路径Dijkstra算法，图论方面的问题
- 打家劫舍
- 跳跃游戏
- 敏感词匹配

### Leetcode周赛

**第232场周赛：**

- [1790. 仅执行一次字符串交换能否使两个字符串相等](https://leetcode-cn.com/problems/check-if-one-string-swap-can-make-strings-equal/)
- [1791. 找出星型图的中心节点](https://leetcode-cn.com/problems/find-center-of-star-graph/)
- [1792. 最大平均通过率](https://leetcode-cn.com/problems/maximum-average-pass-ratio/)
- [1793. 好子数组的最大分数](https://leetcode-cn.com/problems/maximum-score-of-a-good-subarray/)

### 来自面经

1. 微软面经中的一道题，https://www.nowcoder.com/discuss/537549?type=post&order=time&pos=&page=1&channel=1009&source_id=search_post，（给一个由0和1构成的数组，计算0和1个数相等的最长子数组，返回其长度）

   > 一开始想错了，以为是直接滑窗法就完事了，结果不是
   >
   > https://blog.csdn.net/yellowxz/article/details/11763045?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromBaidu-3.control&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromBaidu-3.control
   >
   > https://blog.csdn.net/qq_16234613/article/details/89382379?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromBaidu-3.control&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromBaidu-3.control

2. dfs序专题：https://www.nowcoder.com/discuss/559210?type=101&channel=1009&source_id=discuss_terminal_discuss_jinghua

3. 总结16号的每日一题

   > https://leetcode-cn.com/problems/queue-reconstruction-by-height/（完成leetcode一类题目的总结，参考这篇题解：https://leetcode-cn.com/problems/queue-reconstruction-by-height/solution/onlogncshuang-bai-jie-fa-shu-zhuang-shu-zu-28ms11m/）
   >
   > 16号的题解：（需要重点学习一下）
   >
   > 首先明确，这个题的类型并不是贪心，因为题目有唯一解，如何按怎样的顺序来复原，结果都是唯一的区别就是复原的过程不同，有的复杂，有的简单（先排序，再放置，要简单）
   >
   > 第一种思路是，按值从大到小排序，然后从大到小插入，因为后续元素没有更大的了，因此可以只根据当前的元素来插入。（缺点是，每一次插入都不能确定元素的最终位置）
   >
   > 第二种思路，按值从小到大排序，然后从小到大插入，此时后续元素没有更小的了，因此可以唯一确定当前元素的位置（保证之前有k空位即可，需要从前往后的O(n)遍历）
   >
   > 第三种思路，线段树，对树状数组进行初始化，a[i]表示以i为根的树中空座位数量（基础知识见：https://zhuanlan.zhihu.com/p/29876526）

4. 其它leetcode题目：https://leetcode-cn.com/problems/remove-k-digits/solution/yi-zhao-chi-bian-li-kou-si-dao-ti-ma-ma-zai-ye-b-5/，（https://leetcode-cn.com/problems/remove-duplicate-letters/）

5. 昨天在牛客上，做了一道螺旋数组的问题，可以跟之前的打印二维数组类比，还有旋转90度矩阵（个人举一反三，实现二维矩阵的斜向遍历，从左上到右下角）

6. 字符串是否符合规范，有日期和时间还有一些别的判断，非常复杂，写代码写了30分钟。（参考剑指offer，表示数值的字符串）

7. 给会议的start和end，求能开最多的会，蠡口原题。最多可以参加的会议数目。贪心的思想。在每一天，从这一天可以去的会议中，选择结束时间最早的那一场去。

8. 一个全是0和1的二维矩阵，判断其中所有的1能不能构成一个等腰直角三角形，需要将三角形里所有的位置填充满，包括三条边和里面。这题写了好久，不太会，后来面试官改简单了一点，直角顶点朝向左下。

   > 首先询问是否只有一个1的连通域
   > （1，从左上角开始BFS，找到第一个1）
   > （2，从第一个1开始进行洪水填充BFS，找到该连通域的所有边界）
   > （3，通过这些边界点，判断是否为三角形，并返回三个顶点）（使用聚类法，找斜率，获取边和顶点，顶点是不同类的交集）
   > （4，利用三个顶点判断是否等腰直角三角形）

9. 给出一些父节点到子节点的路径，判断这个图是不是一个二叉树。写的时候没想太好，写的非常复杂，最后好像过了。（二叉树的定义：每一个节点只有两个子节点，并且子节点不能指向祖先节点）

10. n位数的递增数有多少个，递增数是123,123456,34789这样的，1334不算。

    > （感觉可以二维dp，dpn表示当第n位数可以从start开始变化的时候，n位及后续位数的总变化情况个数）
    > （dpn = dpn + dpn + 1）
    > （注意从右下角往左上角填充，并且注意首位不能为0，并且一些特殊情况不可取，如倒数第二位是9则不合理）

11. 手撕代码题是通过a+2,a*3+2这两种计算方式的任意组合，验证能否由a变成b，我当时写了个回溯的方法。

    > （优先明确，是否ab都为正数，是否a小于b）
    > （可以回溯，两条路两种运算，一个是乘加，一个是加，优先DFS遍历乘加，直到a的值大于了b，则回溯到上一步，改为相加）

12. 用c语言实现：给定一个字符串str和另一个字符串sub，统计str中sub出现的次数。不能使用库函数。
    （暴力方法，或者KMP匹配，再不行就是滑窗法，dp）

13. 至少去除数组中多少个数能使数组成为单调序列。类似leetcode300
    （动态规划 + 二分查找）

14. 电话面: 一道算法题，BFS变形，但当时用了dijikstra，更好的算法是我在系统地学完算法之后才想出来的，大概是用了BFS的最小边数搜索性质，具体可见算法导论

15. 请实现一个单向链表（包括append等常规操作），并外加实现一个setAll(T value)方法，将链表中所有已插入”元素置为同一特定值。

16. 字符串是否符合规范，有日期和时间还有一些别的判断，非常复杂，写代码写了30分钟。
    （参考剑指offer，表示数值的字符串）

17. 给会议的start和end，求能开最多的会，蠡口原题。（1353最多可以参加的会议数目，贪心的思想。在每一天，从这一天可以去的会议中，选择结束时间最早的那一场去。）

18. 有一个二维字符矩阵，共有四种字符：#——墙，不可行走，X——每个人的起点，*——迷宫出口，.——地面，可以行走，求每个人走到出口的最短路径（保证每个人都可以走到出口）
    （可以BFS）

19. 给定n*n的正方形，每个点都有权值，有些点是障碍物，问从左上角走到右下角的最小花费
    （回溯法，或者dp）

20. 经典算法题：汉诺塔

    ```python
    （https://www.nowcoder.com/discuss/250029?type=2&order=0&pos=9&page=1&channel=-2&source_id=discuss_tag）
    def han(n,fom,to,buffer):
        if n ==1:     
            x = fom.pop()
            to.append(x)
            print('%s->%s:%s'%(fom[0],to[0],x))
            return
        han(n-1,fom,buffer,to) # 首先需要借助to 把 n-1个牌都移动到buffer
        han(1,fom,to,buffer)    # 然后移动一个把要移动的移动过去
        han(n-1,buffer,to,fom) # 然后把 n-1个从buffer 移动到to
    ```

21. 已有两个能生成0到1之间的数，并且这些数是均匀分布的随机生成器，给定一个任意的三角形，如何能在三角形内等概率随机的生成一个点(然后对于多边形呢)
    （感觉先可以在外接圆生成一个随机点，然后排除在三角形外的点）
    （正解：三角形翻倍映射为平行四边形，平行四边形映射为矩形，两个随机数分别表示在矩形长宽上的采样）

22. 二维前缀差分问题 (比较easy)
    （二维前缀和：a[i][j]+=a[i][j-1]+a[i-1][j]-a[i-1][j-1]）
    （参考：https://blog.csdn.net/Love_Jacques/article/details/105628100?utm_medium=distribute.pc_relevant_t0.none-task-blog-BlogCommendFromMachineLearnPai2-1.channel_param&depth_1-utm_source=distribute.pc_relevant_t0.none-task-blog-BlogCommendFromMachineLearnPai2-1.channel_param）

23. 给定一个链表 执行三类操作：（1.将链表的权值都修改成x; 2.链表后面加入新节点；3.打印链表(注意 修改不能遍历所有节点 解法就类似于线段树的lazy标记吧)）

24. 已知有一颗n(n<=1e9)个节点的完全二叉树 每一层编号从左到右以此递增 比如 第一层的节点编号为1 第二层为2、3，现在询问插入的第n+1个节点的父亲的编号 (确定所在层的编号区间 二分答案 然后每次log的复杂度去check合法性)

25. 纯代码面，手撕两道编程题。记得其中一道与flood fill类似。
    （733. 图像渲染）

26. 两道代码题，一道是用类来实现一个计时器。另一道是动态规划题。

27. 多个有序链表合并成一个有序链表，写代码。
    （ok，leetcode23）

28. 字符串匹配 A串长n B串长为m 以A每个位置为起点长为m的子串 排序后与B串做精确匹配，问有多少次精确匹配（暴力法，KMP）

29. 给定整数数组a,要求数组b，b[i]定义为a[i]左边离自己最近的比自己小的数字的下标：单调栈，如果用跳表时间复杂度和正确性证明
    （https://www.jianshu.com/p/9e3416a7a97b）

30. 给出前序遍历、后序遍历有多少种符合的树结构（可被百度）

31. 有序序列，N个数，随机替换其中的K个，求排序算法让序列仍然有序（merge k list很像，或者用堆）

32. 判断二叉搜索树（98. 验证二叉搜索树，高效方法，judge(root, mmin, mmax)）

33. 旋转二维矩阵（leetcode48）

34. 已知二叉树的前序序列，叶子节点为数字，其余节点为运算符，求根最后运算得到的结果
    首先明确，如果是单枝树怎么办？一个节点是None，另一个非空，如何处理？
    其次，运算符都有哪些，是不是都是双目运算？
    还有，如果只知道前序序列，如何区分左子树和右子树
    （感觉跟使用一个栈，依次弹出计算结果然后弹入，类似计算表达式，逆波兰表达式，即后缀表达式）
    （这个题是前缀表达式，运算符放在了字符前边）

35. 按字典序输出1-n之间的数，如n=10时，输出1,10,2,3,4,5,6,7,8,9
    暴力方法是转换为字符串，然后字典序排序
    正确方式是回溯法，（以下个人测试已通过）

    ```python
    def func(n):
    	"""
    	输入n，输出按字典序排列的1-n，是个list
    	"""
    	ret = []
    	path = [] # 内部暂时存储字符串
    	def backTracking(n):
    		"""
    		n表示最大值，i表示当前正在遍历第i位数字
    		"""
    
    ​      退出的情况，当前值已经大于n
    
    ​		if path:
    ​			val = int("".join(path))
    ​			if val > n:
    ​				return
    ​			ret.append(val)
    ​		start = 0 if path else 1
    ​		for j in range(start, 10):
    ​			path.append(str(j))
    ​			backTracking(n)
    ​			path.pop()
    ​	backTracking(n)
    ​	return ret
    ```

36. 给出一个数组，把所有的0移动到最前面，同时其它数组的顺序保持不变（稳定排序，直接冒泡，把0冒泡到前方）（leetcode，283. 移动零）

37. 如何求树的直径（见leetcode543）
    首先明确，树的直径的定义（一棵二叉树的直径长度是任意两个结点路径长度中的最大值。这条路径可能穿过也可能不穿过根结点。）

    ```python
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.ret = 0
        def getHeight(root):
            """
            后续遍历，获取root的高度，同时更新最大直径
            """
            if root == None:
                return 0
            left = getHeight(root.left)
            right = getHeight(root.right)
            self.ret = max(self.ret, left + right)
            return 1 + max(left, right)
        getHeight(root)
        return self.ret
    ```

38. 给定一个数组，如[7864, 284, 347, 7732, 8498]，现在需要将数组中的数字拼接起来，返回最大的可以拼接出的数字（自定义排序，a > b 的判断表达式为：a拼接b > b拼接a）（使用字符串要更加方便进行拼接，以及拼接后的判断）（最后一个要注意的点就是在快排里，完成这个自定义的排序）

39. 丑数（三指针法，其实也是动态规划，pi表示有资格与i相乘的最小丑数的索引）（核心的跳转逻辑为：if dp[i] == dp[p2] * 2: p2 += 1）

40. 打家劫舍（337. 打家劫舍 III）

    ```python
    树形dp，错解如下：
    class Solution:
        def rob(self, root: TreeNode) -> int:
            def back(root):
                """
                后续遍历，自底向上，返回孙子们，儿子们偷的钱，以及自己最大偷的钱
                """
                if root == None:
                    return 0, 0, 0
                lchild, lson, lself = back(root.left)
                rchild, rson, rself = back(root.right)
                return lson + rson, lself + rself, root.val + max(lson + rson, lchild + rchild)
            return max(back(root))
    
    正解如下：
    （两个状态，dp[node][0]以及dp[node][1]）
    class Solution:
        def rob(self, root: TreeNode) -> int:
            def back(root):
                """
                后续遍历，自底向上，返回当前节点偷或者不偷能得到的最大值
                """
                if root == None:
                    return 0, 0
                ldo, lnot = back(root.left)
                rdo, rnot = back(root.right)
                mdo = root.val + lnot + rnot
                mnot = max(ldo, lnot) + max(rdo, rnot)
                return mdo, mnot
            return max(back(root))
    ```

41. 监控二叉树（968. 监控二叉树）

    ```python
    监控二叉树（968. 监控二叉树）
    同树形dp，三种状态，dp[node][0, 1, 2]分别表示，放置摄像头，不放置但已覆盖，不放置且未覆盖，但是这种方式不太好写，错解：
    class Solution:
        def minCameraCover(self, root: TreeNode) -> int:
            def back(root):
                """
                后续遍历，返回三个状态下的数量
                012表示，已放置，未放置已覆盖，未放置未覆盖
                """
                if root == None:
                    return 0, 0, 0
                lset, lcover, lnot = back(root.left)
                rset, rcover, rnot = back(root.right)
                mset = 1 + lnot + rnot
                mcover = min(lset + rcover, rset + lcover)
                mnot = lcover + rcover
                print(mset, mcover, mnot)
                return mset, mcover, mnot
            return min(back(root))
    
    （这是一个贪心的策略，假定从底向上可以获取最优解）正解如下：
    class Solution(object):
        def minCameraCover(self, root):
            """
            :type root: TreeNode
            :rtype: int
            左右中，后续遍历
            3种状态
                0:未覆盖
                1:已覆盖
                2:装有相机
            """
            def dfs(root):
                if root == None:
                    return 1
                left = dfs(root.left)
                right = dfs(root.right)
                if left == 0 or right == 0:
                    self.res += 1
                    return 2
                elif left == 1 and right == 1:
                    return 0
                elif left + right >= 3:
                    return 1
            self.res = 0
        	if dfs(root) == 0:
            	self.res += 1
        	return self.res
    如果改变题意，每台相机只能监控自己，或者直接子对象呢？
    那就是两个状态了，0表示已经放置相机，1表示未放置相机，待覆盖
    ```

42. 频率topk问题（347. 前 K 个高频元素）
    使用快排，生成【出现频次】数组排序，然后二分找到topk

43. 给你一连串的括号。一对括号()的基准分数是1分。一对括号()里面如果嵌套了x对括号，那么这对括号值2x分。

    > （）：1分
    > （（））：3分
    > （（）（））：6分
    > （（）（））（）：7分
    > （（）（（）））（（））：11分
    > def score(s):
    >     n = 0
    >     empty = 0
    >     level = 0
    >     for c in s:
    >         if c == '(':
    >             if level:
    >                 n += 2
    >             empty = 1
    >             level += 1
    >         else:
    >             n += empty
    >             empty = 0
    >             level -= 1
    >     return n

44. 山峰数组，求topk，本来想无脑堆排序，面试官说不要排序，我就想了好久，面试官就一点点引导我，然后写出来，面试官又让优化，听了好久他是让用二分法找山峰，于是又写了一个二分法，然后代码题结束。接着聊人生，然后反问环节。（个人思路：找到最大值，从中间向两边遍历都是有序数组，归并两个有序数组得到topk）（其中这道题很类似leetcode4，两个有序数组求中位数）

45. 对于给定的数组A，每次可以取出任意一个数A[i]，同时要删除数组内所有等于A[i]-1和A[i]+1的数，直到数组为空，可以取出所有数的最大和为多少

    > 我当时是这样写的
    > 首先，数组从小到大排序  因为要找出和最大的 ，所以应该优先挑大的 有点类似于贪心的做法 
    >
    > 把数值相同的数求和，然后还要保留原始的数值 比如[8,8,7,5,5,5]会变成了一个新的数组 S [(16,8),(7,7),(15,5)]这样 
    > 3 到这里就很像leetcode的抢家夺舍了 ，用dp来写 如果i 个i-1不相连 比如S 里面的 7 和5 就直接加上去 dpi =dpi-1 + si  如果相连 就变成了 dpi=max（dpi-2 +si ,dpi-1） 让后取dp的最后一个值就是最大值 这样子

46. LEETCODE 150题吐血大整理，https://blog.csdn.net/zr459927180/article/details/51932655?utm_medium=distribute.pc_relevant_t0.none-task-blog-BlogCommendFromMachineLearnPai2-1.channel_param&depth_1-utm_source=distribute.pc_relevant_t0.none-task-blog-BlogCommendFromMachineLearnPai2-1.channel_param

## 第五部分：智力题

### 智力题

1. 50桶水，其中1桶有毒。有n头猪，一天可以喝两次水，请问在一天内可以找出有毒的那桶水的最小的n。

### 数学题

1. 一个绳子随机剪成三段，求能让这三段组成三角形的概率。（1/4）

2. 积分微分的应用 曲率及曲率半径的推导(2333 保研失败后想过考研 正好把高数给复习了)

3. 圆上等概率的选3个点 构成锐角三角形的概率 (现场推导)

   > 求圆上任取三个点组成锐角三角形的概率（答案：1/4，参考：https://zhuanlan.zhihu.com/p/69530841）
   > （直角三角形显然概率为0，每个锐角三角形，将三个顶点依次和圆心做对称可以映射到三个钝角三角形，说明锐角三角形的概率和钝角三角形的概率是1:3，所以是1/4）
   > （等价为：任取三角形，圆心落在三角形内、外、边上的概率各是多少）
   > 圆上任选三点组成三角形，求三角形的面积的数学期望。
   > （求面积期望可以分成锐角三角形和钝角三角形两种情况，锐角三角形从圆心将三角形分成三份，面积是三份和；钝角三角形分开后，面积是两份和减去一份差。三角形面积sinα / 2，期望值为1/π，所以结果就是(1/4 * 3 + 3/4) / π = 3/(2π)）
   > 强化版：在一个球面任取4个点，请问这4个点构成的4面体会经过球心的概率。（1/8）
   > （面积法，大三角形面积，等于三个小三角形面积之和，注意浮点数，面积由海伦公式求解）
   > （求直线方程，判断点位于三条直线的什么方向）
   > （矢量叉乘，判断点是否在线段AB的左侧）

4. 如何在圆内随机取点，蠡口原题。（Leetcode:478. 在圆内随机生成点，利用极坐标，一个半径，一个角度）

### 概率题

1. 50个红球与50个白球，放入两个盒子，要求每个盒子至少有一个球。拿的时候随机在其中一个盒子内，随机拿出一个球。请问如何摆放这些球，让拿出的是红球的概率最大。