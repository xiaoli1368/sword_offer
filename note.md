# 剑指offer题解笔记

作者：xiaoli1368
日期：2020/02/23
邮箱：xiaoli1644@qq.com

## 目录
[TOC]

### 01. 二维数组中的查找

**题目描述：**

> 在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

**解题思路：**

- 考察知识点：数组
- 暴力枚举：时间复杂度过大
- 高效解法：利用矩阵的有序性，从而实现更快的检测。（矩阵的L型结构都是有序的，反L也是有序的，因此可以从左下角开始查找，或者从右上角开始查找）

**参考代码：**

```c++
// c++
class Solution {
public:
	bool Find(int target, std::vector<std::vector<int>> array) {
		if (array.empty()) {
			return false;
		}

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

```python
# python
class Solution:
    def Find(self, target, array):
        i = 0
        j = len(array[0]) - 1
        while i < len(array) and j >= 0:
            if target == array[i][j]:
                return True
            elif target < array[i][j]:
                j -= 1
            else:
                i += 1
        return False
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

- 考察知识点：数组，二分查找
- 暴力枚举：这道题一开始没有思路（能够想到是二分折半），但直接采用暴力枚举的方式做的，没想到还通过了
- 高效思路：每次进行折半划分，确定两边的子数组，哪个是非递减数组，哪个是新的旋转数组（旋转数组的首元素大于尾部元素）
- 注意特殊情况是相等，此时无法进行数组划分，因此需要采用常规查找最小值
- 对于二分查找，需要注意中间middle的取值，可以有两种形式，(low+right)/2或者low+(high-low)/2，都是偏向low。另外一个注意的地方就是，缩小范围时的判断条件和区间划分。将array[m]与array[l]或者array[h]比较，二者实现形式并不一致，其中一个要简单，另外一个需要更为复杂的边界条件。
- 可以将本题看做是求数组[0, 0, 0, 1, -1, 0, 0, 0]中的-1，注意到在二分查找的区间划分中，-1属于h半段，因此编程中使用array[m]与array[h]比较更为方便（因为如果此时选择与array[l]比较，则有可能发生在更新l时跳过目标点的情况，需要细细体会，倘若要求的值位于l半段，则与array[l]比较更为方便）
- 另一种思路：使用array[m]与array[l]比较来获取最大值点，然后最大值点的右侧就是待求最小值

**参考代码：**

```c++
// cpp
class Solution {
public:
    int minNumberInRotateArray(std::vector<int> array) {
        if (array.empty()) {
            return 0;
        }

        int l = 0;
        int h = array.size() - 1;
        while (l <= h) {
            int m = (l + h) / 2;
            if (array[l] == array[m] && array[m] == array[h]) {
                return minNumber(array, l, h);
            } else if (array[m] <= array[h]) {
                h = m;
            } else {
                l = m + 1;
            }
        }
        return array[l];
    }
    
    int minNumber(std::vector<int> array, int low, int high) {
        int tmp = array[low];
        for (int i = low; i <= high; i++) {
            if (tmp > array[i]) {
                tmp = array[i];
            }
        }
        return tmp;
    }
};
```

```python
# python
class Solution:
    def minNumberInRotateArray(self, array):
        """
        二分查找，高效思路，优先使用[m, h]区间
        """
        length = len(array)
        if length == 0:
            return 0
        
        l = 0
        h = length - 1
        while l <= h:
            m = (l + h) // 2
            if array[l] == array[m] and array[m] == array[h]:
                return self.minNumber(array, l, h)
            elif array[m] <= array[h]:
                h = m
            else:
                l = m + 1
        return array[l]

    def minNumber(self, array, l, h):
        """
        输入一个数组，返回最小值
        """
        tmp = array[l]
        while l <= h:
            if tmp > array[l]:
                tmp = array[l]
            l += 1
        return tmp
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

- 思路1：借助两个数组，完成奇偶元素的分离，最终拼接输出（空间换时间）
- 思路2：借助一个数组，两次遍历，第一次遍历确定奇偶分界线的索引，第二次遍历进行添加不同的元素
- 思路3：使用冒泡思想，每次将当前最后一个偶数上浮到数组最右边（时间换空间，二重循环，复杂度大，可适当优化）
- 高效思路：插入排序，外层遍历找到第一个奇数，然后内层遍历将该奇数搬移到所有左侧偶数之前，然后重复处理第二个奇数

**参考代码：**

```cpp
// cpp
class Solution {
public:
    // 两个额外数据，空间时间
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
    
    // 高效方式，类似插入排序，不借助额外数组，两层遍历
    // 外层遍历依次找到各个奇数，内层遍历实现找到该奇数前的几个偶数，交换当前奇数与该偶数段的位置
    void reOrderArray2(std::vector<int>& array) {
        if (array.empty()) {
            return;
        }

        for (int i = 0; i < array.size(); i++) {
            if (array[i] % 2 == 1) {
                // 确定上一个奇数的位置（或者为首元素之前的-1索引）
                // 寻找到相邻两个奇数之间的偶数段
                // 当前分段：[last_odd], [last_odd + 1, i - 1], [i]
                // 交换[i]与[last_odd + 1, i - 1]
                int curr_odd = array[i];
                int last_odd = i - 1;

                while (last_odd >= 0 && array[last_odd] % 2 == 0) {
                    last_odd--;
                }

                for (int j = i - 1; j >= last_odd + 1; j--) {
                    array[j + 1] = array[j];
                }
                array[last_odd + 1] = curr_odd;
            }
        }
    }
};
```

```python
# python
class Solution:
    def reOrderArray(self, array):
        """
        两个额外数组，空间换时间
        """
        tmp1 = []
        tmp2 = []
        for i in array:
            if i % 2 == 1:
                tmp1.append(i)
            else:
                tmp2.append(i)
        return tmp1 + tmp2
        return array

    def reOrderArray2(slef, array):
        """
        高效方式，类似插入排序，不借助额外数组，两层遍历
        """
        if array == []:
            return array
        
        for i in range(len(array)):
            if array[i] % 2 == 1:
                # 确定上一个奇数的位置
                # 寻找相邻两个奇数之间的偶数段
                # [last_odd], [last_odd + 1, i - 1], [i]
                # 交换[i]与[last_odd + 1, i - 1]
                curr_odd = array[i]
                last_odd = i - 1

                while last_odd >= 0 and array[last_odd] % 2 == 0:
                    last_odd -= 1
                
                for j in range(i - 1, last_odd, -1):
                    array[j + 1] = array[j]
                array[last_odd + 1] = curr_odd
        
        return array
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

- 使用归并法来实现逆序对的统计，与归并法排序很像，三个部分构成
- 递归，把当前数组分为前后两个数组，每个数组各自区分，直到每个数组仅有一个数字
- 合并，根据前后两个数组的元素大小关系，统计逆序对。这里的任务实际上，对于两个从小到大排列的有序数组，判断存在多少个逆序对，同时将二者组合排序。以下代码中讨论了4种情况：1) 前数组已遍历完，2) 后数组已遍历完，3) 两数组都没有遍历完，且前元素小于后元素，4) 两数组都没有遍历完，且前元素大于后元素。注意，每种情况都有选择一个元素保持到tmp数组，最终需要将这个有序的tmp数组拷贝替换原始的nums数组，只有最后一种情况存在逆序数，需要累加。
- 排序，将前后两个数组排序并且替换原理的数组位置

**参考代码：**

```python
class Solution:
    def __init__(self):
        self.cnt = 0
    
    def InversePairs(self, nums):
        if nums == []:
            return 0
        self.mergeSort(nums, 0, len(nums) - 1)
        return self.cnt % 1000000007
        
    def mergeSort(self, nums, l, h):
        if l >= h:
            return
        m = l + (h - l) // 2
        self.mergeSort(nums, l, m)
        self.mergeSort(nums, m + 1, h)
        self.merge(nums, l, m, h)
    
    def merge(self, nums, l, m, h):
        i = l
        j = m + 1
        k = l
        tmp = []
        while i <= m or j <= h:
            if i > m: # 前数组已经遍历完
                tmp.append(nums[j])
                j += 1
            elif j > h or nums[i] <= nums[j]: # 后数组已经遍历完，或则　前 < 后
                tmp.append(nums[i])
                i += 1
            else: # 前 > 后，符合逆序对的定义
                tmp.append(nums[j])
                j += 1
                self.cnt += m - i + 1
            k += 1
        nums[l:h+1] = tmp[:]
```

```c++
class Solution {
public:
    long cnt = 0;
    vector<int> tmp;
    
    // 外部接口函数
    int InversePairs(vector<int> nums) {
        int length = nums.size();
        if (length == 0) {
            return 0;
        }
        
        tmp = nums;
        mergeSort(nums, 0, length - 1);
        return int(cnt % 1000000007);
    }
    
    // 递归调用的函数
    void mergeSort(vector<int>& nums, int l, int h) {
        if (l >= h) {
            // 当分组到只剩一个时，返回上一层，开始merge
            return;
        }
        int m = l + (h - l) / 2;
        mergeSort(nums, l, m);     // 左数组，统计，排序
        mergeSort(nums, m + 1, h); // 右数组，统计，排序
        merge(nums, l, m, h);      // 本次的前后数组，统计，排序
    }
    
    // 用来实现当前前后数组统计与合并的函数
    // 将两个有序数组合并为一个，同时统计逆序对
    void merge(vector<int>& nums, int l, int m, int h) {
        int i = l, j = m + 1, k = l;
        while (i <= m || j <= h) {
            if (i > m) { // 此时前数组已被遍历完，所有前数组小于后数组当前值
                tmp[k++] = nums[j++];
            } else if (j > h) { // 后数组被遍历完
                tmp[k++] = nums[i++];
            } else if (nums[i] <= nums[j]) { // 两个数组都没有遍历完，前 < 后
                tmp[k++] = nums[i++];
            } else { // 两个数组都没有遍历完，后 < 前，符合逆序数要求
                tmp[k++] = nums[j++];
                this->cnt += m - i + 1;
            }
        }
        
        // 将完成排序的部分拷贝到原数组中
        for (k = l; k <= h; k++) {
            nums[k] = tmp[k];
        }
    }
};
```

