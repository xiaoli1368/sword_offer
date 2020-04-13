# 剑指offer笔记

作者：xiaoli1368
日期：2020/02/23
邮箱：xiaoli1644@qq.com

## 目录
[TOC]

## 第一部分

### 01. 二维数组中的查找

**题目描述：**

> 在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

**解题思路：**

- 直接的方式就是暴力枚举
- 最优的策略是利用矩阵的有序性，从而实现更快的检测。（矩阵的L型结构都是有序的，反L也是有序的，因此可以从左下角开始查找，或者从右上角开始查找）

**参考代码：**

```python
# 这一版比较低级
# 从左上角开始查找，相等则退出
# 更大时则优先向右移动，遇到边界开始向下移（使用flag记录比较的方向，向右还是向下）
# 变小时向下移动
# 如果是连续两次都是变小，此时根据flag则应进行左移动

# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        i = 0
        j = 0
        dire = 0
        ilen = len(array)
        jlen = len(array[0])
        while (i < ilen and j < jlen and i >= 0 and j >= 0):
            if target == array[i][j]:
                return True
            elif target > array[i][j] and j + 1 < jlen:
                j += 1
                dire = 0
            elif target > array[i][j] and j + 1 == jlen:
                i += 1
                dire = 1
            elif target < array[i][j] and dire == 0:
                i += 1
                j -= 1
                dire = 1
            elif target < array[i][j] and dire == 1:
                j -= 1
        return False
```

```python
# 这个是高效的算法
# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        i = 0
        j = len(array[0]) - 1
        while (i < len(array) and j >= 0):
            if target == array[i][j]:
                return True
            elif target < array[i][j]:
                j -= 1
            else:
                i += 1
        return False
```

```c++
class Solution {
public:
    bool Find(int target, vector<vector<int> > array) {
        int i = 0;
        int j = array[0].size() - 1;
        while (i < array.size() && j >= 0) {
            if (target == array[i][j]) {
                return true;
            } else if (target < array[i][j]) {
                j--;
            } else {
                i++;
            }
        }
        return false;
    }
};
```

### 02. 替换空格

**题目描述：**

> 请实现一个函数，将一个字符串中的每个空格替换成“%20”。例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。

**解题思路：**

- 这道题原本的字符串会增长，因此需要动态的空间，事实上测试端已经事先设定了足够大的字符串数组，因此不需要考虑这些情况。
- 注意高效的思路是，第一次循环确定空格数量从而明确最终的字符串长度，第二次循环从尾到头实现搬移

**参考代码：**

```python
#!bin/bash python3
# -*- coding:utf-8 -*-

class Solution:
    def replaceSpace(self, s):
        return s.replace(" ", "%20")

    def replaceSpace2(self, s):
        tmp = ""
        for i in s:
            if i == " ":
                tmp += "%20"
            else:
                tmp += i
        return tmp


def main():
    s = Solution()
    input_str = " A B "
    print(s.replaceSpace(input_str))
    print(s.replaceSpace2(input_str))


if __name__ == "__main__":
    main()
```

```c++
#include <stdio.h>
#include <iostream>
#include <string>

class Solution {
public:
    void replaceSpace(char *str, int length) {
        int count = 0;
        for (int i = 0; i < length; i++) {
            if (str[i] == ' ') {
                count++;
            }
        }
        int j = length + 2 * count;
        str[j] = '\0';
        for (int i = length - 1; i >= 0; i--) {
            if (str[i] == ' ') {
                str[--j] = '0';
                str[--j] = '2';
                str[--j] = '%';
            } else {
                str[--j] = str[i];
            }
        }
    } 

    // c++形式
    // 借助额外空间
    void replaceSpace2(std::string& str) {
        std::string tmp = "";
        for (auto i : str) {
            if (i == ' ') {
                tmp += "%20";
            } else {
                tmp += i;
            }
        }
        str = tmp;
    }

    // c++形式
    // 减少额外空间的使用
    void replaceSpace3(std::string& str) {
        int length = str.length();
        for (int i = 0; i < length; i++) {
            if (str[i] == ' ') {
                str.append("  ");
            }
        }
        // 从后端开始搬移
        int j = str.length(); 
        for (int i = length - 1; i >= 0; i--) {
            if (str[i] == ' ') {
                str[--j] = '0';
                str[--j] = '2';
                str[--j] = '%';
            } else {
                str[--j] = str[i];
            }
        }
    }
};

int main(int argc, char* argv[])
{
    Solution s;
    char input_str[100]= " A B \0";
    s.replaceSpace(input_str, 5);
    printf("%s\n", input_str);

    // c++形式
    std::string in_str = " A B ";
    s.replaceSpace2(in_str);
    std::cout << in_str << std::endl;

    std::string in_str2 = " A B ";
    s.replaceSpace3(in_str2);
    std::cout << in_str2 << std::endl;

    return 0;
}
```

### 03. 从头到尾打印链表

**题目描述：**

> 输入一个链表，按链表从尾到头的顺序返回一个ArrayList。

**解题思路：**

- 第一中方式是递归
- 第二种方式是两次遍历，一次遍历原来的链表反向，之后遍历正序输出
- 或者直接每次都在vector的头部插入元素就可以了
- 还有一种方式正序输出到vector，之后将vector反向即可
- 利用头插法生成反向链表，或者使用堆栈进行反向输出

**参考代码：**

```python
# 类内递归，函数调用自身需要使用vec
# 'NoneType' object is not iterable，这个错误一般是函数情况没有考虑好
# 导致有一种情况默认返回了None，与后续的类型没有匹配
class ListNode():
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        vec = []
        if listNode is not None:
            vec += self.printListFromTailToHead(listNode.next)
            vec.append(listNode.val)
        return vec
```

```c++
// 局部变量被输出了其实是有问题的
// 除非外部将局部变量完成了赋值（值传递），内层的局部变量自动释放了，此时没有问题
class Solution {
public:
    vector<int> printListFromTailToHead(ListNode* head) {
        vector<int> vec =　{};
        vector<int> vec2 = {};
        if (head != nullptr) {
            vec2 = printListFromTailToHead(head->next);
            vec.insert(vec.end(), vec2.begin(), vec2.end());
            vec.push_back(head->val);
        }
        return vec;
    }
    
    // 这样更好，不用递归
    vector<int> printListFromTailToHead(ListNode* head) {
        vector<int> vec;
        while (head != nullptr) {
            vec.insert(vec.begin(), head->val);
            head = head->next;
        }
        return vec;
    }
};
```

### 04. 重建二叉树

**题目描述：**

> 输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。

**解题思路：**

- 明确什么是树，这种数据结构采用c++/python该如何实现
- 树的三种遍历方式，分别如何编程实现
- 三种遍历方式中的关系，已知两个顺序，重建整个二叉树
- 注意题目限制：前序和中序的数字不是重复的

**解题思路2：**

- 设前序数组为pre，中序数组为vin
- 寻找pre[0]在vin中的位置，这样就能完成一次划分了
- 将当前的两个数组pre/vin，划分为下一次迭代的四个数组，newLeftPre，newLeftVin，newRightPre，newRightVin
- 完成对当前根节点的构建和赋值，对左右两个子节点，当对应数组的size不为零时，进行下一次的迭代
- 整体的退出条件为：当pre和vin的size都为１时，仅构建根节点并退出（两个孩子节点为null）

**参考代码：**

```python
// 一次就过，nice
/**
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    TreeNode* reConstructBinaryTree(vector<int> pre,vector<int> vin) {
        TreeNode* newTree = new TreeNode(pre[0]);
        if (pre.size() == 1 && vin.size() == 1) {
            return newTree;
        }
        
        int index = 0;
        for (auto i : vin) {
            if (i != pre[0]) {
                index++;
            } else {
                break;
            }
        }
        
        vector<int> newLeftPre, newLeftVin, newRightPre, newRightVin;
        newLeftPre.assign(pre.begin() + 1, pre.begin() + 1 + index);
        newRightPre.assign(pre.begin() + 1 + index, pre.end());
        newLeftVin.assign(vin.begin(), vin.begin() + index);
        newRightVin.assign(vin.begin() + 1 + index, vin.end());
        
        if (newLeftPre.size() != 0) {
            newTree->left = reConstructBinaryTree(newLeftPre, newLeftVin);
        }
        if (newRightPre.size() != 0) {
            newTree->right = reConstructBinaryTree(newRightPre, newRightVin);
        }
        
        return newTree;
    }
};
```

```c++
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        newTree = TreeNode(pre[0])
        newTree.left = None
        newTree.right = None
        
        if len(pre) == 1 and len(tin) == 1:
            return newTree
        
        index = 0
        for i in tin:
            if i != pre[0]:
                index += 1
            else:
                break
        
        newLeftPre = newLeftTin = newRightPre = newRightTin = []
        newLeftPre = pre[1:1+index]
        newRightPre = pre[1+index:]
        newLeftTin = tin[:index]
        newRightTin = tin[index+1:]
        
        if newLeftPre:
            newTree.left = self.reConstructBinaryTree(newLeftPre, newLeftTin)
        if newRightPre:
            newTree.right = self.reConstructBinaryTree(newRightPre, newRightTin)
        
        return newTree
```

### 05. 用两个栈实现一个队列

**题目描述：**

> 用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。

**解题思路：**

- 使用两个堆栈，借助两次入栈出栈就可以实现一个队列
- 入列：无脑进入堆栈1即可
- 出列：如果堆栈2非空，堆栈2出栈即可，如果堆栈2为空，则将堆栈1的序列循环出栈，并入栈进入堆栈2，然后再调用这个出列函数
- 注意c++可以调用STL中的\<stack>来实现基本的堆栈操作
- 注意pop()是出栈操作，但不返回值。top()操作是返回栈顶的值，但是不会出栈

