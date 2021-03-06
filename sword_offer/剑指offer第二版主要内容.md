# 剑指offer笔记

作者：xiaoli1368
邮箱：xiaoli1644@qq.com
日期：2020/06/07

## 前言

> 总结学习剑指offer中一些重要的笔记

## 目录

[TOC]

## 第1章：面试的流程

> 本章主要介绍了面试流程以及应试技巧。

对于初级程序员，一般考察算法和数据结构，对于高级程序员，一般考察专业技能和项目经验。

**面试的3种形式：**

- 电话面试
- 共享桌面远程面试
- 现场面试

**面试的3个环节：**

- 行为面试
- 技术面试
- 应聘者提问

**STAR模型简述项目经历：**（重点在TA）

- Situation：简短的项目北京
- Task：自己完成的任务
- Action：为了完成任务，自己做了哪些工作，是怎么做的
- Result：自己的贡献

**项目问题：**

- 在项目中碰到的最大问题
- 在项目中学到了什么
- 什么时候会和其它成员有冲突，如何解决（如QA）

**应聘者的5种素质：**

- 扎实的基础知识
- 能写高质量的代码
- 分析问题时思路清晰
- 能优化时间和空间效率
- 学习沟通等各方面能力

## 第2章：面试需要的基础知识

> 本章主要介绍了面试的基本知识，数据结构，算法基础。（含有对应例题）

**C++语言面试的3种类型：**

- 概念理解，如关键字
- 代码分析运行
- 手写代码

**C++推荐书籍：**

- 《Effective C++》（适合在面试前突击C++）
- 《C++ Primer》（全面了解C++）
- 《深度探索C++对象模型》（理解C++对象内部）
- 《The C++ Programming Language》（全面深入掌握C++）

**数据结构：**

- 数组和字符串是两种最基本的数据结构
- 链表和树是面试中出现频率最高的数据结构
- 栈是一个与递归紧密相关的数据结构
- 队列也与广度优先遍历BFS算法紧密相关

**面试题目：**

- 面试题1：赋值运算符函数

  > 题目：为一个class添加赋值运算函数

- 面试题2：实现单例模型

  > 题目：设计一个类，只能生成该类的一个实例
  >
  > 思路：必须把构造函数设为私有，以禁止他人创建实例。然后设置一个指针，通过判断指针是否为空，判断是否第一次调用这个类，这样控制是否可以getInstance()

- 面试题3：数组中重复的数字

  > 题目：找出数组中重复的数字，数组长度为n，元素范围是0 - n-1
  >
  > 思路：哈希，依次遍历归位法

- 面试题3-2：不修改数组找出重复的数字

  > 思路：哈希，二分查找，划分一个范围，搜索数字在这个范围内出现的次数

- 面试题4：二维数组中的查找

  > 题目：每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
  >
  > 思路：利用数组特点，从特定位置开始查找（右上或左下），不断缩小范围

- 面试题5：替换空格

  > 题目：将空格替换为"%20"
  >
  > 思路：考虑存储空间，第一次遍历获取长度，第二次遍历从后向前复制迭代

- 面试题5-2：合并两个排序数组

  > 思路：确保足够大的空间，从尾到头提取最大值赋值

- 面试题6：从尾到头打印链表

  > 思路：递归、堆栈

- 面试题7：重建二叉树

  > 题目：输入前序中序，重建二叉树
  >
  > 思路：递归，每次确定根节点，遍历获取划分的index，划分得到左右子树的前中序列，然后递归构建子树，使用python的list切片会很简单，使用c++传递索引边界会麻烦一些。
  >
  > 举一反三：使用前序和后序为什么不能唯一确定树，可能的解有哪些。

- 面试题8：二叉树的下一个节点

  > 题目：找出中序遍历的下一个节点
  >
  > 思路：分情况解决，不要怕麻烦。节点的右子树不为空，直接返回右子树的最左侧节点。右子树为空时，需要判断当前节点是父节点的哪一个子树，如果是左子树则直接返回父节点。如果是右子树，则迭代向上遍历，直到找到属于父节点的左子树情况，此时返回父节点即可，否则返回空。