### 36. 两个链表的第一个公共结点

**题目描述：**

> 输入两个链表，找出它们的第一个公共结点。（注意因为传入数据是链表，所以错误测试数据的提示是用其他方式显示的，保证传入数据是正确的）

**解题思路：**

- map法：第一次遍历使用map记录第一个链表的键值，第二次遍历第二个链表，寻找map中是否存在
- 迭代法：相同长度的两个链表，第一次遍历直接找到公共节点；不同长度的情况，第一次遍历找到长度差，第二次以长度差进行遍历比较，直接找到公共节点。

**参考代码：**

```python
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def FindFirstCommonNode(self, h1, h2):
        # write code here
        listMap = []
        
        tmp = h1
        while tmp:
            listMap.append(id(tmp))
            tmp = tmp.next
        
        tmp = h2
        while tmp:
            if listMap.count(id(tmp)) == 1:
                return tmp
            tmp = tmp.next
            
        return None
    
    def FindFirstCommonNode2(self, h1, h2):
        # write code here
        t1 = h1
        t2 = h2
        while t1 != t2:
            t1 = t1.next if t1 != None else h2
            t2 = t2.next if t2 != None else h1
        return t1
```

```c++
/*
struct ListNode {
	int val;
	struct ListNode *next;
	ListNode(int x) :
			val(x), next(NULL) {
	}
};*/
#include <map>
class Solution {
public:
    ListNode* FindFirstCommonNode (ListNode* h1, ListNode* h2) {
        if (h1 == nullptr || h2 == nullptr) {
            return nullptr;
        }
        
        map<ListNode*, int> map;
        
        ListNode* tmp = h1;
        while (tmp != nullptr) {
            map[tmp] = tmp->val;
            //map.insert(pair<ListNode*, int>(tmp, tmp->val));
            tmp = tmp->next;
        }
        
        tmp = h2;
        while (tmp != nullptr) {
            if (map.count(tmp) == 1) {
                return tmp;
            }
            tmp = tmp->next;
        }
        return nullptr;
    }

// 迭代方法
    ListNode* FindFirstCommonNode2 (ListNode* h1, ListNode* h2) {
        ListNode* t1 = h1;
        ListNode* t2 = h2;
        while (t1 != t2) {
            t1 = (t1 == nullptr ? h2 : t1->next);
            t2 = (t2 == nullptr ? h1 : t2->next);
        }
        return t1;
    }
};
```

### 37. 数字在排序数组中出现的次数

**题目描述：**

> 统计一个数字在排序数组中出现的次数。（从小到达的有序数组，而且都是正整数）

**解题思路：**

- 常规思路：使用二分查找确定是否存在，当存在时返回一个任意的相等的索引，以此为基础向左右两边查找，直到两边都不相等。
- 高效思路：利用元素都是正整数这一特点，不要去查找目标值k，而是查找假想的值[k-0.5, k+0.5]，这样直接获得目标的区间。也可以修改二分查找算法，去寻找第一个大于等于某值的索引，这样查找[k, k+1]的区间也可以实现
- 其他思路，递归

**参考代码：**

```python
# -*- coding:utf-8 -*-
class Solution:
    def GetNumberOfK(self, data, k):
        first = self.binarySearch(data, k)
        last = self.binarySearch(data, k + 1)
        if first == len(data) or data[first] != k:
            return 0
        else:
            return last - first
        
    def binarySearch(self, data, k):
        l = 0
        h = len(data)
        while l < h:
            m = l + (h - l) // 2
            if data[m] >= k:
                h = m
            else:
                l = m + 1
        return l
```

```c++
class Solution {
public:
    int GetNumberOfK(vector<int> data ,int k) {
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
};
```

### 38. 二叉树的深度

**题目描述：**

> 输入一棵二叉树，求该树的深度。从根结点到叶结点依次经过的结点（含根、叶结点）形成树的一条路径，最长路径的长度为树的深度。

**解题思路：**

- 递归直接求解即可

**参考代码：**

```python
# python
class Solution:
    def TreeDepth(self, root):
        # write code here
        if root == None:
            return 0
        
        l = self.TreeDepth(root.left)
        r = self.TreeDepth(root.right)
        
        return 1 + (l if l > r else r)
        # return 1 + max(l, r)
```

```c++
class Solution {
public:
    int TreeDepth(TreeNode* root) {
        if (root == nullptr) {
            return 0;
        }

        int left = TreeDepth(root->left);
        int right = TreeDepth(root->right);

        return 1 + (left > right ? left : right);
    }
};
```

### 39. 平衡二叉树

**题目描述：**

> 输入一棵二叉树，判断该二叉树是否是平衡二叉树。

**解题思路：**

- 平衡二叉树的定义就是：左右子树的高度差小于等于1，而且左右子树也是平衡二叉树
- 分析定义，只要递归判断各个结点，保证左右子树的高度差小于等于1即可

**参考代码：**

```python
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution():
    def getTreeHeight(self, root):
        if root == None:
            return 0
        return 1 + max(self.getTreeHeight(root.left), self.getTreeHeight(root.right))
    
    def IsBalanced_Solution(self, root):
        """
        个人解法
        """
        if root == None:
            return True

        l = self.getTreeHeight(root.left)
        r = self.getTreeHeight(root.right)

        l, r = max(l, r), min(l, r)

        return l - r <= 1 and self.IsBalanced_Solution(root.left) and self.IsBalanced_Solution(root.right)
```

```c++
class Solution {
public:
    // 平衡二叉树的定义就是左右子树的高度差小于等于1
    // 因此在递归获取高度时一旦发现不满足，则应退出保存
    // 所以需要借助一个类内的全局变量
    bool isBalanced = true;

    // 首先需要获取高度
    int getTreeHeight(TreeNode* root) {
        if (root == nullptr) {
            return 0;
        }

        int left = getTreeHeight(root->left);
        int right = getTreeHeight(root->right);

        // 调整二者大小，使得 left >= right
        if (left < right) {
            int tmp = left;
            left = right;
            right = tmp;
        }

        if (left - right > 1) {
            isBalanced = false;
        }

        return 1 + left;
    }

    bool isBalanced_Solution(TreeNode* root) {
        if (root == nullptr) {
            return true;
        }

        getTreeHeight(root);
        return isBalanced;
    }
};

```

### 40. 数组中只出现一次的数字

**题目描述：**

> 一个整型数组里除了两个数字之外，其他的数字都出现了两次。请写程序找出这两个只出现一次的数字。

**解题思路：**

- 需要明确关于异或的几条规则：

  两个相同的数异或，结果为0

  一个数异或0，结果是自身

  异或可以交换顺序

  对题目中的设置，依次异或，最终的结果为待求的两个数字之间的异或

- 本题的关键点是，通过异或来寻找一个掩码mask，使得遍历整个数组，将每个元素与这个mask作用后，会出现不同的结果，如0/1/others，这样就能区分为待求的两个目标值。

- (a ^ b) ^ b = a ^ (b ^ b) = a ^ 0 = a

- 使用 diff = a ^b

  diff &= -diff

  可以获取一个只有一位为1的掩码mask，如00100，表明a和b最右边开始第一个不同的数位的位置，因此可以遍历整个数组，迭代异或看最终结果是否为1来区分a或b

  （注意，其他的元素不影响，因为是偶数次出现，因此连续异或时最终的影响会抵消）

**参考代码：**

```python
# -*- coding:utf-8 -*-
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        # 投机取巧的方式
        result = []
        if array == []:
            return result
        
        for i in array:
            if array.count(i) == 1:
                result.append(i)
        
        return result
```

```c++
class Solution {
public:
    void FindNumsAppearOnce(std::vector<int> data, int* num1, int* num2) {
        if (data.empty()) {
            return;
        }

        int diff = 0;
        for (auto i : data) {
            diff ^= i;
        }
        diff &= -diff;

        *num1 = 0;
        *num2 = 0;
        for (auto i : data) {
            if ((i & diff) == 0) {
                *num1 ^= i;
            } else {
                *num2 ^= i;
            }
        }
    }
};
```

### 41. 和为S的连续正数序列

**题目描述：**

> 小明很喜欢数学,有一天他在做数学作业时,要求计算出9~16的和,他马上就写出了正确答案是100。但是他并不满足于此,他在想究竟有多少种连续的正数序列的和为100(至少包括两个数)。没多久,他就得到另一组连续正数和为100的序列:18,19,20,21,22。现在把问题交给你,你能不能也很快的找出所有和为S的连续正数序列? Good Luck!（输出所有和为S的连续正数序列。序列内按照从小至大的顺序，序列间按照开始数字从小到大的顺序）

**解题思路：**