**参考代码：**

```c++
class Solution
{
public:
    void push(int node) {
        stack1.push(node);
    }

    int pop() {
        if (stack2.size() != 0) {
            int tmp = stack2.top();
            stack2.pop();
            return tmp;
        }
        
        int length = stack1.size();
        if (length != 0) {
            for (int i = 0; i < length; i++) {
                int tmp = stack1.top();
                stack1.pop();
                stack2.push(tmp);
            }
            return pop();
        }
    }

private:
    stack<int> stack1;
    stack<int> stack2;
};
```

```python
# 这种方式是直接实现了一个队列
# 使用两个栈来实现队列的方式见文件夹下代码

# -*- coding:utf-8 -*-
class Solution:
    def __init__(self, value=0):
        self.val = value
        self.next = None
        
    def push(self, value):
        newQueue = Solution(value)
        newQueue.next = self.next
        self.next = newQueue
    
    def pop(self):
        if self.next == None:
            return
        
        tmpNode = self
        tmpVal = 0
        
        while tmpNode.next.next != None:
            tmpNode = tmpNode.next
            
        tmpVal = tmpNode.next.val
        tmpNode.next = None
        return tmpVal
    
# 这是参考答案
class Solution:
    """
    用两个栈实现一个队列的高效率版
    """
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, value):
        self.stack1.append(value)

    def pop(self):
        if len(self.stack2) != 0:
            return self.stack2.pop()
        
        length = len(self.stack1)
        if length != 0:
            for i in range(length):
                self.stack2.append(self.stack1.pop())

        return self.pop()
```

### 06. 旋转数组的最小数字

**题目描述：**

> 把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。输入一个非递减排序的数组的一个旋转，输出旋转数组的最小元素。例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。

**解题思路：**

- 这道题一开始没有思路（能够想到是二分折半），直接采用暴力枚举的方式做的，没想到还通过了
- 高效思路是，每次进行折半划分，确定两边的子数组，哪个是非递减数组，哪个是新的旋转数组（旋转数组的首元素大于尾部元素）
- 注意特殊情况是相等，此时无法进行数组划分，因此需要采用常规查找
- 对于二分查找，有几个需要注意的边界问题，中间middle的取值，可以有两种形式，(low+right)/2或者(row+right+1)/2，可以发现当范围逐渐缩小到有两个值时（row/right），此时的middle在两种形式下分别对应row和right
- 另外一个注意的地方就是，缩小范围时的判断条件。假设当首元素小于尾元素，则认为这一段数据是递增的。那么区分当前数组的判断添加有两个，将row与middle比较，或者将middle与high比较。注意这两种情况与middle的取值情况应该对应，同时也会具备不同的迭代方式。
- 主要考察的内容就是二分查找的深层次运用

**参考代码：**

```c++
// 暴力查找版本
class Solution {
public:
    int minNumberInRotateArray(vector<int> rotateArray) {
        int length = rotateArray.size();
        if (length == 0) {
            return 0;
        }
        for (int i = 0; i < length - 1; i++) {
            if (rotateArray[i] > rotateArray[i + 1]) {
                return rotateArray[i + 1];
            }
        }
        return rotateArray[0];
    }
};

// 高效版本
class Solution {
public:
    int minNumber(vector<int> array, int low, int high) {
        int tmp = array[low];
        for (int i = 0; i <= high; i++) {
            if (array[i] < tmp) {
                tmp = array[i];
            }
        }
        return tmp;
    }
    
    int minNumberInRotateArray(vector<int> array) {
        int length = array.size();
        if (length == 0) {
            return 0;
        }
        
        int low = 0;
        int high = length - 1;
        while (low < high) {
            int middle = (low + high + 1) / 2;
            if (array[low] == array[middle] && array[middle] == array[high]) {
                return minNumber(array, low, high);
            } else if (array[low] <= array[middle]) {
                low = middle;
            } else {
                if (low + 1 == middle) {
                    low++;
                }
                high = middle;
            }
        }
        return array[low];
    }
};

// 参考答案
class Solution {
public:
    int minNumber(vector<int> array, int low, int high) {
        int tmp = array[low];
        for (int i = 0; i <= high; i++) {
            if (array[i] < tmp) {
                tmp = array[i];
            }
        }
        return tmp;
    }
    
    int minNumberInRotateArray(vector<int> array) {
        int length = array.size();
        if (length == 0) {
            return 0;
        }
        
        int low = 0;
        int high = length - 1;
        while (low < high) {
            int middle = (low + high) / 2;
            if (array[low] == array[middle] && array[middle] == array[high]) {
                return minNumber(array, low, high);
            } else if (array[middle] >= array[high]) {
                low = middle + 1;
            } else {
                high = middle;
            }
        }
        return array[low];
    }
};
```

```python
# 暴力查找版本
# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code hereA
        if rotateArray == []:
            return 0
        for i in range(len(rotateArray) - 1):
            if rotateArray[i] > rotateArray[i + 1]:
                return rotateArray[i + 1]
        return rotateArray[0]
    
# 高效版本
# -*- coding:utf-8 -*-
class Solution:
    def minNumber(self, array, low, high):
        tmp = array[low]
        while low <= high:
            if array[low] < tmp:
                tmp = array[low]
            low += 1
        return tmp

    def minNumberInRotateArray(self, array):
        # write code here
        length = len(array)
        if length == 0:
            return 0
        
        low = 0
        high = length - 1
        while low < high:
            middle = (low + high) // 2 
            if array[low] == array[middle] and array[middle] == array[high]:
                return self.minNumber(array, low, high)
            elif array[middle] >= array[high]:
                low = middle + 1
            else:
                high = middle
        return array[low]
```

### 07. 斐波那契数列

**题目描述：**

> 大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项（从0开始，第0项为0）。n<=39

**解题思路：**

- 不能使用递归，递归方式编程简单，但是会严重超时
- 因此只能开始一个新的数组空间，不断迭代并保存值到数组，最终获得结果
- 更加高效的方式是使用三个临时变量来相互迭代，而不是使用数组

**参考代码：**

```python
class Solution():
    def Fibonacci(self, n):
        """
        迭代的方式，花时间很长
        """
        if n < 2:
            return n
        else:
            return self.Fibonacci(n-1) + self.Fibonacci(n-2)

    def Fibonacci2(self, n):
        """
        使用列表存储并迭代的方式
        """
        if n < 2:
            return n
        else:
            array = [0, 1]
            while len(array) - 1 < n:
                array.append(array[-2] + array[-1])
            return array[-1]

    def Fibonacci3(self, n):
        """
        参考答案，更加高效的方式
        """
        array = [0, 1]
        if n >= 2:
            for i in range(2, n + 1):
                array[i%2] = array[0] + array[1]
        return array[n%2]

    def Fibonacci4(self, n):
        """
        另一种方式
        """
        if n < 2:
            return n
        else:
            a = 0
            b = 1
            c = 0
            for i in range(n-1):
                c = a + b
                a = b
                b = c
            return c
```

```c++
class Solution {
public:
    // 递归的方式
    int Fibonacci(int n) {
        if (n < 2) {
            return n;
        }
        return Fibonacci(n-1) + Fibonacci(n-2);
    }

    // 数组存储的方式
    int Fibonacci2(int n) {
        if (n < 2) {
            return n;
        }
        std::vector<int> vec = {0, 1};
        for (int i = 0; i < n-1; i++) {
            vec.push_back(vec.back() + vec.at(vec.size() - 2));
        }
        return vec.back();
    }

    // 更为高效的方式
    int Fibonacci3(int n) {
        if (n < 2) {
            return n;
        }
        int a = 0, b = 1, c = 0;
        for (int i = 0; i < n-1; i++) {
            c = a + b;
            a = b;
            b = c;
        }
        return c;
    }
}
```

### 08. 跳台阶

**题目描述：**

> 一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）。

**解题思路：**

- 与斐波那契数学的原理一致，区别在于斐波那契数列的前三项为[0, 1, 1]，本题的前三项为[0, 1, 2]
- 后续都是依次叠加的套路

**参考代码：**

```python
# -*- coding:utf-8 -*-
class Solution:
    def jumpFloor(self, n):
        # write code here
        if n < 3:
            return n
        else:
            a = 1
            b = 2
            c = 3
            for i in range(n-2):
                c = a + b
                a = b
                b = c
            return c
```

```c++
class Solution {
public:
    int jumpFloor(int n) {
        if (n < 3) {
            return n;
        }
        
        int a = 1, b = 2, c = 3;
        for (int i = 0; i < n - 2; i++) {
            c = a + b;
            a = b;
            b = c;
        }
        return c;
    }
};
```

### 09. 变态跳台阶

**题目描述：**

> 一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳法。

**解题思路：**

- 可以通过写出前几项找规律，或者推到递推公式的方式，来发现，结果就是2的等比序列。

- 一种思路是通过排列组合，如对于n=15的情况，跳的次数最多的情况是，全部跳1阶且跳15次，以这种情况作为基础。那么考虑1次跳完的情况只能是跳15，此时可以认为情况数是C(15, 0)。之后考虑跳2次跳完的情况，这意味着需要在原来分离的15个台阶中插入一个界限，界限前后的台阶分别合并为一次跳完，总共两次跳完，此时的情况数为C(15, 1)，依次类推，后续的全部情况为(1+1)的15次方展开。因此对于n阶的情况就是2^n。
- 可以考虑递推公式，f(n-1) = f(n-2)+f(n-3)+...+f(0)，f(n) = f(n-1)+f(n-2)+f(n-3)+...+f(0)，由此可见f(n)=2*f(n-1)，是一个等比序列，公比为2。

