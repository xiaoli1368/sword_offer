# cracking_the_coding_interview
## 说明

> 《程序员面试金典》算法题的汇总，主要使用了Python和C++。

## 目录

[TOC]

## [面试题 01.07. 旋转矩阵](https://leetcode-cn.com/problems/rotate-matrix-lcci/)

**题目：**

> 给你一幅由 `N × N` 矩阵表示的图像，其中每个像素的大小为 4 字节。请你设计一种算法，将图像旋转 90 度。不占用额外内存空间能否做到？

**题解：**

直接二重循环，外层控制层数（由最外层到最里层），内层控制每条边需要选择的原始个数。在每个内层循环内，进行一个四元素的循环赋值即可。

## [面试题 03.01. 三合一](https://leetcode-cn.com/problems/three-in-one-lcci/)

**题目：**

> 三合一。描述如何只用一个数组来实现三个栈。
>
> 你应该实现push(stackNum, value)、pop(stackNum)、isEmpty(stackNum)、peek(stackNum)方法。stackNum表示栈下标，value表示压入的值。
>
> 构造函数会传入一个stackSize参数，代表每个栈的大小。

**题解：**

直接使用一个vector或者list即可，共三个栈，每个栈长度固定且等长，初始化数组的总长为 3 * size即可，后续的关键点在于push/pop的时候对下标的正确索引。