- 分析：本质是等差序列求和的问题
- 常规思路：根据能否整数进行因数分解，特别注意是对 2*sum 进行因数分解，结果为 num * midTwice，然后根据 [num, midTwice] 组合的奇偶性质，判断能否满足要求，后续利用 [num, midTwice] 来输出 [l, h] 序列。需要注意的地方有：num要从大往小遍历，这样才能保证最终输出的结果是从小到大。另一个就是需要检测一下l的大小，防止l出现小于等于0的情况
- 高效解法：使用双指针，使用中间变量时刻更新当前这两个指针之间的所有元素的和，然后两个指针配合移动，从而实现找到满足条件的解。找到第一个解后，需要跳出并继续寻找下一个解。（这种方式思路简单，但是好像复杂度更高）

**参考代码：**

```python
# -*- coding:utf-8 -*-
class Solution:
    def FindContinuousSequence(self, tsum):
        # write code here
        if tsum < 3:
            return []

        l = 1
        h = 2
        currSum = 3
        result = []

        while l <= tsum // 2 + 1:
            if currSum > tsum:
                currSum -= l
                l += 1
            elif currSum < tsum:
                h += 1
                currSum += h
            else:
                # 此时相等
                result.append(list(range(l, h + 1)))
                currSum -= l
                l += 1

        return result
```

```c++
class Solution {
public:
    // 用于添加的函数
    void add_vec(std::vector<std::vector<int>>& vec, int l, int h) {
        if (l <= 0) {
            return;
        }

        std::vector<int> tmp;
        for (int i = l; i <= h; i++) {
            tmp.push_back(i);
        }
        vec.push_back(tmp);
    }

    // 高效解法
    std::vector<std::vector<int>> FindContinuousSequence(int sum) {
        std::vector<std::vector<int>> result;
        if (sum < 3) {
            return result;
        }

        int l = 1;
        int h = 2;
        int currSum = 3;

        while (h <= sum / 2 + 1) {
            if (currSum > sum) {
                currSum -= l;
                l++;
            } else if (currSum < sum) {
                h++;
                currSum += h;
            } else {
                // 此时相等
                add_vec(result, l, h);
                currSum -= l;
                l++;
            }
        }
        
        return result;
    }
}
```

### 42. 和为S的两个数字

**题目描述：**

> 输入一个递增排序的数组和一个数字S，在数组中查找两个数，使得他们的和正好是S，如果有多对数字的和等于S，输出两个数的乘积最小的。（对应每个测试案例，输出两个数，小的先输出。）

**解题思路：**

- 使用双指针，配合从两端向中间查找，首先查找到满足要求的两个数即为输出结果。

**参考代码：**

```python
# -*- coding:utf-8 -*-
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        if array == []:
            return []

        l = 0
        h = len(array) - 1
        currSum = 0

        while l < h:
            currSum = array[l] + array[h]
            if currSum == tsum:
                return [array[l], array[h]]
            elif currSum < tsum:
                l += 1
            elif currSum > tsum:
                h -= 1

        return []
```

```c++
class Solution {
public:
    vector<int> FindNumbersWithSum(vector<int> array,int sum) {
        // 使用双指针
        vector<int> result;
        if (array.empty()) {
            return result;
        }
        
        int l = 0;
        int h = array.size() - 1;
        int currSum = 0;
        
        while (l < h) {
            currSum = array[l] + array[h];
            if (currSum == sum) {
                result.push_back(array[l]);
                result.push_back(array[h]);
                return result;
            } else if (currSum < sum) {
                l++;
            } else if (currSum > sum) {
                h--;
            }
        }
        
        return result;
    }
};
```

### 43. 左旋转字符串

**题目描述：**

> 汇编语言中有一种移位指令叫做循环左移（ROL），现在有个简单的任务，就是用字符串模拟这个指令的运算结果。对于一个给定的字符序列S，请你把其循环左移K位后的序列输出。例如，字符序列S=”abcXYZdef”,要求输出循环左移3位后的结果，即“XYZdefabc”。是不是很简单？OK，搞定它！

**解题思路：**

- 常规解法：直接借助stl实现子串切分以及拼接

**参考代码：**

```python
class Solution():
    def LeftRotateString(self, s, n):
        """
        借助下标操作的解法
        """
        if s == "" or n == 0:
            return s
        
        return s[n:] + s[0:n]

    def str_reverse(self, s, l ,h):
        """
        对s[l:h]实现翻转
        """
        tmp = list(s)
        while l < h:
            tmp[l], tmp[h] = tmp[h], tmp[l]
            l += 1
            h -= 1
        s = str(tmp)

    def LeftRotateString2(self, s, n):
        if s == "" or n == 0:
            return s
        
        # 没有对输入的s进行保护
        self.str_reverse(s, 0, n - 1)
        self.str_reverse(s, n, len(s) - 1)
        self.str_reverse(s, 0, len(s) - 1)
        return s
```

```c++
class Solution {
public:
    string LeftRotateString(string str, int n) {
        if (str.empty() || n == 0) {
            return str;
        }
        return str.substr(n, str.size() - n) + str.substr(0, n);
    }

    // 高效解法：两部分分别翻转，然后整体翻转
    void str_reverse(std::string& str, int l, int h) {
        while (l < h) {
            char tmp = str[l];
            str[l] = str[h];
            str[h] = tmp;
            l++;
            h--;
        }
    }

    std::string LeftRotateString(std::string str, int n) {
        if (str.empty() || n == 0) {
            return str;
        }

        str_reverse(str, 0, n - 1);
        str_reverse(str, n, str.size() - 1);
        str_reverse(str, 0, str.size() - 1);
        return str;
    }
};
```

### 44. 翻转单词顺序列

**题目描述：**

> 牛客最近来了一个新员工Fish，每天早晨总是会拿着一本英文杂志，写些句子在本子上。同事Cat对Fish写的内容颇感兴趣，有一天他向Fish借来翻看，但却读不懂它的意思。例如，“student. a am I”。后来才意识到，这家伙原来把句子单词的顺序翻转了，正确的句子应该是“I am a student.”。Cat对一一的翻转这些单词顺序可不在行，你能帮助他么？

**解题思路：**

- 暴力解法：借助python-stl，实现字符串分割，翻转
- 常规解法：先翻转每个单词，然后再翻转整个字符串（优点是不需要额外的空间）

**参考代码：**

```python
class Solution():
    def ReverseSentence(self, s):
        """
        pythonic解法
        """
        if s == "":
            return s

        tmp = s.split(" ")
        tmp.reverse()
        return " ".join(tmp)

    def str_reverse(self, s, l, h):
        tmp = list(s)
        while l < h:
            tmp[l], tmp[h] = tmp[h], tmp[l]
            l += 1
            h -= 1
        s = str(tmp)
        
    def ReverseSentence2(self, s):
        """
        字符串翻转法
        """
        if s == "":
            return s

        l = 0
        h = 0
        length = len(s)

        while l <= h and h <= length:
            if h == length or s[h] == " ":
                self.str_reverse(s, l, h - 1)
                l = h + 1
            h += 1
        self.str_reverse(s, 0, length - 1)

        return s
```

```c++
class Solution {
public:
    // 简化版
    std::string ReverseSentence(std::string str) {
        if (str.empty()) {
            return str;
        }

        int l = 0;
        int h = 0;
        int length = str.size();

        // 开头是空格也可以处理
        while (l <= h && h <= length) {
            if (h == length || str[h] == ' ') {
                str_reverse(str, l, h - 1);
                l = h + 1; // 跳过了每次的空格
            }
            h++;
        }
        str_reverse(str, 0, length - 1);

        return str;
    }

    // 翻转字符串
    void str_reverse(std::string& str, int l, int h) {
        char tmp = '\0';
        while (l < h) {
            tmp = str[l];
            str[l] = str[h];
            str[h] = tmp;
            l++;
            h--;
        }
    }
};
```

### 45. 扑克牌顺子

**题目描述：**

> LL今天心情特别好,因为他去买了一副扑克牌,发现里面居然有2个大王,2个小王(一副牌原本是54张^_^)...他随机从中抽出了5张牌,想测测自己的手气,看看能不能抽到顺子,如果抽到的话,他决定去买体育彩票,嘿嘿！！“红心A,黑桃3,小王,大王,方片5”,“Oh My God!”不是顺子.....LL不高兴了,他想了想,决定大\小 王可以看成任何数字,并且A看作1,J为11,Q为12,K为13。上面的5张牌就可以变成“1,2,3,4,5”(大小王分别看作2和4),“So Lucky!”。LL决定去买体育彩票啦。 现在,要求你使用这幅牌模拟上面的过程,然后告诉我们LL的运气如何， 如果牌能组成顺子就输出true，否则就输出false。为了方便起见,你可以认为大小王是0。

**解题思路：**

- 这道题的主要含义是指：输入一个vector，数量和数值大小未知，也有可能相等（需要保证是5个数，并且每个数都在0-13之间），判断能否构成顺子，其中0可以代替1-13中的任意一个数。

- 个人常规解法：

  1）判断元素个数是否为5，不是则返回false

  2）遍历全部元素，判断是否位于[0, 13]区间，获取大小王个数（即0的个数，也就是癞子），获取除0外最小值，最大值

  3）分情况讨论：4个癞子，true；其它情况，min != max && max - min <= 4，true；其它情况，false

- 参考答案解法：中间增加了排序，，然后从没有癞子的地方开始补全，根据前后两个元素的差值来选择使用相应数量的癞子补全，最终检测剩余癞子的个数是否大于等于0，代码更加简化

**参考代码：**