**参考代码：**

```python
# -*- coding:utf-8 -*-
class Solution:
    def jumpFloorII(self, number):
        # write code here
        if number == 0:
            return 0
        else:
            return 2**(number-1)
```

```c++
class Solution {
public:
    int jumpFloorII(int number) {
        if (number == 0) {
            return 0;
        } else {
            int tmp = 1;
            for (int i = 0; i < number - 1; i++) {
                tmp *= 2;
            }
            return tmp;
        }
    }
};
```

### 10. 矩形覆盖

**题目描述：**

> 我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？

**解题思路：**

- 考虑矩形方格为n*2，宽为n，高为2，此时考虑第一个填充的小矩形1\*2，有两种方式，立起来（1\*2）或者躺起来（2\*1）。
- 对于立起来的情况，剩余的矩形面积为(n-1)*2
- 对于躺起来的情况，由于要求无覆盖填充，因此必须第二个对应的小矩形也躺起了，和第一个小矩形对齐，因此剩余的矩形面积为(n-2)*2
- 因此递推公式为f(n) = f(n-1) + f(n-2)
- 因此本题仍然是类似斐波那契数列，前三项为[0, 1, 2]

**参考代码：**

- 见《09. 变态跳台阶》

### 11. 二进制中的1

**题目描述：**

> 输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。

**解题思路：**

- 首先要考虑将负数转为补码表示（c++直接使用unsigned int，python需要借助0xffffffff）
- 两种思路，暴力枚举的方式是不断的进行整除2以及右移一位，统计1的个数
- 另外一种思路是，循环使用 n&(n-1) != 0 可以消去原来数中的一位1（注意这种方式运算更快，每次消掉一位1，而且不用考虑符号的问题，但是python的与操作比较特殊，因此仍然需要转换符号）

**参考代码：**

```python
class Solution():
    def NumberOf1(self, n):
        """
        注意与操作0xffffffff
        这样并不是获得了一个补码
        而是获得了一个正数，这个正数与n的补码具有相同个数的1
        """
        result = 0
        if n < 0:
            n = n & 0xffffffff
        while n > 0:
            if n & 1 == 1:
                result += 1
            n = n >> 1
        return result

    def NumberOf1_easy(self, n):
        """
        高效解法
        """
        cnt = 0
        if n < 0:
            n = n & 0xffffffff
        while n != 0:
            cnt += 1
            n = n & (n - 1)
        return cnt
```

```c++
class Solution {
public:
    int NumberOf1(int n) {
        // c++需要转换类型
        unsigned int tmp = n;
        int result = 0;
        while (tmp > 0) {
            if (tmp & 1 == 1) {
                result++;
            }
            tmp >>= 1;
        }
        return result;
    }

    int NumberOf1_easy(int n) {
        // 这种方式不需要转换符号
        int cnt = 0;
        while (n != 0) {
            cnt++;
            n &= (n - 1);
        }
        return cnt;
    }
};
```

### 12. 数值的整数次方

**题目描述：**

> 给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。
>
> 保证base和exponent不同时为0

**解题思路：**

- 直接使用循环完成连乘即可
- 注意指数为负数的特殊情况

**参考代码：**

```python
class Solution():
    def Power(self, base, exponent):
        """
        直接使用内置运算符号
        """
        return base**exponent

    def Power2(self, base, exponent):
        """
        自行实现
        """
        if exponent == 0:
            return 1.0
        
        sign = False
        if exponent < 0:
            sign = True
            exponent = -exponent

        result = 1.0
        for i in range(exponent):
            result *= base

        if sign:
            result = 1 / result

        return result
```

```c++
class Solution {
public:
    double Power(double base, int exponent) {
        if (exponent == 0) {
            return 1.0;
        }

        bool sign = false;
        if (exponent < 0) {
            sign = true;
            exponent = -exponent;
        }

        double result = 1.0;
        for (int i = 0; i < exponent; i++) {
            result *= base;
        }

        if (sign) {
            result = 1 / result;
        }

        return result;
    }
};
```

### 13. 调整数组顺序使奇数位于偶数前面

**题目描述：**

> 输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分，所有的偶数位于数组的后半部分，并保证奇数和奇数，偶数和偶数之间的相对位置不变。

**解题思路：**

- 借助两个额外的数组完成添加操作，最终合并两个数组
- 借助一个数组，两次遍历，第一次遍历确定奇偶分界线的索引，第二次遍历进行添加
- 使用冒泡思想，每次将当前偶数上浮到当前最右边，时间换空间
- 可以对冒泡算法进行部分的次数优化

**参考代码：**

```python
class Solution:
    def reOrderArray(self, array):
        # write code here
        tmp1 = []
        tmp2 = []
        for i in array:
            if i % 2 == 1:
                tmp1.append(i)
            else:
                tmp2.append(i)
        return tmp1 + tmp2
```

```c++
class Solution {
public:
    void reOrderArray(vector<int> &array) {
        vector<int> tmp1, tmp2;
        for (auto i : array) {
            if (i % 2 == 1) {
                tmp1.push_back(i);
            }
            if (i % 2 == 0) {
                tmp2.push_back(i);
            }
        }
        tmp1.insert(tmp1.end(), tmp2.begin(), tmp2.end());
        array = tmp1;
    }
};
```

### 14. 链表倒数第k个节点

**题目描述：**

> 输入一个链表，输出该链表中倒数第k个结点。

**解题思路：**

- 第一种方式是：使用数组将所有节点存储下来，之后索引倒数第k个
- 第二种方式是：使用间距为k的两个指针进行遍历，当后一个指针到底尾部的时候，第一个指针刚好到达倒数第k个

**参考代码：**

```python
class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        p = head
        q = head
        count = 0
        
        while p:
            count += 1
            p = p.next
            if count > k:
                q = q.next
        
        if k < 0 or k > count:
            q = None
        return q
```

```c++
class Solution {
public:
    ListNode* FindKthToTail(ListNode* head, unsigned int k) {
        ListNode* p = head;
        ListNode* q = head;
        
        int count = 0;
        while (p) {
            count++;
            p = p->next;
            if (count > k) {
                q = q->next;
            }
        }
        
        if (k > count) {
            q = nullptr;
        }
        return q;
    }
};
```

### 15. 反转链表

**题目描述：**

> 输入一个链表，反转链表后，输出新链表的表头。

**解题思路：**

- 使用双指针完成，链表相邻节点之间的关系拆除，反向建立链接
- 注意头节点需要特殊对待
- 注意停止循环的标志

**参考代码：**

```python
class Solution:
    # 返回ListNode
    def ReverseList(self, head):
        # write code here
        if head == None:
            return None
        
        p = head
        q = head.next
        head.next = None
        
        while q != None:
            tmp = q.next
            q.next = p
            p = q
            q = tmp
            
        return p
```

```c++
class Solution {
public:
    ListNode* ReverseList(ListNode* head) {
        if (head == nullptr) {
            return nullptr;
        }
        
        ListNode* p = head;
        ListNode* q = head->next;
        head->next = nullptr;
        
        while (q) {
            ListNode* tmp = q->next;
            q->next = p;
            p = q;
            q = tmp;
        }
        
        return p;
    }
};
```

### 16. 合并两个排序的链表

**题目描述：**

> 输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。

**解题思路：**

- 递归：分解为更小的两个链表之间的合并问题（这个问题有些类似合并两个有序的列表list，递归更加简单，迭代要考虑各种边界条件）
- 迭代

**参考代码：**

```python
def Merge(self, pp, qq):
    """
    合并两个递增的链表，递归法
    """
    # 使用深拷贝隔绝对外界的影响
    p = copy.deepcopy(pp)
    q = copy.deepcopy(qq)

    if p == None:
        return q
    if q == None:
        return p
    if p.val < q.val:
        p.next = self.Merge(p.next, q)
        return p
    else:
        q.next = self.Merge(p, q.next)
        return q

def Merge2(self, pp, qq):
    """
    合并两个递增链表，迭代法
    """
    # 使用深拷贝隔绝对外界的影响
    p = copy.deepcopy(pp)
    q = copy.deepcopy(qq)

    head = ListNode(0)
    tmp = head
    while p != None and q != None:
        if p.val < q.val:
            tmp.next = p
            p = p.next
        else:
            tmp.next = q
            q = q.next
        tmp = tmp.next
    if p == None:
        tmp.next = q
    if q == None:
        tmp.next = p
    return head.next
```

```c++
// 合并两个递增链表，递归法
// 这种方式会对原始链表造成破坏
ListNode* Merge(ListNode* p, ListNode* q) {
    if (p == nullptr) {
        return q;
    }
    if (q == nullptr) {
        return p;
    }
    if (p->val < q->val) {
        p->next = Merge(p->next, q);
        return p;
    } else {
        q->next = Merge(q->next, p);
        return q;
    }

}

// 合并两个递增链表，迭代法
// 这种方式也会破坏链表
ListNode* Merge2(ListNode* p, ListNode* q) {
    ListNode* head = new ListNode(0);
    ListNode* tmp = head;

    while (p != nullptr && q != nullptr) {
        if (p->val < q->val) {
            tmp->next = p;
            p = p->next;
        } else {
            tmp->next = q;
            q = q->next;
        }
        tmp = tmp->next;
    }

    if (p == nullptr) {
        tmp->next = q;
    }
    if (q == nullptr) {
        tmp->next = p;
    }

    return head->next;
}
```