- 面试题9：用两个栈实现一个队列

  > 题目：两个栈实现一个队列
  >
  > 思路：两个栈ab，入列对应入栈a，出列对应出栈b，如果b为空则把a所有元素出栈入栈到b，然后b出栈

- 面试题9-2：用两个队列实现一个栈

  > 题目：两个队列ab，入栈对应入列a，出栈则先把a的n-1个元素出列入列到b，然后把a的唯一一个元素出列。（也就是每次出栈后，两个队列必然有一个为空，则下一次入栈则入非空队列）

- 面试题10：斐波那契数列

  > 思路：递归，dp，迭代

- 面试题10-2：青蛙跳台阶问题

  > 思路：类似斐波那契数列，修改初始条件，递归，迭代

- 面试题10-3：变态跳台阶

  > 思路：数学推导得到通项公式，2^(n-1)

- 面试题10-4：矩形覆盖

  > 思路：类似斐波那契数列

- 面试题11：旋转数组的最小数字

  > 题目：有序数组一部分旋转到尾部后形成旋转数组，求最小数字
  >
  > 思路：二分查找，注意边界条件和缩小空间的迭代关系

- 面试题12：矩阵中的路径

  > 题目：给定二维矩阵，和一个字符串，判断矩阵中是否存在对应路径
  >
  > 思路：回溯法，递归，使用标记数组flag确保不重复遍历

- 面试题13：机器人的运动范围

  > 题目：从坐标（0，0）到（m，n）的方格中，机器人每次上下左右移动一步，不能进入两坐标数位之后大于k的格子，求最多覆盖多少个格子
  >
  > 思路：回溯法