```python
class Solution():
    def IsContinuous(self, numbers):
        if len(numbers) != 5:
            return False
        
        nmin = 14
        nmax = 0
        zero_cnt = numbers.count(0)

        for i in numbers:
            if i == 0:
                continue
            if i < nmin:
                nmin = i
            if i > nmax:
                nmax = i
        
        if nmin < 0 or nmax > 13:
            return False

        if zero_cnt == 4 or (nmax - nmin <= 4 and nmax != nmin):
            return True
        else:
            return False

    def IsContinuous2(self, numbers):
        """
        参考答案，癞子补全法
        """
        if len(numbers) != 5:
            return False
        
        numbers.sort()
        cnt = numbers.count(0)

        for i in range(cnt, len(numbers) - 1):
            if numbers[i] == numbers[i + 1]:
                return False
            cnt -= numbers[i + 1] - numbers[i] - 1
        
        return cnt >= 0
```

```c++
#include <algorithm>
class Solution {
public:
    // 个人解法
    bool IsContinuous(std::vector<int> numbers) {
        if (numbers.size() != 5) {
            return false;
        }

        int min = 14;
        int max = 0;
        int zero_cnt = 0;

        for (auto i : numbers) {
            if (i < 0 && i > 13) {
                return false;
            } else if (i == 0) {
                zero_cnt++;
                continue;
            }
            
            // 位于[1, 13]
            if (i < min) {
                min = i;
            }
            if (i > max) {
                max = i;
            }
        }

        if (zero_cnt == 4 || (max - min <= 4 && min != max)) {
            return true;
        } else {
            return false;
        }
    }

    // 参考答案解法
    bool IsContinuous2(std::vector<int> numbers) {
        if (numbers.size() != 5) {
            return false;
        }
        sort(numbers.begin(), numbers.end());

        int cnt = 0;
        for (auto i : numbers) {
            if (i == 0) {
                cnt++;
            }
        }

        // 从没有癞子的地方开始，使用癞子去补全顺子
        for (int i = cnt; i < numbers.size() - 1; i++) {
            if (numbers[i] == numbers[i + 1]) {
                return false;
            }
            // 差值为n，则使用n个癞子进行补全
            cnt -= numbers[i + 1] - numbers[i] - 1;
        }

        return cnt >= 0;
    }
};
```

### 46. 圆圈中最后剩下的数

**题目描述：**

> 每年六一儿童节,牛客都会准备一些小礼物去看望孤儿院的小朋友,今年亦是如此。HF作为牛客的资深元老,自然也准备了一些小游戏。其中,有个游戏是这样的:首先,让小朋友们围成一个大圈。然后,他随机指定一个数m,让编号为0的小朋友开始报数。每次喊到m-1的那个小朋友要出列唱首歌,然后可以在礼品箱中任意的挑选礼物,并且不再回到圈中,从他的下一个小朋友开始,继续0...m-1报数....这样下去....直到剩下最后一个小朋友,可以不用表演,并且拿到牛客名贵的“名侦探柯南”典藏版(名额有限哦!!^_^)。请你试着想下,哪个小朋友会得到这份礼品呢？(注：小朋友的编号是从0到n-1)
>
> 如果没有小朋友，请返回-1

**解题思路：**

- 常规思路：使用数组来模拟报数的过程，循环求解。（或者使用链表来求解，单向循环列表，每个结点存储是否被选中的标志bool sign，不断遍历该链表，根据m来选中结点，知道剩下一个结点退出）
- 本质是一个约瑟夫环的问题，考虑编号为[0, 1, 2, ..., m-1, m, ..., n - 1]的序列，排除编号为[m - 1]后的序列为[0, 1, 2, ..., m, ..., n - 1]。将该序列看做从[m]开始的新序列为[m, ..., n - 1, 0, 1, 2, ..., m - 2]，此时通过可以通过公式映射为新序列[0, 1, 2, ..., m-1, m, ..., n - 2]，由此成为一个新的子问题。
- 所以可以利用递归或者反向迭代的思路来解决，考虑最终的的递归退出条件为n=1，此时返回0。
- 考虑递推公式为：s(n) = (s(n-1) + m) % n，这个公式的含义是，将在长度为n-1的解的索引变换到长度为n的序列中的索引。（最终长度为1时的解为0，需要借助该公式不断迭代，得到长度为n时的解）

**参考代码：**

```python
class Solution:
    def LastRemaining_Solution(self, n, m):
        # write code here
        if n <= 0 or m <= 0:
            return -1
        
        tsum = 0
        for i in range(2, n + 1) :
            tsum = (tsum + m) % i
        
        return tsum
```

```c++
class Solution {
public:
    // 暴力枚举
    int LastRemaining_Solution(int n, int m) {
        if (n <= 0 || m <= 0) {
            return -1;
        }

        int sign[n] = {0};
        int count = n;
        int index = -1;
        int step = 0;

        while (count > 0) { // 全部删除，则最后一个就是待求
            index++;
            if (index >= n) { // 确保环形遍历
                index = 0;
            }
            if (sign[index] == 1) { // 跳过删除的元素
                continue;
            }
            step++;
            if (step == m) { // 确定找到了下一个元素
                sign[index] = 1;
                count--;
                step = 0;
            }
        }

        return index;
    }

    // 其它方法
    int LastRemaining_Solution2(int n, int m) {
        if (n == 0) {
            return -1;
        }

        int s = 0;
        for (int i = 2; i <= n; i++) {
            // 这个公式可以由递归得到
            s = (s + m) % i;
        }
        return s;
    }

    // 其它方法
    int LastRemaining_Solution3(int n, int m) {
        if (n == 0) {
            return -1;
        }
        if (n == 1) {
            return 0;
        }

        return (LastRemaining_Solution3(n - 1, m) + m) % n;
    }

    // 需补充单向循环链表方法
    int LastRemaining_Solution4(int n, int m) {}
};
```

### 47. 前N项正整数求和

**题目描述：**

> 求1+2+3+...+n，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。

**解题思路：**

- 根据题目，可以使用的运算符有：加法、减法、移位运算。
- 由于不能使用if语句，因此正常形式的递归也无法使用，但是可以借助&&的短路特性来实现递归。（暴力累加）
- 公式法：(n+1)*n/2，需要考虑如何实现乘法，可以利用sizeof(二维数组实现)，也可以利用pow(n, 2) + n，来实现，最终利用右移位实现除法。

**参考代码：**

```python
class Solution():
    def Sum_Solution(self, n):
        """
        递归解法
        """
        tmp = n and self.Sum_Solution(n - 1)
        return n + tmp

    def Sum_Solution2(self, n):
        return sum(list(range(1, n + 1)))

    def Sum_Solution3(self, n):
        return (n**2 + n) >> 1
```

```c++
class Solution {
public:
    // 递归解法
    int Sum_Solution(int n) {
        int sum = n;
        bool tmp = n > 0 && (sum += Sum_Solution(n - 1)) > 0;
        return sum;
    }

    // 其它解法
    int Sum_Solution2(int n) {
        char tmp[n][n+1];
        return sizeof(tmp) >> 1;
    }

    int Sum_Solution3(int n) {
        return (int(pow(n, 2)) + n) >> 1;
    }

    // 自定义乘法
    int multiply(int a, int b) {
        int res = 0;
        (a&1) && (res += b);
        a >>= 1; b <<=1;
        a && (res += multiply(a, b));
        return res;
    }

    int Sum_Solution4(int n) {
        return multiply(n, n + 1) >> 1;
    }
};
```

### 48. 不用加减乘除做加法

**题目描述：**

> 写一个函数，求两个整数之和，要求在函数体内不得使用+、-、*、/四则运算符号。

**解题思路：**

- 本质是数字电路中对加法器的实现
- 一位加法器：a^b为本位和，(a&b) <<1为进位

- 对每位执行一位加法，整体上可以借助递归实现
- 注意：本位和与进位之间也是加法的运算
- 也可以通过循环来实现

**参考代码：**

```python
class Solution():
    def Add(self, a, b):
        """
        递归法
        """
        tmp = a if b == 0 else self.Add((a^b) & 0xffffffff,
                                        ((a&b) << 1) & 0xffffffff)
        return tmp if tmp < 0x7fffffff else ~(tmp ^ 0xffffffff)

    def Add2(self, a, b):
        """
        循环
        """
        while b != 0:
            tmp = (a ^ b) & 0xffffffff
            b = ((a & b) << 1) & 0xffffffff
            a = tmp if tmp < 0x7fffffff else ~(tmp ^ 0xffffffff)
        return a


def main():
    s = Solution()
    print(s.Add(10 ,-12))
    print(s.Add2(10, -12))
```

```c++
class Solution {
public:
    // 递归实现
    int Add(int a, int b) {
        return b == 0 ? a : Add(a ^ b, (a & b) << 1);
    }

    // 循环实现
    int Add2(int a, int b) {
        int tmp = 0;
        while (b != 0) {
            tmp = a ^ b;
            b = (a & b) << 1;
            a = tmp;
        }
        return a;
    }
};
```

### 49. 把字符串转换成整数

**题目描述：**

> 将一个字符串转换成一个整数，要求不能使用字符串转换整数的库函数。 数值为0或者字符串不是一个合法的数值则返回0。输入一个字符串,包括数字字母符号,可以为空，如果是合法的数值表达则返回该数字，否则返回0。

**解题思路：**

- 关键点在于：特殊情况分析，考虑正负号，考虑非法数值，考虑int溢出

**参考代码：**