### 17. 树的子结构

**题目描述：**

> 输入两棵二叉树A，B，判断B是不是A的子结构。（ps：我们约定空树不是任意一个树的子结构）

**解题思路：**

- 注意子结构可以只是一部分，而非是剩下的全部
- 可以使用递归去做，依次比较a和b节点的数据值是否相等，如果相等，则返回 func(a.left, b.left) && func(a.right, b.right)，即继续比较a和b的左右子树是否为包含关系。如果二者不等，则返回 func(a.left, b) || func(a.right, b)，即查看a的左右子树中是否存在一个包含b。
- 问题的难点就在于约定了空树不是任何树的子结构，但是递归到最后，返回的条件恰恰就是空树是任何树的子结构。因此需要处理这种矛盾。
- 一种解决方式是：保持空树不是任何树的子结构，当两个比较节点的值相等时，根据b的左右子树是否为空树，再进行下一步的比较。
- 另外一种处理方式为：保持这种约定不变，但是另写一个用于递归的函数。区分开这二者的返回条件。

**参考代码：**

```python
class Solution:
    def HasSubtree(self, a, b):
        """
        判断b是否为a的子结构
        """
        # 定义用于递归的子函数
        def isSubTree(a, b):
            if b == None:
                return True
            if a == None:
                return False
            if a.val == b.val:
                return isSubTree(a.left, b.left) and isSubTree(a.right, b.right) or isSubTree(a.left, b) or isSubTree(a.right, b)
            else:
                return isSubTree(a.left, b) or isSubTree(a.right, b)
  
        # 调用子函数
        if a == None or b == None:
            return False
        return isSubTree(a, b) 

    def HasSubtree2(self, a, b):
        """
        不定义子函数的方式
        """
        if a == None or b == None:
            return False

        tmp = False
        if a.val == b.val:
            if b.left == b.right == None:
                return True
            elif b.left == None and b.right != None:
                tmp = self.HasSubtree2(a.right, b.right)
            elif b.left != None and b.right == None:
                tmp = self.HasSubtree2(a.left, b.left)
            else:
                tmp = self.HasSubtree2(a.left, b.left) and self.HasSubtree2(a.right, b.right)

        if tmp:
            return tmp
        else:
            return self.HasSubtree2(a.left, b) or self.HasSubtree2(a.right, b)

```

```c++
class Solution {
public:
    // 定义用于递归调用的函数
    bool isSubtree(TreeNode* a, TreeNode* b) {
        if (b == nullptr) {
            return true;
        }
        if (a == nullptr) {
            return false;
        }
        if (a->val == b->val) {
            return isSubtree(a->left, b->left) && \
                   isSubtree(a->right, b->right) || \
                   isSubtree(a->left, b) || \
                   isSubtree(a->right, b);
        } else {
            return isSubtree(a->left, b) || isSubtree(a->right, b);
        }
    }

    // 判断b是否为a的子结构
    bool HasSubtree(TreeNode* a, TreeNode* b) {
        if (a == nullptr || b == nullptr) {
            return false;
        }

        return isSubtree(a, b);
    }

    // 判断b是否为a的子结构
    // 不使用递归的方式
    bool HasSubtree2(TreeNode* a, TreeNode* b) {
        if (a == nullptr || b == nullptr) {
            return false;
        }

        bool tmp = false;
        if (a->val == b->val) {
            if (b->left == nullptr && b->right == nullptr) {
                return true;
            } else if (b->left == nullptr && b->right != nullptr) {
                tmp = HasSubtree2(a->right, b->right);
            } else if (b->right == nullptr && b->left != nullptr) {
                tmp = HasSubtree2(a->left, b->left);
            } else {
                tmp = HasSubtree2(a->left, b->left) && HasSubtree2(a->right, b->right);
            }
        }

        if (tmp) {
            return tmp;
        } else {
            return HasSubtree2(a->left, b) || HasSubtree2(a->right, b);
        }
    }
};
```

### 18. 二叉树的镜像

**题目描述：**

> 操作给定的二叉树，将其变换为源二叉树的镜像。（即每个树的左右子树互换即可）

**解题思路：**

- 递归即可
- 终止的条件为，遇到了空

**参考代码：**

```python
class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        # write code here
        if root == None:
            return root
        
        root.left, root.right = root.right, root.left
        self.Mirror(root.left)
        self.Mirror(root.right)
        return root
```

```c++
class Solution {
public:
    void Mirror(TreeNode *root) {
        if (root == nullptr) {
            return;
        }
        
        TreeNode* tmp = root->left;
        root->left = root->right;
        root->right = tmp;
        
        Mirror(root->left);
        Mirror(root->right);
        return;
    }
};
```

### 19. 顺时针打印矩阵

**题目描述：**

> 输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，例如，如果输入如下4 X 4矩阵： 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 则依次打印出数字1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.

**解题思路：**

- 这道题的关键是把问题分解为打印环形。
- 依次从最外环打印到最内的环
- 每个环的打印，分为四条直线
- 注意最后的终止条件
- 注意防止出现单行或者单列的特殊情况

**参考代码：**

```python
# -*- coding:utf-8 -*-
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        if matrix == []:
            return []
        
        top = 0
        bottom = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1

        result = []
        while top <= bottom and left <= right:
            for i in range(left, right + 1):
                result.append(matrix[top][i])
            for i in range(top + 1, bottom + 1):
                result.append(matrix[i][right])
            if top != bottom:
                for i in range(right - 1, left - 1, -1):
                    result.append(matrix[bottom][i])
            if left != right:
                for i in range(bottom - 1, top, -1):
                    result.append(matrix[i][left])
            top += 1
            bottom -= 1
            left += 1
            right -= 1
        return result
```

```c++
class Solution {
public:
    vector<int> printMatrix(vector<vector<int> > matrix) {
        vector<int> result;
        
        if (matrix.size() == 0) {
            return result;
        }
        
        int top = 0;
        int bottom = matrix.size() - 1;
        int left = 0;
        int right = matrix[0].size() - 1;
        
        while (top <= bottom && left <= right) {
            for (int i = left; i <= right; i++) {
                result.push_back(matrix[top][i]);
            }
            for (int i = top+1; i <= bottom; i++) {
                result.push_back(matrix[i][right]);
            }
            if (top != bottom) {
                for (int i = right-1; i >= left; i--) {
                    result.push_back(matrix[bottom][i]);
                }
            }
            if (left != right) {
                for (int i = bottom-1; i > top; i--) {
                    result.push_back(matrix[i][left]);
                }
            }

            top++;
            bottom--;
            left++;
            right--;
        }
        
        return result;
    }
};
```

### 20. 包含min函数的栈

**题目描述：**

> 定义栈的数据结构，请在该类型中实现一个能够得到栈中所含最小元素的min函数（时间复杂度应为O（1））。注意：保证测试中不会当栈为空的时候，对栈调用pop()或者min()或者top()方法。

**解题思路：**

- 注意关键点在于限制了min函数的时间复杂度为-1，也就是跟存储数据量的大小没有关系
- 因此必须额外分配一个数据结构来记录当前的最小值

**参考代码：**

```python
class Solution:
    """
    注意最小数必须由一个栈来维护，不能是一个数
    否则经过pop之后就无法保持最小数是正确的了
    也就是说需要保持两个栈的对应性
    """
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, node):
        self.stack.append(node)
        if self.minStack == [] or self.min() > node:
            self.minStack.append(node)
        else:
            tmp = self.min()
            self.minStack.append(tmp)

    def pop(self):
        if self.stack == [] or self.minStack == []:
            return None
        self.stack.pop()
        self.minStack.pop()

    def top(self):
        return self.stack[-1]

    def min(self):
        if self.stack == [] or self.minStack == []:
            return None
        return self.minStack[-1]
```

```c++
#include <stack>
class Solution {
private:
    stack<int> s;
    stack<int> ms;
public:
    void push(int value) {
        s.push(value);
        if (ms.empty() || ms.top() >= value) {
            ms.push(value);
        }
    }
    void pop() {
        if (s.empty() || ms.empty()) {
            return;
        }
        if (s.top() == ms.top()) {
            ms.pop();
        }
        s.pop();
    }
    int top() {
        return s.top();
    }
    int min() {
        return ms.top();
    }
};
```

### 21. 栈的压入弹出序列

**题目描述：**

> 输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否可能为该栈的弹出顺序。假设压入栈的所有数字均不相等。例如序列1,2,3,4,5是某栈的压入顺序，序列4,5,3,2,1是该压栈序列对应的一个弹出序列，但4,3,5,1,2就不可能是该压栈序列的弹出序列。（注意：这两个序列的长度是相等的）

**解题思路：**

- 构造一个空栈，实际模拟一下栈的压入和弹出操作
- 总共的压入次数为pushArray.size()，循环实现这个次数即可，每次循环的内部利用while循环实现弹出操作，判断条件为当前栈非空，并且当前栈的顶部元素等于popArray的首元素，注意当前栈和popArray同步进行弹出的操作
- 最终判断当前栈是否为空，判断两个序列是否合理

**参考代码：**