- 面试题14：剪绳子

  > 题目：长为n的绳子，分为m段，未必等分，问各段乘积最大值
  >
  > 思路：贪心法（3为最优策略）、动态规划、寻找最优子问题、迭代关系。动态规划：dp[i] = max(dp[i], dp[i - j] * dp[j])，对每个i遍历j为[1, i // 2 + 1]

- 面试题15：二进制中1的个数

  > 思路：循环判断最后一位是否为1，n = n & (n-1)，可以应对负数

- 面试题15-2：判断整数是否为2的整数次方

  > 思路：return (n & (n-1)) == 0;

- 面试题15-3：求两个数二进制不同的位数

  > 思路：先异或获取不同的位数对应的二进制，然后求二进制中1的个数

## 第3章：高质量的代码

**代码的规范性：**

- 清晰的书写
- 清晰的布局
- 合理的命名

**代码的完整性：**

- 功能测试
- 边界测试
- 负面测试

**代码的鲁棒性：**

- 防御性编程
- 处理无效输入

**面试题目：**

- 面试题16：数值的整数次方

  > 题目：求base的exp次方
  >
  > 思路：快速幂，大数溢出问题，指数为负数问题

- 面试题17：打印从1到最大的n位数

  > 题目：如n为3，输出1，2，3，直到，999
  >
  > 思路：大数溢出问题，一在字符串上模拟加法，二把字符串对应的数字打印出来。（其它思路是递归全排列，注意消除前置0）

- 面试题17-2：两个大数相加

  > 思路：转为字符串相加

- 面试题18：删除链表的节点

  > 思路：拷贝下一个节点的值到当前节点，修改链接跳过下一个节点

- 面试题18-2：删除链表中重复的节点

  > 思路：考虑头节点也会删除（可以新建头节点），核心函数（查找当前节点的下一个不重复的节点，返回cnt, nextNode），修改链接（cnt为0，则curr = curr.next，不为0，则curr = nextNode，注意此时没有进行跳转，也就是还会对nextNode的重复性进行判断）

- 面试题19：正则表达式匹配

  > 题目：包含*和.的正则表达式匹配
  >
  > 思路：.简单，难的是\*，考虑\*的几种情况，使用递归求解，也可以使用dp

- 面试题20：表示数值的字符串

  > 题目：判断字符串是否为数值
  >
  > 思路：首先要明确正确的数值都是什么形式的，分情况讨论分析

- 面试题21：调整数组顺序使奇数位于偶数前

  > 思路：明确是否要保证内部的顺序？冒泡法（奇数向前冒泡，偶数向后冒泡），双指针法（会破坏顺序），辅助数组法（统计奇数、统计偶数、合并），其它条件（由区分奇偶，变为区分负数正数）

- 面试题22：链表中倒数第k个节点

  > 思路：双指针，先后指针（第一个指针先走k步，之后两个指针同步运动，最终第二个指针到达第k个节点）

- 面试题22-2：链表的中间节点

  > 思路：双指针，快慢指针，速度分别为1和2

- 面试题23：链表中环的入口节点

  > 思路：双指针，快慢指针，速度分别为1和2，相遇之后将一个指针移动到头节点，后续同步为速度1的运动，最终相遇到环的入口（原理为数学推导）

- 面试题24：反转链表

  > 思路：头插法新建一个反转链表，或者直接遍历建立反向链接

- 面试题25：合并两个排序的链表

  > 思路：递归合并
  >
  > 举一反三：合并两个有序数组（使用Python递归实现会很容易）
  >
  > 举一反三：合并K个有序链表（递归，归并排序，先合并两个（封装为函数），再合并k个）

- 面试题26：树的子结构

  > 思路：递归，注意要求空树不是任何树的子结构，因此需要定义额外的函数。

## 第4章：解决面试题的思路

**常见方法：**

- 画图
- 举例
- 分解

**面试题目：**

- 面试题27：二叉树的镜像

  > 题目：输入一颗二叉树，返回它的镜像
  >
  > 思路：递归交换左右子树的位置（引用链接），或者循环实现

- 面试题28：对称的二叉树

  > 思路：递归判断是否对称，与上同

- 面试题29：顺时针打印矩阵

  > 题目：顺时针打印二维矩阵
  >
  > 思路：简化为打印环的四条边，明确边界条件以及特殊情况
  >
  > 举一反三：将二维矩阵顺时针旋转90度

- 面试题30：包含min函数的栈

  > 题目：实现一个栈，要求可以实现O(1)的min函数
  >
  > 思路：常规栈，辅助最小栈（每次都把最小元素压入辅助栈，则可以保存每次的最小元素）

- 面试题31：栈的压入弹出序列

  > 思路：建立辅助栈模拟

- 面试题32：从上到下打印二叉树

  > 题目：按层次遍历，同层从左到右
  >
  > 思路：容器last保存上一层的节点值，遍历last，打印当前层的节点，同时初始化下一层的节点next，next赋值给last（其实这种容器是队列）
  >
  > 举一反三：如何bfs遍历一个有向图（基于队列实现，迭代遍历广度优先）

- 面试题32-2：分行从上到下打印二叉树

  > 思路：同上，无非修改了输出的形式为二维vector

- 面试题32-3：之字形打印二叉树

  > 思路：同上，使用flag区分打印的左右或者右左顺序，每一层都是反向遍历（其它思路：使用两个栈来迭代last和next层的节点）

- 面试题33：二叉搜索树的后序遍历序列

  > 题目：输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历结果
  >
  > 思路：尾部是根节点，从尾部开始遍历，将原数组划分为两部分，检测是否满足要求，递归再次检测

- 面试题33-2：二叉搜索树的前序遍历序列

  > 思路：与上题同，头部是根节点，改为从头部提取并遍历即可

- 面试题34：二叉树中和为某一路径

  > 思路：使用带记忆的DFS来解决，也就是深度优先的方法。可以使用两个函数实现，也可以利用一个函数递归实现。（递归，回溯）
  >
  > 举一反三：如果路径的端点未必是根节点和叶节点，但必须保证向下，则如何求解
  >
  > 举一反三2：如果路径未必是向下的，也可以是折线，则如何求解
  >
  > 举一反三3：求和最大的路径

- 面试题35：复杂链表的复制

  > 思路：哈希法，高效迭代法（每个节点向后复制，建立随机链接，整体分为两个链表）

- 面试题36：二叉搜索树与双向链表

  > 题目：二叉搜索树转换为双向（循环）链表
  >
  > 思路：（1）有序，需要使用递归中序遍历。（2）需要获取首尾节点，因此可以使用右中左的顺序，最终返回首节点
  >
  > 举一反三：转换为单向链表（左子树为空）

- 面试题37：序列化二叉树

  > 思路：使用`#,`这样以及先序序列的方式，对应解序列化，缺点是空节点占据了很多存储，使用层次遍历可以优化，但是code较为麻烦

- 面试题38：字符串的全排列

  > 思路：递归，把第一个字符逐一和它后面的字符交换

- 面试题38-2：字符串的全组合

  > 思路：同上

- 面试题38-3：正方体顶点问题

  > 思路：同上

- 面试题38-4：八皇后问题

  > 思路：同上（先求全排列，再判断是否满足要求）

## 第5章：优化时间和空间效率

**面试题目：**

- 面试题39：数组中出现次数超过一半的数字

  > 思路：基于快排分区，基于多数投票法

- 面试题40：最小的k个数

  > 思路：基于快排分区，基于大顶堆

- 面试题41：数据流中的中位数

  > 思路：两个堆，最大堆，最小堆

- 面试题42：连续子数组的最大和

  > 思路：动态规划，max记录比较过程中出现的最大值，sum记录当前的最大值，sum = max(sum + num[i], num[i])

- 面试题43：1-n整数中1出现的个数

  > 思路：从数字规律入手，思考1在各个数位上出现的情况

- 面试题44：数字序列中某一位的数字

  > 思路：找规律，数位为1时1\*9，数位为2时2\*90，数位为3时3\*900

- 面试题45：把数组排成最小的数

  > 思路：自定义新的比较大小规则，使用字符串处理大数溢出问题

- 面试题46：把数字翻译成字符串

  > 题目：给定一个数字，我们按照如下规则把它翻译为字符串：0 翻译成 “a” ，1 翻译成 “b”，……，11 翻译成 “l”，……，25 翻译成 “z”。一个数字可能有多个翻译。请编程实现一个函数，用来计算一个数字有多少种不同的翻译方法。如12258有5种不同的翻译，分别是"bccfi", "bwfi", "bczi", "mcfi"和"mzi"
  >
  > 思路：动态规划，定义dp(n)为索引为n处的结果，则当[n-1, n]不可以被翻译时，dp(n) = dp(n - 1)，否则dp(n) = dp(n - 1) + dp(n - 2)

- 面试题47：礼物的最大价值

  > 题目：二维数组（元素大于0）中找最大的路径和，每次向右或下运动一步
  >
  > 思路：直接dfs会超时，高效思路为动态规划，状态方程为：grid(i, j) += max(grid(i - 1, j), gird(i, j - 1))

- 面试题48：最长不含重复字符的子字符串

  > 思路：双指针滑窗 + 哈希表，或者动态规划 + 哈希表，较难
  >
  > 动态规划：dp[i]表示第i个字符结尾的最长不含重复字符的子字符串，dp[i]的值与两个遍历有关，一是dp[i-1]，二是上一个相同字符之间的距离i-j，如果dp[i-1] < i - j，则dp[i] = dp[i-1] + 1，否则dp[i] = j - i

- 面试题49：丑数

  > 题目：只含有2/5/7因子的数为丑数，输出第k个丑数
  >
  > 思路：三指针法

- 面试题50：第一个只出现一次的字符

  > 思路：哈希，char tmp[256]

- 面试题50-2：字符流中第一个只出现一个的字符

  > 思路：同上

- 面试题51：数组中的逆序对

  > 思路：归并排序

- 面试题52：两个链表的第一个公共节点

  > 思路：双指针，循环遍历（第一次找到长度差，第二次相遇在公共节点）

## 第6章：面试中的各项能力

**各项能力：**

- 沟通能力
- 学习能力
- 知识迁移能力
- 抽象建模能力
- 发散思维能力

**面试题目：**

- 面试题53：数字在排序数组中出现的次数

  > 思路：二分法查找左右边界

- 面试题53-2：0-n-1中缺失的数字

  > 思路：二分查找

- 面试题53-3：数组中数值和下标相等的元素

  > 思路：二分查找

- 面试题54：二叉搜索树的第k大节点

  > 思路：要求有序，所以中序遍历，外部变量记录索引。（也可以右中左遍历，直接记录第k大的节点）

- 面试题55：二叉树的深度

  > 思路：递归，返回 1 + max(left, right)

- 面试题55-2：平衡二叉树

  > 思路：递归，需要额外的统计深度的函数，自顶向下（存在冗余），或者自底向上（不满足则返回false提前退出）

- 面试题56：数组中数字出现的次数

  > 题目：求只出现一个的两个数字，其它数字都出现了两次
  >
  > 思路：首先异或获得a^b，将其作为flag，之后根据flag，将数组分为两部分，每部分各自异或，输出两个数字

- 面试题56-2：数组中唯一只出现一次的数字

  > 题目：数组中其它数字都出现了3次，只有一个数字出现了一次
  >
  > 思路：从二进制位入手，统计数组中所有数字，在不同二进制位上的累加出现次数，如果可以被3整除，则目标数字该位为，否则该位为1（需要一个32位的数组来保存每一位上的累加出现次数）

- 面试题57：和为s的数字

  > 题目：有序数组中求两个数字，之和为给定值
  >
  > 思路：双指针，分别从前后遍历

- 面试题57-2：和为s的连续正数序列

  > 思路：双指针，都从前开始遍历

- 面试题58：翻转字符串

  > 思路：两次翻转字符串

- 面试题58-2：左旋转字符串

  > 思路：三次翻转字符串

- 面试题59：滑动窗口的最大值

  > 思路：双端队列，保存最大值、次大值等等，两端删除，前端删除过期元素，后端删除较小的元素，每次从头部取最大值（比较高效）

- 面试题59-2：队列的最大值

  > 思路：辅助的双端队列，递减记录添加元素

- 面试题60：n个骰子的点数

  > 题目：把n个骰子扔在地上，所有骰子朝上一面的点数之和为s。输入n，打印出s的所有可能的值出现的概率。你需要用一个浮点数数组返回答案，其中第 i 个元素代表这 n 个骰子所能掷出的点数集合中第 i 小的那个的概率。
  >
  > 思路：动态规划对n个骰子可能的取值为[n, 6n]，关键是求组合次数
  >
  > `dp[i][j] = sum(k=1, k=6, dp[i-1][j-k])`，即本次的次数等于上一次的各种情况次数之和（注意本次与上次的联系在于，骰子个数减少1，并且和减少了k，k遍历取值1-6，同时存在隐含条件，骰子个数i不大于当前的点数和j，对上一次有：i - 1 <= j - k）

- 面试题61：扑克牌中的顺子

  > 思路：分析情况，综合处理

- 面试题62：圆圈中最后剩下的数字

  > 思路：约瑟夫环问题，找两次直接的迭代关系

- 面试题63：股票的最大利润

  > 题目：某股票的价格按照时间先后顺序存储在数组中，请问买卖该股票一次可能获得的最大利润是多少？
  >
  > 思路：动态规划，前i天的最大利润 = max(前i-1天的最大利润，当前价格 - 之前i天的最小价格)，因此需要一个额外变量来记录前i-1天的最小值，并且进行更新

- 面试题64：求1-n的和

  > 思路：利用&&短路特性实现递归

- 面试题65：不用加减乘除做加法

  > 思路：循环迭代实现多位二进制加法器

- 面试题66：构建乘积数组

  > 思路：左右两个方向遍历，期间完成累乘

- 面试题67：把字符串转换成整数

  > 思路：考虑各种情况

- 面试题68：二叉搜索树中两个节点的最低公共祖先

  > 思路：利用二叉搜索树特性，通过比较当前两个节点值与当前root节点值的大小关系，向下递归，搜索空间缩减为左子树或者右子树

- 面试题68：二叉树中两个节点的最低公共祖先

  > 思路：由于是普通的二叉树，因此无法直接通过与root节点对比从而缩小范围，只能完成搜索一遍后才能确定是否存在结果。
  >
  > 可以使用后序dfs遍历，根据左右子树是否分别包括两个节点，从而确定当前root是否为结果