```python
# -*- coding:utf-8 -*-
class Solution:
    def StrToInt(self, s):
        # write code here
        if s == "":
            return 0
        
        sign = 1
        tsum = 0
        for i in range(0, len(s)):
            if i == 0 and s[i] == "-":
                sign = -1
                continue
            if i == 0 and s[i] == "+":
                continue
            if s[i] < "0" or s[i] > "9":
                return 0
            tsum = tsum * 10 + ord(s[i]) - ord("0")
        tsum *= sign
        
        if tsum >= 2**31 or tsum < -2**31:
            return 0
        else:
            return tsum
```

```c++
#include <cmath>
class Solution {
public:
    int StrToInt(string str) {
        if (str.empty()) {
            return 0;
        }
        
        int sign = 1;
        long sum = 0;
        for (int i = 0; i < str.size(); i++) {
            if (i == 0 && str[i] == '-') {
                sign = -1;
                continue;
            }
            if (i == 0 && str[i] == '+') {
                continue;
            }
            if (str[i] < '0' || str[i] > '9') {
                return 0;
            }
            sum = sum * 10 + str[i] - '0';
        }
        sum *= sign;
        
        // 溢出判断
        if (sum >= pow(2, 31) || sum < -pow(2, 31)) {
            return 0;
        } else {
            return sum;
        }
    }
};
```


### 50. 数组中重复的数字

**题目描述：**

> 在一个长度为n的数组里的所有数字都在0到n-1的范围内。 数组中某些数字是重复的，但不知道有几个数字是重复的。也不知道每个数字重复几次。请找出数组中任意一个重复的数字。 例如，如果输入长度为7的数组{2,3,1,0,2,5,3}，那么对应的输出是第一个重复的数字2。

**解题思路：**

- 考察知识点：数组，哈希
- 暴力枚举：二重循环遍历，每个位置与后续的全部位置进行比较，复杂度是O(N^2)
- 哈希思路：使用map或者set来解题
- 高效思路：考虑到题目中给出了对原始数组的限制，即**长度为N的数组，元素取值为0~N-1**，因此必然有重复。考虑到如果把数组完全升序排序，则一定会有**位置i处的元素值不是i**的情况发生，因此本题考察的就是如何进行元素位置的移动，使得尽快出现**位置i处的元素值不是i**的情况发生
- 需要注意：python/C++在进行数组内元素交换的时候的方法，nums[nums[i]]的使用

**参考代码：**

```cpp
// cpp
class Solution {
public:
    bool duplicate(int nums[], int length, int* duplication) {
        for (int i = 0; i < length; i++) {
            while (nums[i] != i) {
                if (nums[i] == nums[nums[i]]) {
                    duplication[0] = nums[i];
                    return true;
                }
                int curr = nums[i];
                nums[i] = nums[curr];
                nums[curr] = curr;
            }
        }      
        return false;
    }
};
```

```python
# python
class solution():
    def duplicate(self, nums, duplication):
        for i in range(len(nums)):
            while nums[i] != i:
                if nums[i] == nums[nums[i]]:
                    duplication[0] = nums[i]
                    return True
                else:
                    nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
        return False
```

### 51. 构建乘积数组

**题目描述：**

> 给定一个数组A[0,1,...,n-1],请构建一个数组B[0,1,...,n-1],其中B中的元素B[i]=A[0]*A[1]*...*A[i-1]*A[i+1]*...*A[n-1]。不能使用除法。（注意：规定B[0] = A[1] * A[2] * ... * A[n-1]，B[n-1] = A[0] * A[1] * ... * A[n-2];）

**解题思路：**

- 待补充

**参考代码：**

```python
# -*- coding:utf-8 -*-
class Solution:
    def multiply(self, A):
        # write code here
        if len(A) == 0:
            return []
        ret = [0] * len(A)
        
        tmp = 1
        for i in range(0, len(A)):
            ret[i] = tmp
            tmp *= A[i]
        
        tmp = 1
        for i in range(len(A) - 1, -1, -1):
            ret[i] *= tmp
            tmp *= A[i]
        
        return ret
```

```C++
// c++
class Solution {
public:
    vector<int> multiply(const vector<int>& A) {
        vector<int> ret;
        if (A.empty()) {
            return ret;
        }
        
        for (int i = 0; i < A.size(); i++) {
            int tmp = 1;
            for (int j = 0; j < A.size(); j++) {
                if (j != i) {
                    tmp *= A[j]; 
                }
            }
            ret.push_back(tmp);
        }
        
        return ret;
    }
};
```

### 52. 正则表达式匹配

**题目描述：**

> 请实现一个函数用来匹配包括'.'和'*'的正则表达式。模式中的字符'.'表示任意一个字符，而'*'表示它前面的字符可以出现任意次（包含0次）。 在本题中，匹配是指字符串的所有字符匹配整个模式。例如，字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，但是与"aa.a"和"ab*a"均不匹配

**解题思路：**

- 两种思路，一是递归，二是循环
- 关键是把各种情况讨论清楚
- 递归回溯法，其实就是把所有可能的情况全部试一遍，通过不停的剪去s和p相同的首部，直到某一个或两个都被剪空，就可以得到结论了

**参考代码：**

```python
# -*- coding:utf-8 -*-
class Solution:
    # s, pattern都是字符串
    def match(self, s, pattern):
        # write code here
        if len(s) == 0 and len(pattern) == 0:
            return True
        elif len(s) != 0 and len(pattern) == 0:
            return False
        elif len(s) == 0  and len(pattern) != 0:
            if len(pattern) > 1 and pattern[1] == "*":
                return self.match(s, pattern[2:])
            else:
                return False
        else: # 二者都非空
            if len(pattern) == 1 or pattern[1] != "*": # 后一位不是 *
                if s[0] == pattern[0] or pattern[0] == ".":
                    return self.match(s[1:], pattern[1:])
                else:
                    return False
            else: # 后一位是 *
                if s[0] != pattern[0] and pattern[0] != ".":
                    return self.match(s, pattern[2:])
                else:
                    return self.match(s[1:], pattern) or self.match(s, pattern[2:])
```

```C++
// c++
class Solution {
public:
    bool match(char* str, char* pattern) {
        if (*str == '\0' && *pattern == '\0') {
            return true;
        }
        if (*str != '\0' && *pattern == '\0') {
            return false;
        }
        
        // 剩下的情况是 *pattern != '\0'
        // 此时考虑 *(pattern + 1) 是否为 '*'
        
        if (*(pattern + 1) != '*') { // 后一位不是 '*'
            if (*str == *pattern || (*str != '\0' && *pattern == '.')) {
                return match(str + 1, pattern + 1);
            } else {
                return false;
            }
        } else { // 后一位是 '*'
            if (*str == *pattern || (*str != '\0' && *pattern == '.')) {
                // 注意这里，不确定 * 会重复几次，因此需要 ||
                return match(str + 1, pattern) || match(str, pattern + 2);
            } else { // * 被当作空
                return match(str, pattern + 2);
            }
        }
    }
};
```

### 53. 表示数值的字符串

**题目描述：**

> 请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。例如，字符串"+100","5e2","-123","3.1416"和"-1E-16"都表示数值。 但是"12e","1a3.14","1.2.3","+-5"和"12e+4.3"都不是。

**解题思路：**

- 主要思路如下：第一个符号位特殊处理，然后while遍历，记录三个情况：has_value，dot_cnt，e_cnt
- 特殊情况返回false或者true，两个*或者.同时出现则false，不能在先有e的情况下出现.，后续出现+-符号位时必须在e后边

**参考代码：**

```python
# -*- coding:utf-8 -*-
class Solution:
    # s字符串
    def isNumeric(self, s):
        # write code here
        if s == None or len(s) == 0:
            return False
        
        e_cnt = 0
        dot_cnt = 0
        has_value = False
        
        i = 0 if s[0] != "+" and s[0] != "-" else 1
        for j in range(i, len(s)):
            if s[j] >= "0" and s[j] <= "9":
                has_value = True
            else:
                has_value = False
                if s[j] == "." and e_cnt == 0:
                    dot_cnt += 1
                elif s[j] == "e" or s[j] == "E":
                    e_cnt += 1
                elif (s[j] == "+" or s[j] == "-") and (s[j-1] == "e" or s[j-1] == "E"):
                    continue
                else:
                    return False
                
                if e_cnt >= 2 or dot_cnt >= 2:
                    return False
        
        return has_value


# 投机取巧解法
def func(self, s):
    try:
        ss = float(s)
        return True
    expect:
        return False

```

```C++
class Solution {
public:
    bool isNumeric(char* str) {
        // 参数合法性判断
        if (str == nullptr) {
            return false;
        }
        
        // 处理首位的符号位
        if (*str == '+' || *str == '-') {
            str++;
        }
        
        // 辅助参数
        int e_cnt = 0;
        int dot_cnt = 0;
        bool has_value = false;
        
        // 为了简化代码
        str--;
        while (*(++str) != '\0') {
            if (*str >= '0' && *str <= '9') {
                has_value = true;
            } else {
                // 以下不会出现数值
                has_value = false;
                if (*str == '.' && e_cnt == 0) { // 注意不能在先有e的情况下出现.
                    dot_cnt++;
                } else if (*str == 'e' || *str == 'E') {
                    e_cnt++;
                } else if ((*str == '+' || *str == '-') && (*(str - 1) == 'e' || *(str - 1) == 'E')) { // 再次出现符号位时，前一位必须为e
                    continue;
                } else {
                    return false;
                }
                
                // 合法性判断
                if (e_cnt >= 2 || dot_cnt >= 2) { // 两个e或者两个.出现时，即为false
                    return false;
                }
            }
        }
        return has_value;
    }

};
```

