# LeetCode刷题笔记

作者：xiaoli1368
日期：2020/07/21
邮箱：xiaoli1644@qq.com

## 前言

> 关于LeetCode刷题中的思路整理，按类型分类。

## 目录

[TOC]

### 链表

#### [725. 分隔链表](https://leetcode-cn.com/problems/split-linked-list-in-parts/)

**解题思路：**

- 遍历得到最大长度
- 分配长度到每个子链表
- 遍历进行拆分

### 二叉树

### 单调栈

### 回溯法

#### [401. 二进制手表](https://leetcode-cn.com/problems/binary-watch/)

**解题思路：**

- 经典回溯思路
- 看作二进制序列的回溯
- 初始化将0放在前，1放在后，完成排序
- 期间需要进行剪枝
- 最终要完成字符串的转换