```python
class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        if pushV == []:
            return True
        
        length = len(pushV)
        
        pair = 0
        tmp = [pushV[0]]
        del pushV[0]
        
        while pair < length:
            if tmp[-1] != popV[0]:
                if pushV != []:
                    tmp.append(pushV[0])
                    del pushV[0]
                else:
                    return False
            else:
                del tmp[-1]
                del popV[0]
                pair += 1
            
        return True
    
    def IsPopOrder(self, pushVec, popVec):
        """
        参考答案的方法
        """
        if pushVec == [] or popVec == []:
            return False
        else:
            # 进行值传递，排除对外界的影响
            pushV = pushVec.copy()
            popV = popVec.copy()

        stack = []
        for i in pushV:
            stack.append(i)
            while stack != [] and stack[-1] == popV[0]:
                stack.pop()
                popV.pop(0)

        if stack:
            return False
        else:
            return True
```

```c++
class Solution {
public:
    // 参考答案
    bool IsPopOrder(std::vector<int> pushV, std::vector<int> popV) {
        if (pushV.size() == 0 || popV.size() == 0) {
            return false;
        }

        std::vector<int> stack;
        for (auto i : pushV) {
            stack.push_back(i);
            while (stack.size() > 0 && stack.back() == popV.front()) {
                // 删除尾部元素的时候使用迭代器会失效
                // 删除首部元素好像就可以
                //stack.erase(std::end(stack));
                stack.pop_back();
                popV.erase(std::begin(popV));
            }
        }

        if (stack.size() == 0) {
            return true;
        } else {
            return false;
        }
    }

    // 自行解法
    bool IsPopOrder2(std::vector<int> pushV, std::vector<int> popV) {
        if (pushV.size() == 0 || popV.size() == 0) {
            return false;
        }

        int length = pushV.size();
        int pair = 0;
        std::vector<int> tmp;
        tmp.push_back(pushV.front());

        while (pair < length) {
            if (tmp.back() != popV.front()) {
                if (pushV.size() > 0) {
                    tmp.push_back(pushV.front());
                    pushV.erase(pushV.begin());
                } else {
                    return false;
                }
            } else {
                tmp.pop_back();
                popV.erase(popV.begin());
                pair++;
            }
        }

        return true;
    }
};
```

### 22. 从上往下打印二叉树

**题目描述：**

> 从上往下打印出二叉树的每个节点,同层节点从左至右打印。

**解题思路：**

- 这个直接看的答案，一开始想的是递归，但是递归好像没法做
- 关键点是遍历整个树，但是不去打印，第一次遍历只是为了存储各个节点，通过迭代的方式，把所有节点按照层次的方式存储起来
- 第二次遍历那个存储即可完成打印输出
- 另外一种形式是使用队列，与第一种形式本质差不多

**参考代码：**

```python
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        if root == None:
            return []
        
        result = []
        curr_list = [root]
        while curr_list:
            next_list = []
            for i in curr_list:
                if i.left:
                    next_list.append(i.left)
                if i.right:
                    next_list.append(i.right)
                result.append(i.val)
            curr_list = next_list
        return result
```

```c++
class Solution {
public:
    vector<int> PrintFromTopToBottom(TreeNode* root) {
        vector<int> result;
        if (root == nullptr) {
            return result;
        }
        
        vector<TreeNode*> queue = {root};
        while (!queue.empty()) {
            TreeNode* currNode = queue.front();
            queue.erase(queue.begin());
            result.push_back(currNode->val);
            
            if (currNode->left) {
                queue.push_back(currNode->left);
            }
            if (currNode->right) {
                queue.push_back(currNode->right);
            }
        }
        
        return result;
    }
};
```

### 23. 二叉搜索树的后续遍历序列

**题目描述：**

> 输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。

**解题思路：**