### 54. 字符流中第一个不重复的字符

**题目描述：**

> 请实现一个函数用来找出字符流中第一个只出现一次的字符。例如，当从字符流中只读出前两个字符"go"时，第一个只出现一次的字符是"g"。当从该字符流中读出前六个字符“google"时，第一个只出现一次的字符是"l"。如果当前字符流没有存在出现一次的字符，返回#字符。

**解题思路：**

- 重点是：使用hash来记录次数，使用string来记录顺序

**参考代码：**

```python
# -*- coding:utf-8 -*-
class Solution:
    # 返回对应char
    def __init__(self):
        self.hash = []
    
    def Insert(self, ch):
        if ch != None:
            self.hash.append(ch)
    
    def FirstAppearingOnce(self):
        for i in self.hash:
            if self.hash.count(i) == 1:
                return i
        return "#"
```

```C++
class Solution
{
public:
    string s; // 用来记录顺序
    char hash[256] = {0};
    
    // Insert one char from stringstream
    void Insert(char ch) {
        s += ch;
        hash[ch]++;
    }
    
    // return the first appearence once char in current stringstream
    char FirstAppearingOnce() {
        for (auto i : s) {
            if (hash[i] == 1) {
                return i;
            }
        }
        
        return '#';
    }
};
```

### 55. 链表中环的入口结点

**题目描述：**

> 给一个链表，若其中包含环，请找出该链表的环的入口结点，否则，输出null。

**解题思路：**

- 利用哈希表直接求解，有其他的高效算法解法，需要看一下

**参考代码：**

```python
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def EntryNodeOfLoop(self, head):
        # write code here
        tmp = []
        while head != None:
            if tmp.count(head) == 0:
                tmp.append(head)
                head = head.next
            else:
                return head
        
        return None
```

```C++
/*
struct ListNode {
    int val;
    struct ListNode *next;
    ListNode(int x) :
        val(x), next(NULL) {
    }
};
*/
class Solution {
public:
    std::map<ListNode*, int> map;
    ListNode* EntryNodeOfLoop(ListNode* head) {
        while (head != nullptr) {
            if (map.count(head) == 0) {
                map[head] = head->val;
                head = head->next;
            } else {
                return head;
            }
        }
        
        return nullptr;
    }
};
```

### 56. 删除链表中重复的结点

**题目描述：**

> 在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，重复的结点不保留，返回链表头指针。 例如，链表1->2->3->3->4->4->5 处理后为 1->2->5

**解题思路：**

- 看似简单，其实很麻烦
- 需要考虑的几点：检测到重复后需要删除，头部也有可能重复，所以需要新加一个头检测
- 可以单独写一个函数，用来判断当前结点的后方有多少个是重复的
- 注意python中传入参数的引用的使用，另一种思路是函数返回多个值

**参考代码：**

```python
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def checkSame(self, head):
        """
        输入一个结点，输出后边有多个个重复的，以及不重复的那个结点
        """
        cnt = 0
        while head != None and head.next != None:
            if head.val != head.next.val:
                return cnt, head.next
            else:
                cnt += 1
                head = head.next
        
        return cnt, None
        
    def deleteDuplication(self, head):
        if head == None:
            return None
        
        new_head = ListNode(0)
        new_head.next = head
        curr = new_head
        
        while curr != None:
            cnt, tmp = self.checkSame(curr.next)
            if cnt == 0:
                curr = curr.next
            else:
                curr.next = tmp
                
        return new_head.next
```

```C++
/*
struct ListNode {
    int val;
    struct ListNode *next;
    ListNode(int x) :
        val(x), next(NULL) {
    }
};
*/
class Solution {
public:
    // 输出一个结点，返回从这里开始有多少个重复的结点，next_head为不重复的下一个结点
    // 这里注意要用引用
    int checkSame(ListNode* head, ListNode* & next_head) {
        int cnt = 0;
        while (head != nullptr && head->next != nullptr) {
            if (head->val != head->next->val) {
                next_head = head->next;
                return cnt;
            } else {
                cnt++;
                head = head->next;
            }
        }
        
        next_head = nullptr;
        return cnt;
    }
    
    ListNode* deleteDuplication(ListNode* head) {
        if (head == nullptr) {
            return nullptr;
        }
        
        // 为了检测head是否存在重复，需要新加一个额外的head
        ListNode* new_head = new ListNode(0);
        new_head->next = head;
        ListNode* curr = new_head;
        ListNode* tmp = nullptr;
        
        while (curr != nullptr) {
            if (checkSame(curr->next, tmp) == 0) {
                curr = curr->next;
            } else {
                curr->next = tmp;
            }
        }
        
        return new_head->next;
    }
};
```

### 57. 二叉树的下一个结点

**题目描述：**

> 给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针。

**解题思路：**

- 分情况讨论即可
- 空，返回nullptr
- 右子树非空，while进行中序遍历，找到最底层的left，输出
- 右子树为空，迭代向上寻找，是父节点的左则输出父节点，是父节点的右则继续迭代

**参考代码：**

```python
# -*- coding:utf-8 -*-
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None
class Solution:
    def GetNext(self, p):
        if p == None:
            return None
        
        if p.right != None:
            p = p.right
            while p.left != None:
                p = p.left
            return p
        else:
            while p.next != None:
                if p == p.next.left:
                    return p.next
                else:
                    p = p.next
            
        return None
```

```C++
/*
struct TreeLinkNode {
    int val;
    struct TreeLinkNode *left;
    struct TreeLinkNode *right;
    struct TreeLinkNode *next;
    TreeLinkNode(int x) :val(x), left(NULL), right(NULL), next(NULL) {
        
    }
};
*/
class Solution {
public:
    TreeLinkNode* GetNext(TreeLinkNode* p) {
        if (p == nullptr) {
            return nullptr;
        }
        
        if (p->right != nullptr) {
            // 右子树非空时，中序遍历右子树，得到一个结点并返回，即最底层的左子树
            p = p->right;
            while (p->left != nullptr) {
                p = p->left;
            }
            return p;
        } else {
            // 右子树为空时，迭代循环，直到满足输出
            // 注意一下循环判断条件为p->next，而非是p非空，坑
            while (p->next != nullptr) {
                if (p == p->next->left){ // 右子树为空，且p是上一级的左，输出
                    return p->next;
                } else { // 右子树为空，且p是上一级的右，迭代
                    p = p->next;
                }
            }
        }
       
        // 最终跳槽循环只可能是，一直是右子树往上迭代，直到顶点
        return nullptr;
    }
};
```

### 58. 对称的二叉树

**题目描述：**

> 请实现一个函数，用来判断一颗二叉树是不是对称的。注意，如果一个二叉树同此二叉树的镜像是同样的，定义其为对称的。

**解题思路：**

- 递归实现，需要注意的点有：
- 叶节点的left和right都是空
- 当前val需要对应相等
- 镜像比较的含义是，left与right比较，right与left比较

**参考代码：**

```python
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def isSame(self, a, b):
        if a == None and b == None:
            return True
        elif a != None and b != None:
            return a.val == b.val and self.isSame(a.left, b.right) and self.isSame(a.right, b.left)
        else:
            return False
    
    def isSymmetrical(self, root):
        # write code here
        if root == None:
            return True
        
        return self.isSame(root.left, root.right)
```

```C++
/*
struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
    TreeNode(int x) :
            val(x), left(NULL), right(NULL) {
    }
};
*/
class Solution {
public:
    bool isSame(TreeNode* a, TreeNode* b) {
        if (a == nullptr && b == nullptr) {
            return true;
        } else if (a != nullptr && b != nullptr) {
            return a->val == b->val && isSame(a->left, b->right) && isSame(a->right, b->left);
        } else {
            return false;
        }
    }
    
    bool isSymmetrical(TreeNode* root) {
        if (root == nullptr) {
            return true;
        }
        
        return isSame(root->left, root->right);
    }

};
```

### 59. 按之字形顺序打印二叉树

**题目描述：**

> 请实现一个函数按照之字形打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右至左的顺序打印，第三行按照从左到右的顺序打印，其他行以此类推。

**解题思路：**

- 本题和下一道题很类似，难点在于控制每层的打印方向，需要增加额外的变量
- 关键点在于每一个curr_list都是倒序遍历，设置sign，0/1分别对应先添加left以及先添加right

**参考代码：**

```python
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def Print(self, root):
        if root == None:
            return []
        
        ret = []
        curr_list = [root]
        sign = 0
        
        while curr_list:
            tmp = []
            next_list = []
            curr_list.reverse()
            
            for i in curr_list:
                tmp.append(i.val)
                if sign == 0:
                    if i.left:
                        next_list.append(i.left)
                    if i.right:
                        next_list.append(i.right)
                else:
                    if i.right:
                        next_list.append(i.right)
                    if i.left:
                        next_list.append(i.left)
            
            ret.append(tmp)
            curr_list = next_list
            sign = 1 - sign
        
        return ret
```

