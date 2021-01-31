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

### 常见数据结构

### 字符串

### 链表

### 树

### 图

### 更加复杂的数据结构

## 第二部分：算法

### 贪心

| 题目链接                                                     | 难度   | 个人题解    | 说明     |
| ------------------------------------------------------------ | ------ | ----------- | -------- |
| [605. 种花问题](https://leetcode-cn.com/problems/can-place-flowers/) | simple | cpp, python | 分配问题 |
| [135. 分发糖果](https://leetcode-cn.com/problems/candy/)     | hard   | cpp, python | 分配问题 |
| [455. 分发饼干](https://leetcode-cn.com/problems/assign-cookies/) | simple | cpp, python | 分配问题 |
| [435. 无重叠区间](https://leetcode-cn.com/problems/non-overlapping-intervals/) | medium | cpp,python  | 区间问题 |
| [452. 用最少数量的箭引爆气球](https://leetcode-cn.com/problems/minimum-number-of-arrows-to-burst-balloons/) | medium | cpp,python  | 区间问题 |
| [763. 划分字母区间](https://leetcode-cn.com/problems/partition-labels/) | medium | cpp,python  | 区间问题 |
| [122. 买卖股票的最佳时机 II](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/) | easy   | cpp,python  | 其它     |
| [665. 非递减数列](https://leetcode-cn.com/problems/non-decreasing-array/) | easy   | cpp,python  | 其它     |
| [406. 根据身高重建队列](https://leetcode-cn.com/problems/queue-reconstruction-by-height/) | medium | cpp,python  | 其它     |
| 后续待刷的题目：                                             |        |             |          |
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

### 双指针

| 题目链接                                                     | 难度   | 个人题解   | 说明     |
| ------------------------------------------------------------ | ------ | ---------- | -------- |
| [1. 两数之和](https://leetcode-cn.com/problems/two-sum/)     |        |            | N数之和  |
| [167. 两数之和 II - 输入有序数组](https://leetcode-cn.com/problems/two-sum-ii-input-array-is-sorted/) | easy   | cpp,python | N数之和  |
| [633. 平方数之和](https://leetcode-cn.com/problems/sum-of-square-numbers/) | medium | cpp,python | N数之和  |
| [15. 三数之和](https://leetcode-cn.com/problems/3sum/)       |        |            | N数之和  |
| [16. 最接近的三数之和](https://leetcode-cn.com/problems/3sum-closest/) |        |            | N数之和  |
| [18. 四数之和](https://leetcode-cn.com/problems/4sum/)       |        |            | N数之和  |
| [454. 四数相加 II](https://leetcode-cn.com/problems/4sum-ii/) |        |            | N数之和  |
| [142. 环形链表 II](https://leetcode-cn.com/problems/linked-list-cycle-ii/) | medium | cpp,python | 快慢指针 |
| [141. 环形链表](https://leetcode-cn.com/problems/linked-list-cycle/) |        |            | 快慢指针 |
| [876. 链表的中间结点](https://leetcode-cn.com/problems/middle-of-the-linked-list/) |        |            | 快慢指针 |
| [202. 快乐数](https://leetcode-cn.com/problems/happy-number/) |        |            | 快慢指针 |
| 倒数第k个节点                                                |        |            | 快慢指针 |
| [3. 无重复字符的最长子串](https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/) |        |            | 滑动窗口 |
| [76. 最小覆盖子串](https://leetcode-cn.com/problems/minimum-window-substring/) | hard   | cpp,python | 滑动窗口 |
| 340. 至多包含 K 个不同字符的最长子串                         | hard   | cpp,python | 滑动窗口 |
| [125. 验证回文串](https://leetcode-cn.com/problems/valid-palindrome/) | easy   | cpp,python | 回文串   |
| [680. 验证回文字符串 Ⅱ](https://leetcode-cn.com/problems/valid-palindrome-ii/) | easy   | cpp,python | 回文串   |
| [524. 通过删除字母匹配到字典里最长单词](https://leetcode-cn.com/problems/longest-word-in-dictionary-through-deleting/) | medium | cpp,python | 字符串   |
| [88. 合并两个有序数组](https://leetcode-cn.com/problems/merge-sorted-array/) | easy   | cpp,python | 归并排序 |
| [845. 数组中的最长山脉](https://leetcode-cn.com/problems/longest-mountain-in-array/) |        |            |          |
| [830. 较大分组的位置](https://leetcode-cn.com/problems/positions-of-large-groups/) |        |            |          |
| [42. 接雨水](https://leetcode-cn.com/problems/trapping-rain-water/) |        |            |          |
| [844. 比较含退格的字符串](https://leetcode-cn.com/problems/backspace-string-compare/) |        |            |          |
| [925. 长按键入](https://leetcode-cn.com/problems/long-pressed-name/) |        |            |          |

### 二分查找

| 题目链接                                                     | 难度   | 个人题解   | 说明     |
| ------------------------------------------------------------ | ------ | ---------- | -------- |
| [69. x 的平方根](https://leetcode-cn.com/problems/sqrtx/)    | easy   | cpp,python | 常规二分 |
| [34. 在排序数组中查找元素的第一个和最后一个位置](https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/) | medium | cpp,python | 区间二分 |
| [33. 搜索旋转排序数组](https://leetcode-cn.com/problems/search-in-rotated-sorted-array/) |        |            |          |
| [81. 搜索旋转排序数组 II](https://leetcode-cn.com/problems/search-in-rotated-sorted-array-ii/) |        |            |          |
| [153. 寻找旋转排序数组中的最小值](https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array/) |        |            |          |
| [154. 寻找旋转排序数组中的最小值 II](https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array-ii/) |        |            |          |
| [540. 有序数组中的单一元素](https://leetcode-cn.com/problems/single-element-in-a-sorted-array/) |        |            |          |
| [4. 寻找两个正序数组的中位数](https://leetcode-cn.com/problems/median-of-two-sorted-arrays/) |        |            |          |
| [240. 搜索二维矩阵 II](https://leetcode-cn.com/problems/search-a-2d-matrix-ii/) |        |            |          |
| [378. 有序矩阵中第K小的元素](https://leetcode-cn.com/problems/kth-smallest-element-in-a-sorted-matrix/)（难，重点学习） |        |            |          |
| [475. 供暖器](https://leetcode-cn.com/problems/heaters/)     |        |            |          |
| 牛客比赛中出现的二分题目                                     |        |            |          |
| 寻找单个元素，寻找左边界，寻找右边界                         |        |            |          |

### 排序

### 搜索

### 动态规划

### 分治法

## 第三部分：数学

### 数学问题

### 位运算

## 第四部分：专题

| 题目链接 | 难度 | 个人题解 | 说明     |
| -------- | ---- | -------- | -------- |
|          |      |          | 股票买卖 |
|          |      |          | 石子游戏 |
|          |      |          | N数之和  |