- 讲道理，这道题连题目都没看懂
- 二叉搜索树，BST，Binary search Tree，它或者是一棵空树，或者是具有下列性质的[二叉树](https://baike.baidu.com/item/二叉树/1602879)： 若它的左子树不空，则左子树上所有结点的值均小于它的根结点的值； 若它的右子树不空，则右子树上所有结点的值均大于它的根结点的值； 它的左、右子树也分别为[二叉排序树](https://baike.baidu.com/item/二叉排序树/10905079)。
- 所以关键点在两个地方，一是二叉搜索树满足左<中<右，且左右也都是二叉搜索树。二是后续遍历。

**参考代码：**

```python
# -*- coding:utf-8 -*-
class Solution:
    def VerifyBST(self, seq, first, last):
        if first >= last:
            return True
        
        rootVal = seq[last]
        cutIndex = first
        while cutIndex < last and seq[cutIndex] < rootVal:
            cutIndex += 1
            
        for i in range(cutIndex, last):
            if seq[i] < rootVal:
                return False
            
        return self.VerifyBST(seq, first, cutIndex - 1) and self.VerifyBST(seq, cutIndex, last - 1)
        
    def VerifySquenceOfBST(self, seq):
        # write code here
        if seq == []:
            return False
        
        return self.VerifyBST(seq, 0, len(seq) - 1)
```

```c++
class Solution {
public:
    // 递归层次的函数调用
    bool VerifyBST(std::vector<int>&seq, int first, int last) {
        if (first >= last) {
            return true;
        }

        // 寻找左右子树的区分点
        int rootVal = seq[last];
        int cutIndex = first;
        while (cutIndex < last && seq[cutIndex] < rootVal) {
            cutIndex++;
        }

        // 检测右子树是否满足都大于根节点的值
        for (int i = cutIndex; i < last; i++) {
            if (seq[i] < rootVal) {
                return false;
            }
        }

        // 当前层次已经满足，递归检测下一层次
        return VerifyBST(seq, first, cutIndex - 1) && VerifyBST(seq, cutIndex, last - 1);
    }

    // 顶层的函数调用
    bool VerifySequenceOfBST(std::vector<int>& seq) {
        if (seq.empty()) {
            return false;
        }

        return VerifyBST(seq, 0, seq.size() - 1);
    }
};
```

### 24. 二叉树中和为某一值的路径

**题目描述：**

> 输入一颗二叉树的根节点和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。(注意: 在返回值的list中，数组长度大的数组靠前)

**解题思路：**

- 使用带记忆的DFS来解决，也就是深度优先的方法。
- 这道题有个bug，结果根本就没有验证是否是路径长的数组靠前。
- 可以使用两个函数实现，也可以利用一个函数递归实现。

**参考代码：**

```python
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def __init__(self):
        self.path = []
        self.ret = []
        
    def FindPath(self, root, target):
        # write code here
        if root == None:
            return self.ret
        
        self.path.append(root.val)
        target -= root.val
        
        if target == 0 and root.left == None and root.right == None:
            tmp = self.path[:]
            self.ret.append(tmp)
        else:
            self.FindPath(root.left, target)
            self.FindPath(root.right, target)
            
        self.path.pop(-1)
        return self.ret
```

```c++
/*
struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
    TreeNode(int x) :
            val(x), left(NULL), right(NULL) {
    }
};*/
class Solution {
private:
    vector<vector<int>> ret;
    vector<int> path;
public:
    void backTracking(TreeNode* root, int target) {
        if (root == nullptr) {
            return;
        }
         
        path.push_back(root->val);
        target -= root->val;
         
        if (target == 0 && root->left == nullptr && root->right == nullptr) {
            ret.push_back(path);
        } else {
            backTracking(root->left, target);
            backTracking(root->right, target);
        }
         
        // 关键在于这一句，完成一条路径的遍历之后，path清除最后一个节点
        path.pop_back();
    }
     
    vector<vector<int> > FindPath(TreeNode* root,int target) {
        backTracking(root, target);
        return ret;
    }
};
```

### 25. 复杂链表的复制

**题目描述：**

> 输入一个复杂链表（每个节点中有节点值，以及两个指针，一个指向下一个节点，另一个特殊指针指向任意一个节点），返回结果为复制后复杂链表的head。（注意，输出结果中请不要返回参数中的节点引用，否则判题程序会直接返回空）

**解题思路：**

- 看了别人的答案，才把题目看懂，就不能说的明白些吗？要求完全复制，包括那些随机的没有任何意义的链接。

- 问题的关键在于顺序遍历时，那些随机的链接无法同样复制。解决方法有两种。一是多次遍历法：(1) 在旧链表中创建新链表，此时不处理兄弟节点。(2) 根据旧链表的兄弟节点，初始化新链表的兄弟节点。(3) 从旧链表中拆分得到新链表。二是map字典关联。

- 方法一：map关联
  

首先遍历一遍原链表，创建新链表（赋值label和next），用map关联对应结点；再遍历一遍，更新新链表的random指针。（注意map中应有NULL ----> NULL的映射）

- 方法二：next指针关联
  

创建新链表的时候，用原结点的next指针指向对应新结点，新结点的next指针指向下一个原结点，以此类推，形成之字形关联。然后，就可以先更新新链表的random指针，再解除next关联，更新next指针。这种方法不需要map来辅助，不管查找next还是random指针都是O(1)的，效率很高。

- 另外，python使用了递归结果是可以的，但是c++使用递归结果就不行，奇怪。

**参考代码：**

```python
# next指针关联
class Solution:
    # 返回 RandomListNode
    def Clone(self, head):
        if head == None:
            return None
        
        # 遍历节点并拷贝到后面
        currNode = head
        while currNode != None:
            nextNode = currNode.next
            newNode = RandomListNode(currNode.label)
            currNode.next = newNode
            newNode.next = nextNode
            currNode = nextNode
            
        # 拷贝随机的链接关系
        currNode = head
        while currNode != None:
            currNode.next.random = currNode.random.next if currNode.random else None
            currNode = currNode.next.next
            
        # 从旧链表中分离出新链表
        currNode = head
        headClone = head.next
        while currNode != None:
            tmp = currNode.next
            currNode.next  = tmp.next
            tmp.next = tmp.next.next if tmp.next else None
            currNode = currNode.next
            
        return headClone

# ====================
# map映射方法
class Solution:
    # 返回 RandomListNode
    def Clone(self, head):
        if head == None:
            return None
        
        head1 = head
        head2 = RandomListNode(head1.label)
        newhead = head2
        Map = {head1 : head2}
        
        # 完全复制并且建立映射
        while head1 != None:
            if head1.next != None:
                head2.next = RandomListNode(head1.next.label)
                
            head1 = head1.next
            head2 = head2.next
            Map[head1] = head2
            
        # 复制随机的链接
        head1 = head
        head2 = newhead
        while head1 != None:
            head2.random = Map[head1.random]
            head1 = head1.next
            head2 = head2.next
            
        return newhead
    
# ====================
# 递归法（这种方式，新链表挂载在了旧链表上）
class Solution:
    # 返回 RandomListNode
    def Clone(self, head):
        # write code here
        if head == None:
            return None
        
        newhead = RandomListNode(head.label)
        newhead.random = head.random
        newhead.next = self.Clone(head.next)
        
        return newhead
```

```c++
// next指针遍历
class Solution {
public:
    RandomListNode* Clone(RandomListNode* head) {
        if (head == nullptr) {
            return nullptr;
        }
        
        // 1、复制每个结点，如复制结点A得到A1，将结点A1插到结点A后面；
        // 注意尾部的nullptr没有复制
        RandomListNode* currNode = head;
        RandomListNode* nextNode = nullptr;
        while (currNode != nullptr) {
            nextNode = currNode->next;
            RandomListNode *newNode = new RandomListNode(currNode->label);
            currNode->next = newNode;
            newNode->next = nextNode;
            currNode = nextNode;
        }
        
        // 2、重新遍历链表，复制老结点的随机指针给新结点，如A1.random = A.random.next;
        // 拷贝随机的链接关系
        currNode = head;
        while (currNode != nullptr) {
            currNode->next->random = currNode->random == nullptr ? nullptr : currNode->random->next;
            currNode = currNode->next->next;
        }
        
        // 3、拆分链表，将链表拆分为原链表和复制后的链表
        // 从旧链表分离得到新链表
        currNode = head;
        RandomListNode* headClone = head->next;
        while (currNode != nullptr) {
            RandomListNode* tmp = currNode->next;
            currNode->next = tmp->next;
            tmp->next = tmp->next == nullptr ? nullptr : tmp->next->next;
            currNode = currNode->next;
        }
        
        return headClone;
    }
};

// ====================
// map映射方法
#include <map>
class Solution {
public:
    RandomListNode* Clone(RandomListNode* head) {
        if (head == nullptr) {
            return nullptr;
        }
        
        // map法, 初始化
        map<RandomListNode*, RandomListNode*> map;
        RandomListNode* head1 = head;
        RandomListNode* head2 = new RandomListNode(head1->label);
        RandomListNode* newhead = head2;
        map[head1] = head2;
        
        // 完全复制链表并建立map
        while (head1) {
            if (head1->next) {
                head2->next = new RandomListNode(head1->next->label);
            } else {
                head2->next = nullptr;
            }
            
            head1 = head1->next;
            head2 = head2->next;
            map[head1] = head2;
        }
        
        // 复制随机的链接
        head1 = head;
        head2 = newhead;
        while (head1) {
            head2->random = map[head1->random];
            head1 = head1->next;
            head2 = head2->next;
        }
        
        return newhead;
    }
};
```

### 26. 二叉树搜索树与双向链表

**题目描述：**

> 输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。要求不能创建任何新的结点，只能调整树中结点指针的指向。

**解题思路：**

- 递归进行中序遍历，左中右，但是需要注意的是，递归函数返回的是链表的头，而由于递归过程中需要完成链表的拼接，因此需要记录链表的尾，因此需要额外的变量来记录。
- 注意对空节点的处理。
- 更为高效的方式是，采用逆向的中序遍历，右中左，这样就能节省额外的存储变量空间。

**参考代码：**

```python
class Solution:
    def __init__(self):
        self.head = None
    def Convert(self, root):
        # write code here
        if root == None:
            return None
        
        # 右
        self.Convert(root.right)
        
        # 中
        root.right = self.head
        if self.head != None:
            self.head.left = root
        self.head = root
        
        # 左
        self.Convert(root.left)
        
        return self.head
```

```c++
// c++
TreeNode* head = nullptr;
TreeNode* Convert(TreeNode* root) {
    // 中序遍历：右　中　左
    if (root == nullptr) {
        return nullptr;
    }
    
    // 右
    Convert(root->right);
    
    // 中
    root->right = head;
    if (head != nullptr) {
        head->left = root;
    }
    head = root;
    
    // 左
    Convert(root->left);
    
    return head;
}

// 其它方法
class Solution {
public:
    // 中序遍历：左 中　右
    TreeNode* last = nullptr; // 类内变量，记录双链表的尾部
    
    TreeNode* Convert(TreeNode* root) {
        if (root == nullptr) {
            return nullptr;
        }
        
        // 左
        // 将左子树挂载到last上，并返回头
        TreeNode* head = Convert(root->left); // 中间变量，记录双链表的头
        if (head == nullptr) {
            head = root;
        }
        
        // 中
        // 完成last和根的链接
        root->left = last;
        if (last != nullptr) {
            last->right = root;
        } 
        last = root;
        
        // 右
        Convert(root->right);
        
        return head;
    }
};
```

### 27. 字符串的排列

**题目描述：**

> 输入一个字符串,按字典序打印出该字符串中字符的所有排列。例如输入字符串abc,则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。（输入一个字符串,长度不超过9(可能有字符重复),字符只包括大小写字母。）

**解题思路：**

- 这里只是实现了基本的解法，高效解法需要补充。
- 利用递归实现，perm(1234) = 1perm(234) + 2perm(134) + 3perm(124) + 4perm(123)
- 首先进行排序，后续依次将后面的元素与首元素进行调换位置，然后排序，再进行后续的递归
- 递归终止的条件为low==high
- 注意对含有重复元素情况的处理

**参考代码：**

```python
class Solution:
    def __init__(self):
        self.ret = []
        
    def perm(self, ss, low, high):
        if low == high:
            tmp = "".join(ss)
            self.ret.append(tmp)
            return
        
        # 这里是个坑，需要补上之前的那一小段才可以
        curr = ss[0:low] + sorted(ss[low:high + 1])
        
        for i in range(low, high + 1):
            if i == low or curr[i] != curr[low]:
                curr[i], curr[low] = curr[low], curr[i]
                self.perm(curr, low + 1, high)
                curr[i], curr[low] = curr[low], curr[i]
                
        return
    
    def Permutation(self, ss):
        # write code here
        if ss == None:
            return self.ret
        
        strList = list(ss)
        self.perm(strList, 0, len(strList) - 1)
        
        return self.ret
```

```c++
// c++
#include <algorithm>
class Solution {
public:
    vector<string> ret;
    
    void swap(char& a, char& b) {
        char tmp = a;
        a = b;
        b = tmp;
    }
    
    // 采用递归，输入str，每个函数实现的功能是将当前的全排列可能添加到ret中去
    void perm(string str, int low, int high) {
        if (low == high) {
            ret.push_back(str);
            return;
        }
        
        sort(str.begin() + low, str.end());
        
        // 依次交换，并进行下一次的迭代
        for (int i = low; i <= high; i++) {
            // 跳过重复
            if (i == low || str[low] != str[i]) {
                swap(str[i], str[low]); // 交换
                perm(str, low + 1, high); // 递归
                //swap(str[i], str[low]); // 交换回来
            }
        }
        return;
    }
    
    vector<string> Permutation(string str) {
        if (str.empty()) {
            return ret;
        }
        
        sort(str.begin(), str.end());
        perm(str, 0, str.size() - 1);
        return ret;
    }
};
```

### 28. 数组中出现次数超过一半的数字

**题目描述：**

> 数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。

**解题思路：**

- 先进行排序，之后构建长度为length/2的检测区间[first, last]
- 当array[first] == array[last]时，则找到该元素。
- 存在高效解法，待补充（多数投票问题,可以利用 Boyer-Moore Majority Vote Algorithm 来解决这个问题,使得时间复杂度为 O(N)）

**参考代码：**

```python
class Solution:
    def MoreThanHalfNum_Solution(self, number):
        # write code here
        number.sort()
        
        length = len(number)
        first = 0
        end = first + length // 2
        while end < length:
            if number[first] == number[end]:
                return number[first]
            first += 1
            end += 1
        
        return 0
```

```c++
#include <algorithm>
class Solution {
public:
    int MoreThanHalfNum_Solution(vector<int> numbers) {
        sort(numbers.begin(), numbers.end());
        
        int length = numbers.size();
        int first = 0;
        int end = first + length / 2;
        
        while (end < length) {
            if (numbers[first] == numbers[end]) {
                return numbers[first];
            }
            first++;
            end++;
        }
        return 0;
    }
};
```

### 29. 最小的k个数

**题目描述：**

> 输入n个整数，找出其中最小的K个数。例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4,。

**解题思路：**

- 借助stl直接排序，然后取最小的k个数
- 存在不借助stl的高效解法（待补充）

**参考代码：**

```python
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        if tinput == [] or k > len(tinput):
            return []
        
        tinput.sort()
        return tinput[0:k]
```

```c++
#include <algorithm>
class Solution {
public:
    vector<int> GetLeastNumbers_Solution(vector<int> input, int k) {
        vector<int> result = {};
        if (input.empty() || k > input.size()) {
            return result;
        }
        
        sort(input.begin(), input.end());
        result.insert(result.begin(), input.begin(), input.begin() + k);
        return result;
    }
};
```

### 30. 连续子数组的最大和

**题目描述：**

> HZ偶尔会拿些专业问题来忽悠那些非计算机专业的同学。今天测试组开完会后,他又发话了:在古老的一维模式识别中,常常需要计算连续子向量的最大和,当向量全为正数的时候,问题很好解决。但是,如果向量中包含负数,是否应该包含某个负数,并期望旁边的正数会弥补它呢？例如:{6,-3,-2,7,-15,1,2,2},连续子向量的最大和为8(从第0个开始,到第3个为止)。给一个数组，返回它的最大连续子序列的和，你会不会被他忽悠住？(子向量的长度至少是1)

**解题思路：**

- **动态规划**，初级题目

- F（i）：以array[i]为末尾元素的子数组的和的最大值，子数组的元素的相对位置不变  

  F（i）=　max（F（i-1）+　array[i] ， array[i]）  

  res：所有子数组的和的最大值  

  res　=　max（res，F（i））

**参考代码：**

```python
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        if array == []:
            return 0
        
        length = len(array)
        if length == 1:
            return array[0]
        
        curr_sum = array[0]
        curr_max = array[0]
        
        for i in range(1, length):
            if curr_sum >= 0:
                curr_sum += array[i]
            else:
                curr_sum = array[i]
                
            if curr_sum > curr_max:
                curr_max = curr_sum
                
        return curr_max
```

```c++
class Solution {
public:
    int FindGreatestSumOfSubArray(vector<int> array) {
        if (array.empty()) {
            return 0;
        }
        
        int length = array.size();
        if (length == 1) {
            return array[0];
        }
        
        int curr_sum = array[0];
        int curr_max = array[0];
        for (int i = 1; i < length; i++) {
            if (curr_sum >= 0) {
                curr_sum += array[i];
            } else {
                curr_sum = array[i];
            }
            
            if (curr_sum > curr_max) {
                curr_max = curr_sum;
            }
        }
        
        return curr_max;
    }
};
```

### 31. 整数中1出现的次数

**题目描述：**

> 求出1-13的整数中1出现的次数,并算出100-1300的整数中1出现的次数？为此他特别数了一下1~13中包含1的数字有1、10、11、12、13因此共出现6次,但是对于后面问题他就没辙了。ACMer希望你们帮帮他,并把问题更加普遍化,可以很快的求出任意非负整数区间中1出现的次数（从1 到 n 中1出现的次数）。

**解题思路：**

- 从个位到最高位依次进行查找，例如12345：

  考虑个位为1的情况，00001-12341，共有(12345//10 + 1)种，总共1235种

  考虑十位为1的情况，00010-12310，共有(1234//10 + 1)组，其中每组涵盖10-19，共10种，总共1240种

  考虑百位为1的情况，00100-12100，共有(123//10 + 1)组，其中每组涵盖00-99，共100种，总共1300种

  考虑千位为1的情况，01000-11000，共有(12//10 + 1)组，其中每组函数000-999，共1000种，总共2000种

  考虑万位为1的情况，10000-12345，共有(2345+1)，共有2346种

- 注意，这种方式从右到左来讨论1的位置，且当假定当前数位上为1时，只考虑后续几位的变化情况，因此不同数位上是1时并不会产生重叠的情况

- 当前数位有3种情况，0，１，大于2

- 以当前数位是0为基础，假设此时满足条件的数目为a*b，则大于2时的数目为(a+1)\*b，1时的数目为a\*b+c

- 其中c是额外处理的情况，而对于0-2带来的a和a+1的问题，可以利用+8来实现进位的处理（因此如果是判断数字中是否含有2，则比较的01-2-3-9的处理，即3时要进位，此时要利用+7来实现进位的处理）

**参考代码：**

```python
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        """
        暴力解法
        """
        return ''.join(map(str, range(n+1))).count('1')
    
    def NumberOf1Between1AndN_Solution2(self, n):
        cnt = 0
        m = 1
        
        while m <= n:
            a = n // m
            b = n % m
            cnt += (a + 8) // 10 * m + (b + 1 if a % 10 == 1 else 0)
            m *= 10
        
        return cnt
```

```c++
class Solution {
public:
    int NumberOf1Between1AndN_Solution(int n) {
        int cnt = 0;
        for (int m = 1; m <= n; m *= 10) {
            int a = n / m;
            int b = n % m;
            cnt += (a + 8) / 10 * m + (a % 10 == 1 ? b + 1 : 0);
        }
        return cnt;
    }
};
```

### 32. 把数组排成最小的数

**题目描述：**

> 输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。例如输入数组{3，32，321}，则打印出这三个数字能排成的最小数字为321323。

**解题思路：**

- 主要思路是将题目看做是，字符串排序问题
- 判断字符串a比字符串b小的条件是，a + b < b + a
- 冒泡实现从小到大的排序

**参考代码：**

```python
class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        if numbers == []:
            return ""
        
        length = len(numbers)
        num = [str(x) for x in numbers]
        for i in range(0, length-1):
            for j in range(i + 1, length):
                if num[i] + num[j] > num[j] + num[i]:
                    num[i], num[j] = num[j], num[i]

        return "".join(num)
```

```c++
class Solution {
public:
    string PrintMinNumber(vector<int> numbers) {
        string result;
        if (numbers.empty()) {
            return result;
        }
        
        int length = numbers.size();
        for (int i = 0; i < length - 1; i++) {
            for (int j = i + 1; j < length; j++) {
                string a = to_string(numbers[i]);
                string b = to_string(numbers[j]);
                if (a + b > b + a) {
                    int tmp = numbers[i];
                    numbers[i] = numbers[j];
                    numbers[j] = tmp;
                }
            }
        }
        
        for (auto i : numbers) {
            result += to_string(i);
        }
        
        return result;
    }
};
```

### 33. 丑数

**题目描述：**

> 把只包含质因子2、3和5的数称作丑数（Ugly Number）。例如6、8都是丑数，但14不是，因为它包含质因子7。 习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数。

**解题思路：**

- 基础的思路是暴力枚举，从1开始遍历，分别使用532进行整除，知道最后无法整除时，查看结果是否为1，判断当前结果是否为丑数。（这种方法的最大问题就是复杂度过大）
- 高效的思路是发现所有的丑数都是由1235之间相互倍乘得到，因此可以维护三个队列，每个队列分别对应倍乘235的情况，当时每个队列的基数都要实时更新（从之前的丑数中依次增大），当前的丑数由这三个对列中最小值得出。
- 利用三个指针，功能是维护了三个有序的丑数队列（由小到大），再求三个队列的最小值的最小值，则一定是还没有出现的丑数中的最小值。（注意更新的步骤，每个队列需要pop出最小的值作为丑数，同时需要push一个倍乘相应系数的丑数，进行下一次的筛选）

**参考代码：**

```python
# python
# -*- coding:utf-8 -*-
class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        if index == 0:
            return 0
        
        result = [1] * index
        t2 = t3 = t5 = 0
        
        for i in range(1, index):
            result[i] = min(result[t2] * 2, result[t3] * 3, result[t5] * 5)
            if result[i] == 2 * result[t2]:
                t2 += 1
            if result[i] == 3 * result[t3]:
                t3 += 1
            if result[i] == 5 * result[t5]:
                t5 += 1
        
        return result[index - 1]
```

```c++
class Solution {
public:
    int min(int a, int b, int c) {
        int tmp = a < b ? a : b;
        return tmp < c ? tmp : c;
    }
    int GetUglyNumber_Solution(int index) {
        if (index == 0) {
            return 0;
        }
        
        int t2 = 0, t3 = 0, t5 = 0;
        vector<int> result(index, 1);
        
        for (int i = 1; i < index; i++) {
            result[i] = min(result[t2] * 2, result[t3] * 3, result[t5] * 5);
            if (result[i] == 2 * result[t2]) t2++;
            if (result[i] == 3 * result[t3]) t3++;
            if (result[i] == 5 * result[t5]) t5++;
        }
        
        return result[index - 1];
    }
};
```

### 34. 第一个只出现一次的字符

**题目描述：**

> 在一个字符串(0<=字符串长度<=10000，全部由字母组成)中找到第一个只出现一次的字符,并返回它的位置, 如果没有则返回 -1（需要区分大小写）

**解题思路：**

- 暴力解法：二重遍历即可（无奈超时了）
- 高效解法：借助map，记录每个字母出现的次数，同时按要求输出第一个只出现一次的字母
- 注意map是以红黑树实现的，map后，不能以map的迭代器遍历，必需用str[i]来遍历。
- 也可以使用一个256的数组来代替stl中的map，本质都是hash

**参考代码：**

```python
class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        if len(s) <= 0:
            return -1
        
        d = dict()
        for i in s:
            d[i] = d.get(i, 0) + 1
        for i in s:
            if d[i] == 1:
                return s.index(i)
        return -1
```

```c++
class Solution {
public:
    int FirstNotRepeatingChar(string str) {
        if (str.empty()) {
            return -1;
        }
        
        unsigned int hash[256] = {0};
        for (int i = 0; i < str.size(); i++) {
            hash[str[i]]++;
        }
        for (int i = 0; i < str.size(); i++) {
            if (hash[str[i]] == 1) {
                return i;
            }
        }
        
        return -1;
    }
};
```

### 35. 数组中的逆序对

**题目描述：**

> 在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组,求出这个数组中的逆序对的总数P。并将P对1000000007取模的结果输出。 即输出P%1000000007

**解题思路：**

- 暴力解法

**参考代码：**

```python
# python
```

```c++
// c++
```

### 36. 两个链表的第一个公共结点

**题目描述：**

> 输入两个链表，找出它们的第一个公共结点。（注意因为传入数据是链表，所以错误测试数据的提示是用其他方式显示的，保证传入数据是正确的）

**解题思路：**

- 暴力解法

**参考代码：**

```python
# python
```

```c++
// c++
```

### 37. 数字在排序数组中出现的次数

**题目描述：**

> 统计一个数字在排序数组中出现的次数。

**解题思路：**

- 暴力解法

**参考代码：**

```python
# python
```

```c++
// c++
```

### 38. 二叉树的深度

**题目描述：**

> 输入一棵二叉树，求该树的深度。从根结点到叶结点依次经过的结点（含根、叶结点）形成树的一条路径，最长路径的长度为树的深度。

**解题思路：**

- 暴力解法

**参考代码：**

```python
# python
```

```c++
// c++
```

### 39. 平衡二叉树

**题目描述：**

> 输入一棵二叉树，判断该二叉树是否是平衡二叉树。

**解题思路：**

- 暴力解法

**参考代码：**

```python
# python
```

```c++
// c++
```

### 40. 数组中只出现一次的数字

**题目描述：**

> 一个整型数组里除了两个数字之外，其他的数字都出现了两次。请写程序找出这两个只出现一次的数字。

**解题思路：**

- 暴力解法

**参考代码：**

```python
# python
```

```c++
// c++
```

### 41. 和为S的连续正数序列

**题目描述：**

> 小明很喜欢数学,有一天他在做数学作业时,要求计算出9~16的和,他马上就写出了正确答案是100。但是他并不满足于此,他在想究竟有多少种连续的正数序列的和为100(至少包括两个数)。没多久,他就得到另一组连续正数和为100的序列:18,19,20,21,22。现在把问题交给你,你能不能也很快的找出所有和为S的连续正数序列? Good Luck!（输出所有和为S的连续正数序列。序列内按照从小至大的顺序，序列间按照开始数字从小到大的顺序）

**解题思路：**

- 暴力解法

**参考代码：**

```python
# python
```

```c++
// c++
```

### 42. 和为S的两个数字

**题目描述：**

> 输入一个递增排序的数组和一个数字S，在数组中查找两个数，使得他们的和正好是S，如果有多对数字的和等于S，输出两个数的乘积最小的。（对应每个测试案例，输出两个数，小的先输出。）

**解题思路：**

- 暴力解法

**参考代码：**

```python
# python
```

```c++
// c++
```

### 43. 左旋转字符串

**题目描述：**

> 汇编语言中有一种移位指令叫做循环左移（ROL），现在有个简单的任务，就是用字符串模拟这个指令的运算结果。对于一个给定的字符序列S，请你把其循环左移K位后的序列输出。例如，字符序列S=”abcXYZdef”,要求输出循环左移3位后的结果，即“XYZdefabc”。是不是很简单？OK，搞定它！

**解题思路：**

- 暴力解法

**参考代码：**

```python
# python
```

```c++
// c++
```

### 44. 翻转单词顺序列

**题目描述：**

> 牛客最近来了一个新员工Fish，每天早晨总是会拿着一本英文杂志，写些句子在本子上。同事Cat对Fish写的内容颇感兴趣，有一天他向Fish借来翻看，但却读不懂它的意思。例如，“student. a am I”。后来才意识到，这家伙原来把句子单词的顺序翻转了，正确的句子应该是“I am a student.”。Cat对一一的翻转这些单词顺序可不在行，你能帮助他么？

**解题思路：**

- 暴力解法

**参考代码：**

```python
# python
```

```c++
// c++
```

### 45. 扑克牌顺子

**题目描述：**

> LL今天心情特别好,因为他去买了一副扑克牌,发现里面居然有2个大王,2个小王(一副牌原本是54张^_^)...他随机从中抽出了5张牌,想测测自己的手气,看看能不能抽到顺子,如果抽到的话,他决定去买体育彩票,嘿嘿！！“红心A,黑桃3,小王,大王,方片5”,“Oh My God!”不是顺子.....LL不高兴了,他想了想,决定大\小 王可以看成任何数字,并且A看作1,J为11,Q为12,K为13。上面的5张牌就可以变成“1,2,3,4,5”(大小王分别看作2和4),“So Lucky!”。LL决定去买体育彩票啦。 现在,要求你使用这幅牌模拟上面的过程,然后告诉我们LL的运气如何， 如果牌能组成顺子就输出true，否则就输出false。为了方便起见,你可以认为大小王是0。

**解题思路：**

- 暴力解法

**参考代码：**

```python
# python
```

```c++
// c++
```

### 46. 圆圈中最后剩下的数

**题目描述：**

> 每年六一儿童节,牛客都会准备一些小礼物去看望孤儿院的小朋友,今年亦是如此。HF作为牛客的资深元老,自然也准备了一些小游戏。其中,有个游戏是这样的:首先,让小朋友们围成一个大圈。然后,他随机指定一个数m,让编号为0的小朋友开始报数。每次喊到m-1的那个小朋友要出列唱首歌,然后可以在礼品箱中任意的挑选礼物,并且不再回到圈中,从他的下一个小朋友开始,继续0...m-1报数....这样下去....直到剩下最后一个小朋友,可以不用表演,并且拿到牛客名贵的“名侦探柯南”典藏版(名额有限哦!!^_^)。请你试着想下,哪个小朋友会得到这份礼品呢？(注：小朋友的编号是从0到n-1)
>
> 如果没有小朋友，请返回-1

**解题思路：**

- 暴力解法

**参考代码：**

```python
# python
```

```c++
// c++
```

### 47. 前N项正整数求和

**题目描述：**

> 求1+2+3+...+n，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。

**解题思路：**

- 暴力解法

**参考代码：**

```python
# python
```

```c++
// c++
```

### 48. 不用加减乘除做加法

**题目描述：**

> 写一个函数，求两个整数之和，要求在函数体内不得使用+、-、*、/四则运算符号。

**解题思路：**

- 暴力解法

**参考代码：**

```python
# python
```

```c++
// c++
```

### 49. 把字符串转换成整数

**题目描述：**

> 将一个字符串转换成一个整数，要求不能使用字符串转换整数的库函数。 数值为0或者字符串不是一个合法的数值则返回0

**解题思路：**

- 暴力解法

**参考代码：**

```python
# python
```

```c++
// c++
```


### 50. 数组中重复的数字

**题目描述：**

> 在一个长度为n的数组里的所有数字都在0到n-1的范围内。 数组中某些数字是重复的，但不知道有几个数字是重复的。也不知道每个数字重复几次。请找出数组中任意一个重复的数字。 例如，如果输入长度为7的数组{2,3,1,0,2,5,3}，那么对应的输出是第一个重复的数字2。

**注意事项：**

1. python中交换列表中两个元素的位置不能使用更深层次的列表迭代：

   ```python
   a = [2, 3, 1, 0, 2, 5, 3]
   a[0], a [2] = a[2], a[0]  # 正确
   a[0], a[a[0]] = a[a[0]], a[2] # 错误
   index = a[0]
   a[0], a[index] = a[index], a[0] # 正确
   ```

2. 使用pdb进行调试的方式

   ```python
   import pdb
   pdb.set_trace()
   外部调试，快捷键 n c
   ```

**解题思路：**

- 第一思路是二重循环遍历，每个位置与后续的全部位置进行比较，这样的复杂度是O(N*(N-1))
- 考虑到题目中给出了对原始数组的限制，即**长度为N的数组，元素取值为0~N-1**，因此必然有重复
- 考虑到如果把数组完全升序排序，则一定会有**位置i处的元素值不是i**的情况发生
- 因此本题考察的就是如何进行元素位置的移动，使得尽快出现**位置i处的元素值不是i**的情况发生
- 需要注意的点就是：python/C++在进行数组内元素交换的时候的方法

**参考代码：**

```python
#!/bin/python3                                                       
#-*- coding:utf-8 -*-

class solution():
    # 需要赋值到duplication[0]
    # 函数返回bool
    def duplicate(self, numbers, duplication):
        i = 0 
        while (i < len(numbers)):
            if numbers[i] == i:
                i += 1
            elif numbers[i] != numbers[numbers[i]]:
                index = numbers[i]
                numbers[i], numbers[index] = numbers[index], numbers[i]
            else:
                duplication[0] = numbers[i]
                return True
        return False


if __name__ == "__main__":
    test = [2, 3, 1, 0, 2, 5, 3]
    duplication = [0] 
    s = solution()
    print(s.duplicate(test, duplication), duplication[0])
```

```C++
#include <iostream>                                                  

class Solution {
public:
    bool duplicate(int numbers[], int length, int* duplication) {
        int i = 0;
        int index = 0;
        while (i < length) {
            if (numbers[i] == i) {
                i++;
            } else if (numbers[i] != numbers[numbers[i]]) {
                index = numbers[i];
                numbers[i] = numbers[index];
                numbers[index] = index;
            } else {
                duplication[0] = numbers[i];
                return true;
            }
        }
        return false;
    }
};

int main (int argc, char* argv[])
{
    int numbers[] = {2, 3, 1, 0, 2, 5, 3};
    int duplication[] = {0};
    Solution s;
    if (s.duplicate(numbers, 7, duplication)) {
        printf("Ture %d\n", duplication[0]);
    } else {
        printf("False\n");
    }
    return 0;
}
```

## 第二部分

```markdown
其它
```
















