```C++
/*
struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
    TreeNode(int x) :
            val(x), left(NULL), right(NULL) {
    }
};
*/
class Solution {
public:
    vector<vector<int> > Print(TreeNode* root) {
        vector<vector<int>> ret;
        if (root == nullptr) {
            return ret;
        }
        
        int sign = 0; // 表示从左到右
        vector<TreeNode*> curr_list = {root};
        
        while (!curr_list.empty()) {
            vector<int> tmp;
            vector<TreeNode*> next_list;
            
            // 永远是倒序遍历
            // 0先右后左添加，1先左后右添加
            for (int j = curr_list.size() - 1; j >= 0; j--) {
                auto i = curr_list[j];
                tmp.push_back(i->val);
                if (sign == 0) {
                    if (i->left != nullptr) {
                        next_list.push_back(i->left);
                    }
                    if (i->right != nullptr) {
                        next_list.push_back(i->right);
                    }
                } else {
                    if (i->right != nullptr) {
                        next_list.push_back(i->right);
                    }
                    if (i->left != nullptr) {
                        next_list.push_back(i->left);
                    }
                }
            }
            ret.push_back(tmp);
            curr_list = next_list;
            sign = 1 - sign;
        }
        
        return ret;
    }
};
```

### 60. 把二叉树打印成多行

**题目描述：**

> 从上到下按层打印二叉树，同一层结点从左至右输出。每一层输出一行。

**解题思路：**

- 关键是四个vector，ret : 最终输出，curr_list : 当前层结点，next_list : 下一层非空结点，tmp : 当前层结点val
- 步骤：１）循环遍历curr_list，２）把每个结点val整合到tmp，最终整合到ret，３）把每个结点的left, right整合到next_list, 然后赋值给curr_list

**参考代码：**

```python
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, root):
        # write code here
        ret = []
        if root == None:
            return ret
        
        curr_list = [root]
        
        while curr_list:
            tmp = []
            next_list = []
            for i in curr_list:
                tmp.append(i.val)
                if i.left:
                    next_list.append(i.left)
                if i.right:
                    next_list.append(i.right)
            ret.append(tmp)
            curr_list = next_list
            
        return ret
```

```C++
/*
struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
    TreeNode(int x) :
            val(x), left(NULL), right(NULL) {
    }
};
*/
class Solution {
public:
        vector<vector<int> > Print(TreeNode* root) {
            vector<vector<int>> ret;
            if (root == nullptr) {
                return ret;
            }
            
            vector<TreeNode*> curr_list = {root};
            
            while (!curr_list.empty()) {
                // 将curr_list内值整理到ret，同时子结点整理到next_list
                vector<int> tmp;
                vector<TreeNode*> next_list;
                for (auto i : curr_list) {
                    tmp.push_back(i->val);
                    if (i->left != nullptr) {
                        next_list.push_back(i->left);
                    }
                    if (i->right != nullptr) {
                        next_list.push_back(i->right);
                    }
                }
                
                ret.push_back(tmp);
                curr_list = next_list;
            }
            
            return ret;
        }
};
```

### 61. 序列化二叉树

**题目描述：**

> 请实现两个函数，分别用来序列化和反序列化二叉树
>
> 二叉树的序列化是指：把一棵二叉树按照某种遍历方式的结果以某种格式保存为字符串，从而使得内存中建立起来的二叉树可以持久保存。序列化可以基于先序、中序、后序、层序的二叉树遍历方式来进行修改，序列化的结果是一个字符串，序列化时通过 某种符号表示空节点（#），以 ！ 表示一个结点值的结束（value!）。
>
> 二叉树的反序列化是指：根据某种遍历顺序得到的序列化字符串结果str，重构二叉树。

**解题思路：**

- 分析：（1）思考什么表示结束？#，那么！是用来干什么的？（！用来表示当前结点值结束了，如12！）（2）思考返回值是什么？字符串指针
- 需要另外编写两个函数用来递归调用：c++之所以这样做是考虑，生成的str是局部变量，跳出函数后有可能会清空
- 注意python函数参数，如果在函数形式参数中传递list时，使用保持list的引用（针对删除列表元素这个操作，不能使用冒号赋值，需要使用del）
- 更为高效的方式为，每个val或者#后边都加上“，”，这样解析的时候可以直接使用split(",")解析出来“#”或者一个str形式的val

**参考代码：**

```python
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def Serialize(self, root):
        # write code here
        if root == None:
            return "#"
        
        return str(root.val) + "!" + self.Serialize(root.left) + self.Serialize(root.right)
    
    def my_Deserialize(self, s):
        # 传递列表更加方便
        if s[0] == "#":
            s.pop(0)
            return None
        
        # 获取当前值
        index = s.index("!")
        curr_val = int("".join(s[:index]))
        del s[:index + 1]
        #s = s[index + 1:] // 这是错误的方式
        
        currNode = TreeNode(curr_val)
        currNode.left = self.my_Deserialize(s)
        currNode.right = self.my_Deserialize(s)
        
        return currNode
        
    def Deserialize(self, s):
        # 注意字符串参数是传值的
        if s == "":
            return None
        
        tmp = list(s)
        return self.my_Deserialize(tmp)
```

```C++
/*
struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
    TreeNode(int x) :
            val(x), left(NULL), right(NULL) {
    }
};
*/
class Solution {
public:
    std::string ret;
    
    std::string my_Serialize(TreeNode *root) {
        if (root == nullptr) {
            return "#";
        } else {
            // 先序遍历
            return std::to_string(root->val) + "!" + my_Serialize(root->left) + my_Serialize(root->right);
        }
    }
    
    TreeNode* my_Deserialize(char* &str) {
        if (*str == '#') {
            return nullptr;
        }
        
        // 提取当前结点值
        int curr_val = 0;
        while (*str != '!') {
            curr_val = curr_val * 10 + (*str - '0');
            str++;
        }
        
        TreeNode* currNode = new TreeNode(curr_val);
        currNode->left = my_Deserialize(++str);
        currNode->right = my_Deserialize(++str);
        
        return currNode;
    }
    
    char* Serialize(TreeNode *root) {    
        if (root == nullptr) {
            return nullptr;
        }
        
        this->ret = my_Serialize(root);
        return (char*)(ret.c_str());
    }
    
    TreeNode* Deserialize(char *str) {
        if (str == nullptr) {
            return nullptr;
        }
        
        return my_Deserialize(str);
    }
};
```

### 62. 二叉搜索树的第k个结点

**题目描述：**

> 给定一棵二叉搜索树，请找出其中的第k小的结点。例如， （5，3，7，2，4，6，8）    中，按结点数值大小顺序第三小结点的值为4。

**解题思路：**

- 思路一：先整体排序，保存到vector，之后输出所以为k-1的元素
- 高效方法：中序遍历第k个即可，利用全局变量

**参考代码：**

```python
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def __init__(self):
        self.index = 0
    
    def KthNode(self, root, k):
        # 返回对应节点TreeNode
        if root == None or k <= 0:
            return None
        
        tmp = self.KthNode(root.left, k)
        if tmp:
            return tmp
        
        self.index += 1
        if self.index == k:
            return root
        
        tmp = self.KthNode(root.right, k)
        if tmp:
            return tmp
        
        return None
```

```C++
/*
struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
    TreeNode(int x) :
            val(x), left(NULL), right(NULL) {
    }
};
*/
class Solution {
public:
    int index = 0;
    
    TreeNode* KthNode(TreeNode* root, int k) {
        if (root == nullptr or k <= 0) {
            return nullptr;
        }
        
        TreeNode* tmp;
        tmp = KthNode(root->left, k);
        if (tmp) { // 需要提前检测是否要返回
            return tmp;
        }
        
        if (++index == k) {
            return root;
        }
        
        tmp = KthNode(root->right, k);
        if (tmp) { // 需要提前检测是否要返回
            return tmp;
        }
        
        return nullptr; // 如果没有找到
    }
};
```

### 63. 数据流中的中位数

**题目描述：**

> 如何得到一个数据流中的中位数？如果从数据流中读出奇数个数值，那么中位数就是所有数值排序之后位于中间的数值。如果从数据流中读出偶数个数值，那么中位数就是所有数值排序之后中间两个数的平均值。我们使用Insert()方法读取数据流，使用GetMedian()方法获取当前读取数据的中位数。

**解题思路：**

- 主要思路：排序，然后找中位数元素，求解
- 有两种方式，一是借助stl进行排序，二是自行排序

**参考代码：**

```python
# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.data = []
    
    def Insert(self, num):
        # write code here
        self.data.append(num)
        self.data.sort()
    
    def GetMedian(self, not_used):
        # write code here
        length = len(self.data)
        if length == 0:
            return 0.0
        
        if length % 2 == 1:
            return self.data[length // 2]
        else:
            return float(self.data[length // 2] + self.data[length // 2 - 1]) / 2
```

```C++
#include <algorithm>
class Solution {
public:
    std::vector<int> data;
    
    void Insert(int num) {
        data.push_back(num);
        sort(data.begin(), data.end());
    }

    double GetMedian() {
        int length = data.size();
        if (length == 0) {
            return 0.0;
        }
        
        if (length % 2 == 1) {
            return data[length / 2];
        } else {
            return double(data[length / 2] + data[length / 2 - 1]) / 2;
        }
    }
};
```

### 64. 滑动窗口的最大值

**题目描述：**

> 给定一个数组和滑动窗口的大小，找出所有滑动窗口里数值的最大值。例如，如果输入数组{2,3,4,2,6,2,5,1}及滑动窗口的大小3，那么一共存在6个滑动窗口，他们的最大值分别为{4,4,6,6,6,5}； 针对数组{2,3,4,2,6,2,5,1}的滑动窗口有以下6个： {[2,3,4],2,6,2,5,1}， {2,[3,4,2],6,2,5,1}， {2,3,[4,2,6],2,5,1}， {2,3,4,[2,6,2],5,1}， {2,3,4,2,[6,2,5],1}， {2,3,4,2,6,[2,5,1]}。

**解题思路：**

- 常规思路：正常化窗，每次使用stl求最大值
- 高效思路：每次平移后，不需要全部排序求最大值，只需要两点，确定之前的最大值是否被丢弃，新来的值与之前的最大值相比哪个更大
- 其它实现方式：双端队列，两端删除，参考它解法

**参考代码：**

```python
# python
```

```C++
#include <algorithm>
class Solution {
public:
    vector<int> maxInWindows(const vector<int>& num, unsigned int size) {
        vector<int> ret;
        int length = num.size();
        
        if (size > length || size == 0) {
            return ret;
        }
        
        for (int i = 0; i <= length - size; i++) {
            ret.push_back(*std::max_element(num.begin() + i, num.begin() + i + size));
        }
        
        return ret;
    }
};

```

### 65. 矩阵中的路径

**题目描述：**

> 请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。路径可以从矩阵中的任意一个格子开始，每一步可以在矩阵中向左，向右，向上，向下移动一个格子。如果一条路径经过了矩阵中的某一个格子，则该路径不能再进入该格子。

**解题思路：**

- 思路：有些难，递归回溯法
- 更为高效的python版本是直接转换为二维列表（留待后续补充吧）
- 回溯法的基本做法是搜索，或是一种组织得井井有条的，能避免不必要搜索的穷举式搜索法。这种方法适用于解一些组合数相当大的问题。回溯法指导思想——走不通，就掉头。设计过程：确定问题的解空间；确定结点的扩展规则；搜索。

**参考代码：**

```python
# -*- coding:utf-8 -*-
class Solution:
    def hasPath(self, matrix, rows, cols, path):
        # write code here
        if not matrix or not path or rows <= 0 or cols <= 0:
            return False
        
        matrix = list(matrix)        # 原来是一维字符串
        flag = [False] * rows * cols # 表示全都没有遍历过
        
        for i in range(rows):
            for j in range(cols):
                if self.haha(matrix, rows, cols, i, j, path, 0, flag):
                    return True
        
        return False
    
    def haha(self, matrix, rows, cols, i, j, path, k, flag):
        index = i * cols + j
        
        if i < 0 or i >= rows or j < 0 or j >= cols or k >= len(path) or matrix[index] != path[k] or flag[index] == True:
            return False
        
        if k == len(path) - 1:
            return True
        
        flag[index] = True
        
        if self.haha(matrix, rows, cols, i - 1, j, path, k + 1, flag) or \
           self.haha(matrix, rows, cols, i + 1, j, path, k + 1, flag) or \
           self.haha(matrix, rows, cols, i, j - 1, path, k + 1, flag) or \
           self.haha(matrix, rows, cols, i, j + 1, path, k + 1, flag):
            return True
        
        flag[index] = False
        return False
```

```C++
class Solution {
public:
    bool hasPath(char* matrix, int rows, int cols, char* str) {
        // 合法性判断
        if (matrix == nullptr || str == nullptr || rows <= 0 || cols <= 0) {
            return false;
        }
        
        // 标记是否遍历过的数组
        bool* flag = new bool[rows * cols];
        memset(flag, false, rows * cols);
        
        // 遍历整个数组，作为起点，haha判断是否找到路径
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (haha(matrix, rows, cols, i, j, str, 0, flag)) {
                    return true;
                }
            }
        }
        
        // 没有找到
        delete[] flag;
        return false;
    }
    
    bool haha(char* matrix, int rows, int cols, int i, int j, char* str, int k, bool* flag) {
        // 二维索引处理为一维索引
        int index = i * cols + j;
        
        // 递归的合法性判断，直接返回的情况（出界，不等，已经遍历过）
        if (i < 0 || i > rows || j < 0 || j > cols || matrix[index] != str[k] || flag[index] == true) {
            return false;
        }
        
        // 如果str已经到头了，之前的都找到了，则true
        if (str[k + 1] == '\0') {
            return true;
        }
        
        // 标记当前的位置已经遍历过
        flag[index] = true;
        
        // 递归从四个方向回溯
        if (   haha(matrix, rows, cols, i - 1, j, str, k + 1, flag)
            || haha(matrix, rows, cols, i + 1, j, str, k + 1, flag)
            || haha(matrix, rows, cols, i, j - 1, str, k + 1, flag)
            || haha(matrix, rows, cols, i, j + 1, str, k + 1, flag)) {
            return true;
        }
        
        // 如果没有找到，则标记为没有遍历过
        flag[index] = false;
        return false;
    }

};
```

### 66. 机器人的运动范围

**题目描述：**

> 地上有一个m行和n列的方格。一个机器人从坐标0,0的格子开始移动，每一次只能向左，右，上，下四个方向移动一格，但是不能进入行坐标和列坐标的数位之和大抓例如，当k为18时，机器人能够进入方格（35,37），因为3+5+3+7 = 18。但是，它不能进入方格（35,38），因为3+5+3+8 = 19。请问该机器人能够达到多少个格子？

**解题思路：**

- 递归回溯法：走过就标记

**参考代码：**

```python
# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.count = 0
    
    def my_sum(self, a):
        ret = 0
        while a != 0:
            ret += a % 10
            a //= 10
        return ret
    
    def findway (self, threshold, rows, cols, i, j, flag):
        if i < 0 or i >= rows or j < 0 or j >= cols or flag[i][j] == 1:
            return
        
        if self.my_sum(i) + self.my_sum(j) > threshold:
            return
        
        flag[i][j] = 1
        self.count += 1
        
        self.findway(threshold, rows, cols, i + 1, j, flag)
        self.findway(threshold, rows, cols, i - 1, j, flag)
        self.findway(threshold, rows, cols, i, j - 1, flag)
        self.findway(threshold, rows, cols, i, j + 1, flag)
        return
        
    def movingCount(self, threshold, rows, cols):
        # write code here
        if threshold > 0 and rows > 0 and cols > 0:
            flag = [[0 for i in range(cols)] for j in range(rows)]
            self.findway(threshold, rows, cols, 0, 0, flag)
        return self.count
```

```C++
class Solution {
public:
    int cnt = 0;
    bool* flag;
    
    // 获取a的数位之和
    int sum(int a) {
        int ret = 0;
        while (a != 0) {
            ret += a % 10;
            a /= 10;
        }
        return ret;
    }
    
    void search(int threshold, int rows, int cols, int i, int j) {
        int index = i * cols + j;
        
        // 出界或者已经遍历过了，返回
        if (i < 0 || i >= rows || j < 0 || j >= cols || flag[index] == true) {
            return;
        }
        
        // 大于门限返回
        if (sum(i) + sum(j) > threshold) {
            return;
        }
        
        // 当前格子可以进入
        flag[index] = true;
        cnt++;
        
        search(threshold, rows, cols, i + 1, j);
        search(threshold, rows, cols, i - 1, j);
        search(threshold, rows, cols, i, j - 1);
        search(threshold, rows, cols, i, j + 1);
        
    }
    
    int movingCount(int threshold, int rows, int cols) {
        // 合理性判断
        if (threshold <= 0 || rows <= 0 || cols <= 0) {
            return cnt;
        }
        
        flag = new bool[rows * cols];
        memset(flag, false, rows * cols);
        
        search(threshold, rows, cols, 0, 0);
        return cnt;
    }
};
```

### 67. 剪绳子

**题目描述：**

> 给你一根长度为n的绳子，请把绳子剪成整数长的m段（m、n都是整数，n>1并且m>1），每段绳子的长度记为k[0],k[1],...,k[m]。请问k[0]xk[1]x...xk[m]可能的最大乘积是多少？例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。

**解题思路：**

- 有几点先验知识需要考虑：
- 全部分为长度为1的线段，没有意义，乘积为1
- 分为若干段时，这几段越接近，乘积越大（均值不等式）
- 不能出现1，出现1还不如把1加到之前那个上边，乘积更大一些
- 3的效率最高
- 存在高效算法，后续应补充（贪婪算法，动态规划）

**参考代码：**

```python
# -*- coding:utf-8 -*-
class Solution:
    def cutRope(self, n):
        # write code here
        if n <= 3:
            return n - 1
        cnt3 = n // 3 - 1 if n % 3 == 1 else n // 3
        cnt2 = (n - cnt3 * 3) // 2
        return 2**cnt2 * 3**cnt3
```

```C++
个人解法1：
#include<cmath>
class Solution {
public:
    int cutRope(int n) {
        if (n <= 2) {
            return 1;
        }
        
        if (n == 3) {
            return 2;
        }
        
        long ret = 0;
        int cnt2 = (n % 2 == 0 ? n/2 : n/2-1);
        int cnt3 = (n % 2 == 0 ? 0 : 1);
        
        while (cnt2 >= 3) {
            cnt2 -= 3;
            cnt3 += 2;
        }
        
        ret = pow(2, cnt2) * pow(3, cnt3);
        return ret;
    }
};

个人高度优化版：
#include<cmath>
class Solution {
public:
    int cutRope(int n) {
        if (n <= 3) return n - 1;
        int cnt3 = (n % 3 == 1 ? n / 3 - 1 : n / 3);
        int cnt2 = (n - cnt3 * 3) / 2;
        return pow(2, cnt2) * pow(3, cnt3);
    }
};
```
