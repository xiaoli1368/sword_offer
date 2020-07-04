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

- 题目分析：解题时需要考虑原本的字符串会增长，因此需要额外的空间，有两种形式，一是使用string，二是事先申请足够大的字符串数组。（刷题时不需要考虑这些情况，根据形参的类型解题即可）
- 常规思路：利用stl的string，借助临时变量，一次遍历，根据当前字符情况来更新即可，时间复杂度O(n)，空间复杂度O(n)
- 高效思路：对于c形式的字符数组，不借助额外空间，两次遍历，第一次循环确定空格数量从而明确最终的字符串长度，第二次循环从尾到头实现搬移，时间复杂度O(n*2)，空间复杂度O(1)

**参考代码：**

```cpp
// cpp
class Solution {
public:
    // 基于c字符数组，扩容搬移法
    void replaceSpace(char *str, int length) {
        if (str == nullptr || length <= 0) {
            return;
        }

        // 获取空格的长度
        int count = 0;
        for (int i = 0; i < length; i++) {
            if (str[i] == ' ') {
                count++;
            }
        }

        // 从尾部开始搬移
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

    // 基于c++中字符串，借助额外空间
    void replaceSpace(std::string& str) {
        if (str.empty()) {
            return;
        }

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
};
```

```python
# python
class Solution:
    def replaceSpace1(self, s):
        """
        pythonic方法
        """
        return s.replace(" ", "%20")

    def replaceSpace2(self, s):
        """
        扩容替换法
        """
        tmp = ""
        for i in s:
            if i == " ":
                tmp += "%20"
            else:
                tmp += i
        return tmp
```

### 03. 从头到尾打印链表

**题目描述：**

> 输入一个链表，按链表从尾到头的顺序返回一个ArrayList。

**解题思路：**

1. 递归法，递归时间复杂度O(n)，空间复杂度O(1)
2. 使用堆栈，递归就是堆栈实现的，时间复杂度O(2n)，空间复杂度O(n)
3. 头插法形成新的反向链表，然后顺序输出，时间复杂度O(2n)，空间复杂度O(n)
4. 两次遍历，vec尾部添加，时间复杂度O(2n)，空间复杂度O(1)
5. 一次遍历，vec头部添加，时间复杂度O(n)，空间复杂度O(1)，需要调用insert
6. 原链表基础上直接反转，然后顺序输出，其实就是翻转链表了，注意会破坏原有链表，时间复杂度O(2n)，空间复杂度O(1)

**参考代码：**

```cpp
// cpp
typedef struct ListNode {
    int val;
    ListNode* next;
    ListNode (int x, ListNode* ptr) : val(x), next(ptr) {}
} ListNode;

// 2. 使用堆栈，递归就是堆栈实现的
// 时间复杂度O(2n)，空间复杂度O(n)
void printListFromTailToHead2(ListNode* head) {
    if (head == nullptr) {
        return;
    }

    std::stack<int> stack;
    while (head != nullptr) {
        stack.push(head->val);
        head = head->next;
    }

    while (!stack.empty()) {
        this->vec_.push_back(stack.top());
        stack.pop();
    }
}
```

```python
# python
class ListNode():
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def printListFromTailToHead4(self, head):
        """
        4. 两次遍历，vec尾部添加
        """
        if head == None:
            return
        
        length = 0
        currhead = head
        while currhead != None:
            length += 1
            currhead = currhead.next
        
        index = 1
        self.vec_ = [0] * length
        while head != None:
            self.vec_[length - index] = head.val
            head = head.next
            index += 1
```

### 04. 重建二叉树

**题目描述：**

> 输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。

**基础知识：**

- 明确什么是树，这种数据结构采用c++/python该如何实现
- 树的三种遍历方式，分别如何编程实现
- 三种遍历方式中的关系，已知两个顺序，重建整个二叉树
- 注意题目限制：前序和中序的数字不是重复的

**解题思路：**

- 设前序数组为pre，中序数组为vin，寻找pre[0]在vin中的位置，这样就能完成一次划分了
- 将当前的两个数组pre/vin，划分为下一次迭代的四个数组，newLeftPre，newLeftVin，newRightPre，newRightVin
- 完成对当前根节点的构建和赋值，对左右两个子节点，当对应数组的size不为零时，进行下一次的迭代
- 整体的退出条件为：当pre和vin的size都为１时，仅构建根节点并退出（两个孩子节点为null）
- 另外一种高效的思路是，传递数组的引用以及边界索引begin/end，空节点的条件为begin > end

**参考代码：**

```python
// cpp
class Solution {
public:
    // 递归优化版
    TreeNode* reConstructBinaryTree2(std::vector<int> pre, std::vector<int> vin) {
        if (pre.empty() || vin.empty()) {
            return nullptr;
        }

        return reConstructFunc(pre, 0, pre.size() - 1, vin, 0, vin.size() - 1);
    }

    TreeNode* reConstructFunc(std::vector<int>& pre, int p1, int p2, std::vector<int>& vin, int v1, int v2) {
        if (p1 > p2 || v1 > v2) {
            return nullptr;
        }
        
        // 获取划分点坐标
        int vinMid = v1;
        while (vinMid <= v2) {
            if (vin[vinMid] == pre[p1]) {
                break;
            }
            vinMid++;
        }
        int preMid = p1 + vinMid - v1; // 注意二者有可能不是对齐的，所以需要两个mid

        TreeNode* root = new TreeNode(pre[p1]);
        root->left = reConstructFunc(pre, p1+1, preMid, vin, v1, vinMid-1);
        root->right = reConstructFunc(pre, preMid+1, p2, vin,vinMid+1, v2);

        return root;
    }
};
```

```c++
# python
class Solution:
    def reConstructBinaryTree2(self, pre, vin):
        """
        递归优化版
        但是中间重新生成了list，所以低效
        更加高效的方式是传递list引用，以及索引
        """
        if pre == [] or vin == []:
            return None
        
        mid = vin.index(pre[0])
        root = TreeNode.TreeNode(pre[0])
        root.left = self.reConstructBinaryTree2(pre[1:mid+1], vin[:mid])
        root.right = self.reConstructBinaryTree2(pre[mid+1:], vin[mid+1:])

        return root
```

### 05. 用两个栈实现一个队列

**题目描述：**

> 用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。

**解题思路：**

- 使用两个堆栈，借助两次入栈出栈就可以实现一个队列
- 入列：直接进入栈1即可
- 出列：如果堆栈2非空，堆栈2出栈即可，如果堆栈2为空，则将堆栈1的序列循环出栈，并入栈进入堆栈2，然后再调用这个出列函数
- 注意c++可以调用STL中的\<stack>来实现基本的堆栈操作，pop()是出栈操作，但不返回值。top()操作是返回栈顶的值，但是不会出栈
- 举一反三：使用两个队列实现一个栈

**参考代码：**

```c++
// cpp
class Solution {
public:
    // ===== 使用stl定义的栈 =====
    std::stack<int> s1;
    std::stack<int> s2;

    void push(int node) {
        s1.push(node);
    }

    int pop(void) {
        if (s1.empty() && s2.empty()) {
            return 0;
        }

        if (!s2.empty()) {
            int tmp = s2.top();
            s2.pop();
            return tmp;
        } 

        while (!s1.empty()) {
            s2.push(s1.top());
            s1.pop();
        }
        return pop();
    }
};
```

```python
# python
class Solution():
    def __init__(self):
        """
        初始化，使用list封装
        """
        self.s1 = []
        self.s2 = []

    def push(self, val):
        """
        压入
        """
        self.s1.append(val)
    
    def pop(self):
        """
        弹出
        """
        if self.s1 == [] and self.s2 == []:
            return 0
        
        if self.s2 != []:
            return self.s2.pop(-1)
        
        while self.s1:
            self.s2.append(self.s1.pop(-1))
        
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

- 常规思路：递归，编程简单，但是时间复杂度较大O(2^n)，严重超时
- 动态规划：使用数组自底向上迭代，时间复杂度O(n)，空间复杂度O(n)
- 动态规划：使用临时变量互相迭代，时间复杂度O(n)，空间复杂度O(1)
- 注意有可能出想int或long的溢出，可以在迭代内部取余数解决

**参考代码：**

```cpp
// cpp
class Solution {
public:
    // 递归的方式
    int Fibonacci(int n) {
        if (n < 2) {
            return n;
        }
        return Fibonacci(n-1) + Fibonacci(n-2);
    }

    // 动态规划：临时变量
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

```python
# python
class Solution():
    def Fibonacci(self, n):
        """
        递归，时间复杂度较大
        """
        if n < 2:
            return n
        else:
            return self.Fibonacci(n-1) + self.Fibonacci(n-2)

    def Fibonacci4(self, n):
        """
        动态规划，利用临时变量
        """
        if n < 2:
            return n
        
        a, b, c = 0, 1, 0
        for i in range(n-1):
            c = a + b
            a, b = b, c
        return c
```

### 08. 跳台阶

**题目描述：**

> 一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）。

**解题思路：**

- 题目分析：与斐波那契序列类似，区别在于斐波那契数列的前三项为[0, 1, 1]，本题的前三项为[0, 1, 2]
- 类似解题方法见面试题07

**参考代码：**

```cpp
// cpp
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

```python
# python
class Solution:
    def jumpFloor(self, n):
        if n < 3:
            return n

        a, b, c = 1, 2, 3
        for i in range(n - 2):
            c = a + b
            a, b = b, c
        return c
```

### 09. 变态跳台阶

**题目描述：**

> 一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳法。

**解题思路：**

- 题目分析：可以通过找规律，或者递推公式的方式，推导得出通项公式就是2的等比序列。

  > f(n-1) = f(n-2)+f(n-3)+...+f(0)，f(n) = f(n-1)+f(n-2)+f(n-3)+...+f(0)，由此可见f(n)=2*f(n-1)，是一个等比序列，公比为2。
  >
  > 考虑首项为0，第1项为1，因此n!=0时的通项公式为2^(n-1)

- 另外一种思路是通过排列组合，如对于n=15的情况，跳的次数最多的情况是，全部跳1阶且跳15次，以这种情况作为基础。那么考虑1次跳完的情况只能是跳15，此时可以认为情况数是C(14, 0)。之后考虑跳2次跳完的情况，这意味着需要在原来分离的15个台阶中插入一个界限，界限前后的台阶分别合并为一次跳完，总共两次跳完，此时的情况数为C(14, 1)，依次类推，后续的全部情况为(1+1)\^14进行二项式展开，因此对于n阶的情况就是2^(n-1)。


**参考代码：**

  ```cpp
// cpp
class Solution {
public:
    int jumpFloorII(int number) {
        if (number == 0) {
            return 0;
        }
        
        int tmp = 1;
        for (int i = 0; i < number - 1; i++) {
            tmp *= 2;
        }
        return tmp;
    }
};
  ```

```python
# python
class Solution:
    def jumpFloorII(self, n):
        if n == 0:
            return 0
        else:
            return 2**(n - 1)
```

### 10. 矩形覆盖

**题目描述：**

> 我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？

**解题思路：**

- 题目分析:

  > 1) 考虑矩形方格为n\*2，宽为n，高为2，此时考虑第一个填充的小矩形1\*2，有两种方式，立起来（1\*2）或者躺起来（2\*1）。
  >
  > 2) 对于立起来的情况，剩余的矩形面积为(n-1)\*2
  >
  > 3) 对于躺起来的情况，由于要求无覆盖填充，因此必须第二个对应的小矩形也躺起了，和第一个小矩形对齐，因此剩余的矩形面积为(n-2)*2
  >
  > 4) 因此递推公式为f(n) = f(n-1) + f(n-2)

- 因此本题仍然类似斐波那契数列，前三项为[0, 1, 2]

- 参考代码见面试题08

### 11. 二进制中的1

**题目描述：**

> 输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。

**解题思路：**

- 首先，要考虑将负数转为补码表示：c++直接使用类型转换 unsigned int，python需要借助 0xffffffff
- 常规思路：暴力枚举，循环右移，检测最右边二进制位是否为1，缺点需要检测32次
- 高效思路：环使用 n&(n-1) != 0 可以消去原来数中的一位1（注意这种方式运算更快，每次消掉一位1，而且不用考虑符号的问题，但是python的与操作比较特殊，因此仍然需要转换符号）

**参考代码：**

```cpp
// cpp
class Solution {
public:
    // 循环移位法,注意需要转换类型
    // 时间复杂度为O(32)
    int NumberOf1(int n) {
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

    // 依次找最后一位1,不需要转换类型
    // 时间复杂度:O(1的个数)
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

```python
# python
class Solution():
    def NumberOf1(self, n):
        """
        循环移位法
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
        依次找最后一位1
        """
        cnt = 0
        if n < 0:
            n = n & 0xffffffff
        while n != 0:
            cnt += 1
            n = n & (n - 1)
        return cnt
```

### 12. 数值的整数次方

**题目描述：**

> 给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。
>
> 保证base和exponent不同时为0

**解题思路：**

- 常规思路：循环连乘即可，时间复杂度O(n)，n为输入的指数，复杂度过大
- 高效思路：利用二分法实现的快速幂运算，时间复杂度O(logn)
- 注意：指数n为负数的特殊情况，需要取相反数。（但是当n为0x80000000时，即int32下最小的负数，此时取相反数会溢出，可以使用long来处理，另一种方式为使用快速幂运算，不考虑符号位）

**参考代码：**

```cpp
// cpp
class Solution {
public:
    // 暴力循环法，复杂度过大
    // 没有考虑exponent溢出
    double Power2(double base, int exponent) {
        if (base == 0) {
            return 0;
        }

        // 处理符号位
        bool sign = true;
        if (exponent < 0) {
            sign = false;
            exponent = -exponent;
        }

        // 获取结果
        double ret = 1.0;
        for (int i = 0; i < exponent; i++) {
            ret *= base;
        }

        return sign ? ret : 1 / ret;
    }
    
    // 快速幂方法
    // 时间复杂度为o(logn)，不用考虑符号问题
    double Power3(double base, int exponent) {
        if (base == 0) {
            return 0;
        }

        int e = exponent;
        double ret = 1.0;
        while (e != 0) {
            if (e & 1 == 1) { // 奇数无法二分，需要向结果中凑一个base
                ret *= base;
            }
            base *= base;     // base增长为2倍
            //e >>= 1;        // 指数二分，这种方式要保证符合位，因此结果可能永远为负
            e /= 2;           // 这种方式不用考虑符号
        }

        return exponent < 0 ? 1 / ret : ret;
    }
};
```

```python
# python
class Solution():
    def Power2(self, base, exponent):
        """
        快速幂方法，需要处理符号
        """
        if base == 0:
            return 0
        
        ret = 1.0
        sign = True
        if exponent < 0:
            sign = False
            exponent = - exponent

        while exponent != 0:
            if exponent & 1 == 1:
                ret *= base
            base *= base
            exponent >>= 1
        
        return ret if sign else 1 / ret
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
- 第二种方式是：两次遍历，第一次遍历获取总长度，第二次直接找到 length - k 节点
- 第二种方式是：使用快慢间距为k的两个指针进行遍历，当后一个指针到底尾部的时候，第一个指针刚好到达倒数第k个节点

**参考代码：**

```cpp
// cpp
class Solution {
public:
    // 3. 采用双指针的形式
    // 时间复杂度O(n)，空间复杂度O(1)
    ListNode* FindKthToTail3(ListNode* head, unsigned int k) {
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
            return nullptr;
        } else {
            return q;
        }
    }
};
```

```python
# python
class Solution:
    def FindKthToTail1(self, head, k):
        """
        1. 列表存储所有节点
        时间复杂度O(n)，空间复杂度O(n)
        """
        if head == None or k <= 0:
            return None
        
        ptr = []
        while head:
            ptr.append(head)
            head = head.next
        
        if k <= len(ptr):
            return ptr[-k]
        else:
            return None
    
    def FindKthToTail2(self, head, k):
        """
        2. 两重遍历的方式
        时间复杂度O(2n - k)，空间复杂度O(1)
        """
        if head == None or k <= 0:
            return None
        
        length = 0
        curr = head
        while curr != None:
            length += 1
            curr = curr.next
        
        if k > length:
            return None
        
        for i in range(length - k):
            head = head.next
        
        return head
```

### 15. 反转链表

**题目描述：**

> 输入一个链表，反转链表后，输出新链表的表头。

**解题思路：**

- 两种方式，递归法，迭代法，注意画图使节点关系更加清晰
- 注意使用双指针完成，链表相邻节点之间的关系拆除，反向建立链接
- 注意头节点需要特殊对待
- 注意停止循环的标志

**参考代码：**

```cpp
// cpp
class Solution {
public:
    // 递归法
    ListNode* ReverseList3(ListNode* head) {
        if (head == nullptr || head->next == nullptr) {
            return head;
        }

        ListNode* curr = ReverseList3(head->next);
        head->next->next = head; // 需要画图理解
        head->next = nullptr;    // 处理头节点

        return curr;
    }
};
```

```python
# python
class Solution:
    def ReverseList2(self, head):
        """
        迭代法优化版
        """
        if head == None or head.next == None:
            return head
        
        p = head.next
        head.next = None

        while p != None:
            q = p.next
            p.next = head
            head = p
            p = q
        
        return head
```

### 16. 合并两个排序的链表

**题目描述：**

> 输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。

**解题思路：**

- 递归：分解为更小的两个链表之间的合并问题（这个问题有些类似合并两个有序的列表list，递归更加简单，迭代要考虑各种边界条件）
- 循环：直接迭代实现
- 注意：可以new新的节点，也可以直接在两个元时链表上建立新的链接即可（会破坏原有的结构，delete会出现doubel free）
- 举一反三：合并K个有序链表（循环迭代，归并排序）

**参考代码：**

```cpp
// cpp
class Solution {
public:
    // 递归法，创建新的节点
    ListNode* Merge1(ListNode* p, ListNode* q) {
        if (p == nullptr) {
            return q;
        }
        if (q == nullptr) {
            return p;
        }

        ListNode* head = new ListNode(0);
        if (p->val < q->val) {
            head->val = p->val;
            head->next = Merge1(p->next, q);
        } else {
            head->val = q->val;
            head->next = Merge1(q->next, p);
        }

        return head;
    }
    
    // 递归法，直接构建链接
    // 这种方式会对原始链表造成破坏
    ListNode* Merge3(ListNode* p, ListNode* q) {
        if (p == nullptr) {
            return q;
        }
        if (q == nullptr) {
            return p;
        }
        if (p->val < q->val) {
            p->next = Merge3(p->next, q);
            return p;
        } else {
            q->next = Merge3(q->next, p);
            return q;
        }
    }
};
```

```python
# python
class Solution:
    def Merge3(self, pp, qq):
        """
        合并两个递增链表，迭代法，优化版
        """
        # 使用深拷贝隔绝对外界的影响
        p = copy.deepcopy(pp)
        q = copy.deepcopy(qq)

        head = curr = ListNode.ListNode(0)
        while p and q:
            if p.val < q.val:
                curr.next, p = p, p.next
            else:
                curr.next, q = q, q.next
            curr = curr.next
        curr.next = p if p else q

        return head.next
```

### 17. 树的子结构

**题目描述：**

> 输入两棵二叉树A，B，判断B是不是A的子结构。（ps：我们约定空树不是任意一个树的子结构）

**解题思路：**

- 注意子结构可以只是一部分，而非是剩下的全部。可以使用递归去做，依次比较a和b节点的数据值是否相等，如果相等，则返回 func(a.left, b.left) && func(a.right, b.right)，即继续比较a和b的左右子树是否为包含关系。如果二者不等，则返回 func(a.left, b) || func(a.right, b)，即查看a的左右子树中是否存在一个包含b。
- 问题的难点就在于约定了空树不是任何树的子结构，但是递归到最后，返回的条件恰恰就是空树是任何树的子结构。因此需要处理这种矛盾。
- 一种解决方式是：保持空树不是任何树的子结构，当两个比较节点的值相等时，根据b的左右子树是否为空树，再进行下一步的比较。（繁琐）
- 另外一种处理方式为：保持这种约定不变，但是另写一个用于递归的函数（仅使用该一个函数进行递归）。区分开这二者的返回条件。注意由于只使用一个函数递归，所以需要添加flag变量，用来指示之前是否已经对齐。
- 高效方式：两个函数递归，外层控制先序遍历，内层检测每个节点是否存在子结构

**参考代码：**

```cpp
// cpp
class Solution {
public:
    // 3. 两个函数，互相递归，先序遍历（根、左、右）
    bool HasSubTree3(TreeNode* a, TreeNode* b) {
        return (a != nullptr && b != nullptr) && (isSubTree3(a, b) || HasSubTree3(a->left, b) || HasSubTree3(a->right, b));
    }

    // 判断是否是子结构，辅助函数，不进行向下的延伸
    bool isSubTree3(TreeNode* a, TreeNode* b) {
        if (b == nullptr) {
            return true;
        }
        if (a == nullptr || a->val != b->val) {
            return false;
        }
        return isSubTree3(a->left, b->left) && isSubTree3(a->right, b->right);
    }
};
```

```python
# python
class Solution:
    def HasSubtree(self, a, b):
        """
        1. 内部定义递归函数
        注意需要传递flag记录之前是否已经对齐
        """
        def isSubTree(a, b, flag):
            if b == None:
                return True
            if a == None:
                return False
            if flag and a.val != b.val: # 如果之前对齐，本次不等
                return False
            if a.val == b.val and isSubTree(a.left, b.left, True) and isSubTree(a.right, b.right, True):
                return True
            else:
                return isSubTree(a.left, b, False) or isSubTree(a.right, b, False)
  
        # 调用子函数
        if a == None or b == None:
            return False
        return isSubTree(a, b, False) 
```

### 18. 二叉树的镜像

**题目描述：**

> 操作给定的二叉树，将其变换为源二叉树的镜像。（即每个树的左右子树互换即可）

**解题思路：**

- 递归即可，终止的条件为，遇到了空
- 注意不同的实现方式，递归or辅助栈，自顶向下or自底向上，原树操作or返回新树

**参考代码：**

```cpp
// cpp
class Solution {
public:
    // 1. 递归法，自顶向下，在原树上操作
    TreeNode* Mirror1(TreeNode* root) {
        if (root == nullptr) {
            return nullptr;
        }

        // 左右子树交换
        TreeNode* tmp = root->left;
        root->left = root->right;
        root->right = tmp;

        // 递归下一层
        Mirror1(root->left);
        Mirror1(root->right);

        return root;
    }

    // 2. 辅助栈，自顶向下，在原树上操作
    TreeNode* Mirror2(TreeNode* root) {
        if (root == nullptr) {
            return nullptr;
        }

        std::stack<TreeNode*> stack;
        stack.push(root);

        while (!stack.empty()) {
            TreeNode* node = stack.top();
            stack.pop();

            // 交换左右子树
            TreeNode* tmp = node->left;
            node->left = node->right;
            node->right = tmp;

            // 入栈
            if (node->left) {
                stack.push(node->left);
            }
            if (node->right) {
                stack.push(node->right);
            }
        }

        return root;
    }
};
```

```python
# python
class Solution:
    def Mirror3(self, root):
        """
        3. 递归法，自底向上，新建一颗树
        """
        if root == None:
            return None
        
        head = TreeNode.TreeNode(root.val)
        head.left = self.Mirror3(root.right)
        head.right = self.Mirror3(root.left)
        return head
```

### 19. 顺时针打印矩阵

**题目描述：**

> 输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，例如，如果输入如下4 X 4矩阵： 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 则依次打印出数字1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.

**解题思路：**

- 高效思路：将问题理解为打印环形，依次从最外环打印到最内的环。然后采用分治的思想，将每个环的打印，分为四条直线。
- 需要额外注意：终止条件，考虑出现单行或者单列的特殊情况

**参考代码：**

```cpp
// cpp
class Solution {
public:
    // 高效解法：将每圈打印分解为四次直线打印
    std::vector<int> printMatrix(std::vector<std::vector<int>> matrix) {
        if (matrix.empty()) {
            return std::vector<int>{};
        }

        int top = 0;
        int left = 0;
        int bottom = matrix.size() - 1;
        int right = matrix[0].size() - 1;
        std::vector<int> result;

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

```python
# python
class Solution:
    def printMatrix(self, matrix):
        """
        高效方式，顺时针打印矩阵
        """
        if matrix == []:
            return

        top = 0
        left = 0
        bottom = len(matrix) - 1
        right = len(matrix[0]) - 1
        result = []

        while top <= bottom and left <= right:
            # 上横线
            for i in range(left, right + 1):
                result.append(matrix[top][i])
            # 右竖线
            for i in range(top+1, bottom+1):
                result.append(matrix[i][right])
            # 下横线
            if top != bottom:
                for i in range(right-1, left-1, -1):
                    result.append(matrix[bottom][i])
            # 左竖线
            if left != right:
                for i in range(bottom-1, top, -1):
                    result.append(matrix[i][left])
            # 更新        
            top += 1
            bottom -= 1
            left += 1
            right -= 1
        
        return result
```

### 20. 包含min函数的栈

**题目描述：**

> 定义栈的数据结构，请在该类型中实现一个能够得到栈中所含最小元素的min函数（时间复杂度应为O（1））。注意：保证测试中不会当栈为空的时候，对栈调用pop()或者min()或者top()方法。

**解题思路：**

- 注意关键点在于限制了min函数的时间复杂度为-1，也就是跟存储数据量的大小没有关系，因此必须额外分配一个数据结构来记录当前的最小值，即辅助的最小栈，最小栈有两种方式。
- 一是与原始栈等长，每次push数据到stack，同时也比较得出minValue，将其push到minStack。
- 二是与原始栈不等长，每次push数据到stack，只选择数据小于等于minStack顶部时，将其push到minStack，每次pop时需要判断是否需要对minStack进行pop

**参考代码：**

```cpp
// cpp
// 等长最小栈，存在数据冗余
class Solution {
private:
    std::stack<int> stack;
    std::stack<int> minStack;
public:
    void push(int value) {
        if (minStack.empty() || value <= minStack.top()) {
            minStack.push(value);
        } else {
            minStack.push(minStack.top());
        } 
        stack.push(value);
    }

    void pop() {
        minStack.pop();
        stack.pop();
    }

    int top() {
        return stack.top();
    }

    int min() {
        return minStack.top();
    }
};
```

```python
# python
# 不等长最小栈
class Solution:
    def __init__(self):
        """
        初始化
        """
        self.stack = []
        self.minStack = []

    def push(self, node):
        """
        压入
        """
        self.stack.append(node)
        if self.minStack == [] or node <= self.min():
            self.minStack.append(node)

    def pop(self):
        """
        弹出
        """
        if self.stack[-1] == self.minStack[-1]:
            self.minStack.pop()
        self.stack.pop()

    def top(self):
        """
        获取顶部元素
        """
        return self.stack[-1]

    def min(self):
        """
        获取最小元素
        """
        return self.minStack[-1]
```

### 21. 栈的压入弹出序列

**题目描述：**

> 输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否可能为该栈的弹出顺序。假设压入栈的所有数字均不相等。例如序列1,2,3,4,5是某栈的压入顺序，序列4,5,3,2,1是该压栈序列对应的一个弹出序列，但4,3,5,1,2就不可能是该压栈序列的弹出序列。（注意：这两个序列的长度是相等的）

**解题思路：**

- 个人思路（较为繁琐）：构造一个空栈，实际模拟一下栈的压入和弹出操作，总共的压入次数为pushArray.size()，循环实现这个次数即可，每次循环的内部利用while循环实现弹出操作，判断条件为当前栈非空，并且当前栈的顶部元素等于popArray的首元素，注意当前栈和popArray同步进行弹出的操作，最终判断当前栈是否为空，判断两个序列是否合理
- 高效思路：模拟栈的压入弹出，优化细节

**参考代码：**

```cpp
// cpp
class Solution {
public:
    // 高效答案，小细节：使用计数代替出栈
    bool IsPopOrder3(std::vector<int> pushV, std::vector<int> popV) {
        if (pushV.empty() || popV.empty()) {
            return false;
        }

        int i = 0;
        std::vector<int> stack;
        for (auto num : pushV) {
            stack.push_back(num);
            while (!stack.empty() && stack.back() == popV[i]) {
                i++;
                stack.pop_back();
            }
        }

        return stack.empty();
    }
};
```

```python
# python
class Solution:
    def IsPopOrder3(self, pushV, popV):
        """
        高效方法优化版，使用计数代替了pop
        """
        if pushV == [] or popV == []:
            return False

        i = 0
        stack = []
        for num in pushV:
            stack.append(num)
            while stack != [] and stack[-1] == popV[i]:
                i += 1
                stack.pop()

        return stack == []
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

- 看了别人的答案，才把题目看懂，就不能说的明白些吗？要求完全复制，包括那些随机的没有任何意义的链接。（也就是深拷贝）问题的关键在于顺序遍历时，那些随机的链接无法同样复制。解决方法有多种。
- map关联：首先遍历一遍原链表，创建新链表（赋值label和next），用map关联对应结点；再遍历一遍，更新新链表的random指针。（注意map中应有NULL ----> NULL的映射）
- 图遍历：看作一个有向图，每个节点会出去两条边，使用DFS/BFS完成遍历复制
- 高效迭代法：(1) 在旧链表中创建新链表，此时不处理兄弟节点。(2) 根据旧链表的兄弟节点，初始化新链表的兄弟节点。(3) 从旧链表中拆分得到新链表。（next指针关联，创建新链表的时候，用原结点的next指针指向对应新结点，新结点的next指针指向下一个原结点，以此类推，形成之字形关联。然后，就可以先更新新链表的random指针，再解除next关联，更新next指针。这种方法不需要map来辅助，不管查找next还是random指针都是O(1)的，效率很高。）
- 其它python方法：直接深拷贝，或者使用了递归仅建立链接

**参考代码：**

```cpp
// cpp
class Solution {
public:
    // next指针遍历
    RandomListNode* Clone5(RandomListNode* head) {
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
```

```python
# python
class Solution:
    def Clone2(self, h1):
        """
        dict优化版
        """
        if h1 == None:
            return None
        
        h2 = RandomListNode()
        curr1, curr2 = h1, h2
        dic = {None: None}

        # 完全建立线性节点以及映射
        while curr1:
            curr2.next = RandomListNode(curr1.label)
            curr2 = curr2.next
            dic[curr1] = curr2
            curr1 = curr1.next
        
        # 建立随机节点
        while h1:
            dic[h1].random = dic[h1.random]
            h1 = h1.next
        
        return h2.next


    def Clone3(self, head):
        """
        dfs图遍历
        """
        def dfs(head):
            if head == None:
                return None
            if head in dic:
                return dic[head]
            # 创建新节点
            copy = RandomListNode(head.label)
            dic[head] = copy
            copy.next = dfs(head.next)
            copy.random = dfs(head.random)
            return copy
        
        dic = dict()
        return dfs(head)
    
    def Clone4(self, head):
        """
        bfs图遍历
        """
        def bfs(head):
            if head == None:
                return None
            clone = RandomListNode(head.label)
            queue = [head]
            dic = {head : clone, None : None}

            while queue:
                tmp = queue.pop(0)
                if tmp.next != None and tmp.next not in dic:
                    dic[tmp.next] = RandomListNode(tmp.next.label)
                    queue.append(tmp.next)
                if tmp.random!= None and tmp.random not in dic:
                    dic[tmp.random] = RandomListNode(tmp.random.label)
                    queue.append(tmp.random)
                dic[tmp].next = dic[tmp.next]
                dic[tmp].random = dic[tmp.random]
            return clone
        
        return bfs(head)

    def Clone6(self, head):
        """
        深拷贝
        """
        if head == None:
            return None
        return copy.deepcopy(head)
    
    def Clone7(self, head):
        """
        递归法，新链表挂载在旧链表上
        其实就是浅拷贝
        """
        if head == None:
            return None
        
        newhead = RandomListNode(head.label)
        newhead.random = head.random
        newhead.next = self.Clone7(head.next)
        
        return newhead
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

- 题目分析：本质是全排列，使用递归回溯法求解（注意要求结果是否有序或无序）

  > 基本原理：perm(1234) = 1perm(234) + 2perm(134) + 3perm(124) + 4perm(123)
  >
  > 在核心的perm(str, start)函数中，循环调换位置，然后进行后续的递归
  >
  > 递归终止的条件为start == str.size() - 1

- 考虑几个问题：（1）递归实现遍历的两种方式：传递引用或者传值，交换位置。（2）结果是否要求保持字典序。（3）考虑重复的情况，结果中不应该包括重复的元素。

  > 关于重复性的处理：
  >
  > 1）i == start，表示当前情况，继续递归
  >
  > 2）str[i] != str[start] && ifHasSame(str, start, i)，对于区间[start, i]，在考虑调换(start, i)二者的位置时，只有当二者不相等并且中间没有与i相同的元素，才继续递归
  >
  > 关于直接循环替换实现有序以及无重复：
  >
  > 1）对于输入 abc 进行全排列，以下比较两种递归交换方式，第一种传递引用，递归后swap恢复，第二种传递值，递归后不进行swap恢复
  >
  > 2）第一种结果：abc, acb, bac, bca, cba, cab
  >
  > 3）第二种结果：abc, acb, bac, bca, cab, cba
  >
  > 4）可见第二种结果是有序的，注意之所以导数第二个元素会得到 cab，是因为这是在之前的结果 bac 上执行[0, 3]交换得到的
  >
  > 5）至于重复性处理与上同

- 解决思路1：有序版本，借助stl中的全排列函数，直接求解

- 解决思路2：无序版本，递归传递引用来实现遍历，使用set/map来存储，消除重复性

- 解决思路3：有序版本，使用思路2求解，结果使用stl排序

- 解决思路4：有序版本，递归传递引用来实现遍历，使用vector来存储，使用额外判断消除重复性，每次递归使用stl完成排序，实现最终的结果有序

- 解决思路5：有序版本，递归传递值，循环交换实现遍历（同时保证无重复，有序性），缺点为形参传递浪费

- 详细解法见源代码，其它高效解法待补充。

**参考代码：**

```cpp
// cpp
class Solution {
public:
    std::vector<std::string> ret;
    
    // 4. 递归传递值，不使用stl排序，循环替换实现（有序，无重复）
    std::vector<std::string> Permutation4(std::string str) {
        if (str.empty()) {
            return ret;
        }
        
        sort(str.begin(), str.end());
        perm2(str, 0); // 调用perm-method-2
        return ret;
    }

    void perm2(std::string str, int start) {
        if (start == str.size() - 1) {
            ret.push_back(str);
            return;
        }
        
        // 依次交换，并进行下一次的迭代
        for (int i = start; i < str.size(); i++) {
            if (i == start || str[start] != str[i]) { // 跳过重复
                swap(str[i], str[start]);             // 交换
                perm2(str, start + 1);                // 递归
            }
        }
        return;
    }
    
    void swap(char& a, char& b) {
        char tmp = a;
        a = b;
        b = tmp;
    }
};
```

```python
# python
class Solution:
    def __init__(self):
        self.ret = []
    
    def Permutation4(self, ss):
        """
        4. 递归传递值，不使用使用stl排序，循环替换实现（有序，重复）
        """
        if len(ss) == 0:
            return []
        
        self.perm2(sorted(list(ss)), 0)
        return self.ret

    def perm2(self, oriStrList, start):
        """
        有序版本，递归传递值
        输入字符串ss对应的列表oriStrList，以及起始索引start
        注意：
            [1] 这种方式传递了很多次形式参数
            [2] 不需要额外的步骤
        """
        if start == len(oriStrList) - 1:
            self.ret.append("".join(oriStrList))
            return
        
        # 保证值传递
        strList = oriStrList[:]
        
        for i in range(start, len(strList)):
            if i == start or strList[i] != strList[start]:
                strList[i], strList[start] = strList[start], strList[i]
                self.perm1(strList, start + 1)
        return
```

### 28. 数组中出现次数超过一半的数字

**题目描述：**

> 数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。

**解题思路：**

- 常规思路：排序，以length/2进行滑窗[first, last]，array[first]==array[last]则输出

- 哈希思路：借助额外数据结构，一次遍历，统计每个数字的次数，超过一半则输出

- 高效解法：多数投票问题,可以利用 [Boyer-Moore Majority Vote Algorithm](https://www.cs.utexas.edu/~moore/best-ideas/mjrty/index.html) 来解决这个问题,使得时间复杂度为 O(N)），记录两个值（当前投票的数字，当前数字的票数），一次遍历，数字相同则加一票，数字不同则减票，票数为0时把下一票作为新的候选票。由于待求数字超过一半，因此最终票数最多的一定是待求结果，可以参考该算法作者的网页动图[demo](https://www.cs.utexas.edu/~moore/best-ideas/mjrty/example.html#step01)

- 高效解法2：利用之前的知识可得，只要找到数组中值为第k大的元素即可（k = length / 2），因此利用利用快速排序的思想，递归来寻找该数字（这种方法待补充，其实也就是寻找数组中的中位数）

- 举一反三：数组中超过2/3的数字，数组中超过1/3的数字

  >对于数组中超过m的数字（0 < m < 1），当m >= 1/2 时，都可以使用Moore’s Vote Algorithm，结果一致。
  >
  >而当m < 1/2时，此时使用m = 1 / k来代替，需要使用Misra’s Algorithm，频率大于1/k的结果最多有k-1个，因此不能再使用一对值[curr_val, curr_cnt]来表征，需要借助一个候选集合，并没每个候选值都要计数。
  >
  >以下是来自知乎文章的解释：这个算法相比Moore的算法扩充在，cand不再是一个值，而是一个规模大小以K-1为上限的候选集合，记为T，对应着集合中的每个元素都有一个计数。当T的元素个数不足K的时候，则加入到T中。当集合T满的时候，且扫描遇到的元素不在集合T中的时候，则对集合中所有对象的计数全部都减一。

**参考代码：**

```cpp
// cpp
class Solution {
public:
    int MoreThanHalfNum_Solution(std::vector<int> nums) {
        if (nums.empty()) {
            return 0;
        }

        int curr_val = 0;
        int curr_cnt = 0;

        for (auto i : nums) {
            if (curr_cnt == 0) {
                curr_cnt = 1;
                curr_val = i;
            } else {
                curr_cnt += (curr_val == i ? 1 : -1);
            }
        }

        // 此时不存在大于一半的数字
        if (curr_cnt == 0) {
            return 0;
        }

        return curr_val;
    }
};
```

```python
# python
class Solution:
    def MoreThanHalfNum_Solution(self, nums):
        """
        高效方法，多数投票法，复杂度是O(n)
        """
        if nums == []:
            return 0
        
        curr_val = 0
        curr_cnt = 0

        for i in nums:
            if curr_cnt == 0:
                curr_cnt = 1
                curr_val= i
            else:
                curr_cnt += 1 if curr_val == i else -1
        
        # 此时有可能不存在大于一半的数字
        if curr_cnt == 0:
            return 0
        
        return curr_val
```

### 29. 最小的k个数

**题目描述：**

> 输入n个整数，找出其中最小的K个数。例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4,。

**解题思路：**

- 常规思路：排序，之后取前k个值，时间复杂度为stl
- 冒泡排序：从后往前冒泡，依次取最小值、次小值等，遍历k次即可，时间复杂度为O(n*k)
- 基于partition函数，每次随机选择一个参考元素，将当前数组分区为两部分，左侧小于参考元素，右侧大于参考元素，返回当前参考元素的索引。解法为：从[start, end]区间随机获取index的分区，根据与k的大小关系，继续选择[start, index - 1]或者[index + 1, end]分区，依次迭代，直到找到前k个最小值的分区，时间复杂度为O(n)，缺点是会改变原始数组，且前k个最小元素没有排序
- 借助最大堆实现，遍历data数组，前k个元素构成一个长度为k的最大堆，其余元素与堆最大值比较，只有当更小时才进行【入堆，出堆】的更新操作，最终输出k个元素即可，时间复杂度为O(n*logk)，适用于海量数据，n远大于k的情况
- 利用空间换时间，构造长为10000的vec，遍历输入data，执行vec[data[i]]++来累积数量，最后从vec头部取k项有数量的值即可

**参考代码：**

```cpp
// cpp，其它方法见源文件
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

```python
# python，其它方法见源文件
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        if tinput == [] or k > len(tinput):
            return []
        
        tinput.sort()
        return tinput[0:k]
```

### 30. 连续子数组的最大和

**题目描述：**

> HZ偶尔会拿些专业问题来忽悠那些非计算机专业的同学。今天测试组开完会后,他又发话了:在古老的一维模式识别中,常常需要计算连续子向量的最大和,当向量全为正数的时候,问题很好解决。但是,如果向量中包含负数,是否应该包含某个负数,并期望旁边的正数会弥补它呢？例如:{6,-3,-2,7,-15,1,2,2},连续子向量的最大和为8(从第0个开始,到第3个为止)。给一个数组，返回它的最大连续子序列的和，你会不会被他忽悠住？(子向量的长度至少是1)

**解题思路：**

- 常规思路：暴力枚举

- 高效思路：动态规划，初级题目

  > [1] 建模：使用F(i)表示以array[i]为末尾元素的子数组的和的最大值，必须要求以array[i]为结尾
  >
  > [2] 状态转移方程：在已知F(i-1)的情况下如何求F(i)，考虑F(i-1)的大小，根据其正负，选择将当前值array[i]加到之前和上或者直接选择array[i]，即：
  >
  > F(i) = array[i] + (F[i-1] > 0 ? F[i-1] : 0); // 注意无论array[i]是否为正负，都有覆盖array[i]
  >
  > [3] 解：因为F(i)的会遍历整个数组，获取以每个元素为结果的最大子数组和，因此需要额外的变量来记录其中的最大值

**参考代码：**

```cpp
// cpp
class Solution {
public:
    int FindGreatestSumOfSubArray(std::vector<int> array) {
        if (array.empty()) {
            return 0;
        }

        int curr_sum = -1;
        int curr_max = array[0];
        for (auto i : array) {
            curr_sum = i + (curr_sum > 0 ? curr_sum : 0);
            if (curr_max < curr_sum) {
                curr_max = curr_sum;
            }
        }

        return curr_max;
    }
}
```

```python
# Python
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        if array == []:
            return 0
        
        curr_sum = -1
        curr_max = array[0]
        for i in array:
            curr_sum = i + (curr_sum if curr_sum > 0 else 0)
            curr_max = max(curr_max, curr_sum)
        
        return curr_max
```

### 31. 整数中1出现的次数

**题目描述：**

> 求出1-13的整数中1出现的次数,并算出100-1300的整数中1出现的次数？为此他特别数了一下1~13中包含1的数字有1、10、11、12、13因此共出现6次,但是对于后面问题他就没辙了。ACMer希望你们帮帮他,并把问题更加普遍化,可以很快的求出任意非负整数区间中1出现的次数（从1 到 n 中1出现的次数）。

**解题思路：**

- 常规解法：暴力枚举，时间复杂度过大

- 题目分析：出现的总数等于在各个数位上出现次数的和（并不会重复），从个位到最高位依次进行查找，存在三种情况：

  > （1）当前数位为0，次数仅由高位决定，公式为：high * digit
  >
  > （2）当前数位为1，次数由高位和低位共同决定，公式为：high * digit + low + 1
  >
  > （3）当前数位大于1，次数仅由高位决定，公式为：(high + 1) * digit
  
- 举例说明：
  
> （1）以12351为例：
  >
> 考虑个位为1的情况，00001-12341，共有(12345//10 + 1)种，总共1235种
  >
> 考虑十位为1的情况，00010-12310，共有(1234//10 + 1)组，其中每组涵盖10-19，共10种，总共1240种
  >
> 考虑百位为1的情况，00100-12100，共有(123//10 + 1)组，其中每组涵盖00-99，共100种，总共1300种
  >
  > 考虑千位为1的情况，01000-11000，共有(12//10 + 1)组，其中每组函数000-999，共1000种，总共2000种
  >
  > 考虑万位为1的情况，10000-12345，共有(2345+1)，共有2346种
  >
  > （2）以3120为例：
  >
  > 个位为1情况：312 * 1 = 312
  >
> 十位为1情况：(31 + 1) * 10 = 320
  >
  > 百位为1情况：3 * 100 + 20 + 1 = 321
  >
  > 千位为1情况：(0 + 1) * 1000 = 1000

- 其它思路：对于当前数位的情况（0-1比2-9少一个digit），可以利用+8来实现进位的处理

- 拓展思路：对于寻找数字2的出现的次数，原始公式依然成立。

- 举一反三：寻找0-n范围内，数位上含有1的数字（可以出现多次）出现次数，使用排列组合分析，每次后续乘以digit相应减少保证不重复即可

**参考代码：**

```cpp
// cpp
class Solution {
public:
    // 高效解法：直接版，易于理解
    int NumberOf1Between1AndN_Solution2(int n) {
        if (n <= 0) {
            return 0;
        }

        int ret = 0;
        for (int digit = 1; digit <= n; digit *= 10) {
            // 分解数位
            int curr = (n / digit) % 10;
            int high = n / digit / 10;
            int low = n % digit;

            // 分类讨论
            if (curr == 0) {
                ret += high * digit;
            } else if (curr == 1) {
                ret += high * digit + low + 1;
            } else {
                ret += (high + 1) * digit;
            }
        }

        return ret;
    }

    // 高效解法：优化版，不易于理解
    int NumberOf1Between1AndN_Solution3(int n) {
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

```python
# python
class Solution:
    def NumberOf1Between1AndN_Solution3(self, n):
        """
        高效解法：直接版，易于理解
        """
        if n <= 0:
            return 0
        
        ret = 0
        digit = 1

        while digit <= n:
            # 分解数位
            curr = (n // digit) % 10
            high = n // digit // 10
            low = n % digit

            #分类讨论
            if curr == 0:
                ret += high * digit
            elif curr == 1:
                ret += high * digit + low + 1
            else:
                ret += (high + 1) * digit
            
            digit *= 10
        
        return ret

    def NumberOf1Between1AndN_Solution4(self, n):
        """
        高效解法：优化版，不易于理解
        """
        cnt = 0
        m = 1
        while m <= n:
            a = n // m
            b = n % m
            cnt += (a + 8) // 10 * m + (b + 1 if a % 10 == 1 else 0)
            m *= 10
        return cnt
```

### 32. 把数组排成最小的数

**题目描述：**

> 输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。例如输入数组{3，32，321}，则打印出这三个数字能排成的最小数字为321323。

**解题思路：**

- 常规思路：全排列组合，寻找最小的数字（存在的问题：计算量n!过大，同时也存在大数溢出问题）
- 解决大数溢出问题一种直观方式为：将数字转换为字符串
- 高效思路：根据题目要求，自定义新型的字符串比较大小函数，判断数字a和b大小的方式为，先转换为字符串a和b，如果a + b < b + a则有a小于b，然后使用排序算法实现
- 也可以选择其它的排序算法

**参考代码：**

```cpp
//cpp
class Solution {
public:
    std::string PrintMinNumber(std::vector<int> numbers) {
        if (numbers.empty()) {
            return "";
        }

        int length = numbers.size();
        for (int i = 0; i < length - 1; i++) {
            for (int j = i + 1; j < length; j++) {
                std::string a = std::to_string(numbers[i]);
                std::string b = std::to_string(numbers[j]);
                if (a + b > b + a) {
                    int tmp = numbers[i];
                    numbers[i] = numbers[j];
                    numbers[j] = tmp;
                }
            }
        }

        std::string result;
        for (auto i : numbers) {
            result += std::to_string(i);
        }
        return result;
    }
}
```

```python
class Solution:
    def PrintMinNumber(self, numbers):
        if numbers == []:
            return ""

        num = [str(x) for x in numbers]
        for i in range(len(numbers) - 1, 0, -1):
            for j in range(0, i):
                if num[i] + num[j + 1] > num[j + 1] + num[i]: 
                    num[i], num[j + 1] = num[j + 1], num[i]
        
        return "".join(num)
```

### 33. 丑数

**题目描述：**

> 把只包含质因子2、3和5的数称作丑数（Ugly Number）。例如6、8都是丑数，但14不是，因为它包含质因子7。 习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数。

**解题思路：**

- 常规思路：暴力枚举，从1开始遍历，分别使用532进行整除，直到最终无法整除时，依据结果是否为1，判断当前结果是否为丑数。（缺点：复杂度过大）
- 其它思路：最小堆模拟法，从result = 1作为起始值，每次使用result * (2, 3 ,5)得到三个值，添加到最小堆中，取最小值来更新result（缺点是：复杂度仍然不是最优）
- 高效思路：三指针法，由于所有的丑数都是由1235之间相互倍乘得到，因此可以维护三个指针，每个指针对应的元素为当前可以与(2, 3, 5)相乘的最小值，当前的丑数由这三个指针分别乘以(2, 3, 5)后的最小值得出，同时需要更新指针的位置。

**参考代码：**

```cpp
// cpp
class Solution {
public:
    // 高效解法：三指针
    int GetUglyNumber_Solution3(int index) {
        int t2 = 0, t3 = 0, t5 = 0;
        std::vector<int> result(index, 1);

        for (int i = 1; i < index; i++) {
            result[i] = min(result[t2] * 2, result[t3] * 3, result[t5] * 5);
            if (result[i] == 2 * result[t2]) t2++;
            if (result[i] == 3 * result[t3]) t3++;
            if (result[i] == 5 * result[t5]) t5++;
        }

        return result[index - 1];
    }

    // ===== 工具函数 =====
    // 定义求三个数中最小值的函数
    int min(int a, int b, int c) {
        int tmp = a < b ? a : b;
        return tmp < c ? tmp : c;
    }
};
```

```python
# python
class Solution:
    def GetUglyNumber_Solution3(self, index): 
        """
        高效解法：三指针
        """
        result = index * [1]
        t2 = t3 = t5 = 0

        for i in range(1, index):
            result[i] = min(result[t2] * 2, result[t3] * 3, result[t5] * 5)
            if result[i] == 2 * result[t2]:
                t2 += 1
            if result[i] == 3 * result[t3]:
                t3 += 1
            if result[i] == 5 * result[t5]:
                t5 += 1
        
        return result[-1]
```

### 34. 第一个只出现一次的字符

**题目描述：**

> 在一个字符串(0<=字符串长度<=10000，全部由字母组成)中找到第一个只出现一次的字符,并返回它的位置, 如果没有则返回 -1（需要区分大小写）

**解题思路：**

- 暴力解法：二重遍历即可，每个位置需要一次与其它所以字符对比
- 其它思路：借助map，记录每个字母出现的次数，同时按要求输出第一个只出现一次的字母
- 高效思路：自行利用ascii关系，建立hash表，用一个256的数组来代替stl中的map，查找输出
- 其它思路：借助stl实现

**参考代码：**

```cpp
// cpp
class Solution {
public:
    int FirstNotRepeatingChar(std::string str) {
        if (str.empty()) {
            return -1;
        }

        unsigned char hash[256] = {0};
        for (auto i : str) {
            hash[i]++;
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

```python
# python
class Solution:
    def FirstNotRepeatingChar(self, s):
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

### 35. 数组中的逆序对

**题目描述：**

> 在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组,求出这个数组中的逆序对的总数P。并将P对1000000007取模的结果输出。 即输出P%1000000007

**解题思路：**

- 常规思路：二重循环暴力枚举
- 其它思路：倒序遍历数组，建立二叉排序树，然后递归获取右子树的总节点个数，即为逆序数
- 其它思路2：倒序遍历数组，对于[0, len]的数组，扫描当前下标a时，使用二分查找，判断a位于[a+1, len]的哪个位置，根据这个位置可以获取一个以a为首的逆序数个数，然后将a插入到该位置（其它元素前移，这样能保证每次[a+1, len]都是降序的）
- 高效思路：使用归并法来实现逆序对的统计，与归并法排序很像，三个部分构成：

>递归，把当前数组分为前后两个数组，每个数组各自区分，直到每个数组仅有一个数字
>
>合并，根据前后两个数组的元素大小关系，统计逆序对。这里的具体任务是，对于两个从小到大排列的有序数组，判断存在多少个逆序对，同时将二者组合排序。以下代码中讨论了4种情况：1) 前数组已遍历完，2) 后数组已遍历完，3) 两数组都没有遍历完，且前元素小于后元素，4) 两数组都没有遍历完，且前元素大于后元素。注意，每种情况都有选择一个元素保存到tmp数组，最终需要将这个有序的tmp数组拷贝替换原始的nums数组，只有最后一种情况存在逆序数，需要累加结果。
>
>排序，将前后两个数组排序并且替换原理的数组位置

**参考代码：**

```cpp
// cpp
class Solution {
public:
    long cnt = 0;
    vector<int> tmp;
    
    // 外部接口函数
    int InversePairs(vector<int> nums) {
        if (nums.empty()) {
            return 0;
        }
        
        tmp = nums;
        mergeSort(nums, 0, nums.size() - 1);
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

### 36. 两个链表的第一个公共结点

**题目描述：**

> 输入两个链表，找出它们的第一个公共结点。（注意因为传入数据是链表，所以错误测试数据的提示是用其他方式显示的，保证传入数据是正确的）

**解题思路：**

- map法：第一次遍历使用map记录第一个链表的键值，第二次遍历第二个链表，寻找map中是否存在
- 双指针迭代法：相同长度的两个链表，第一次遍历可以直接找到公共节点；不同长度的情况，第一次遍历找到长度差，第二次以长度差进行快慢指针遍历比较，直接找到公共节点。

**参考代码：**

```cpp
// cpp
// 1. hash方式
// 时间复杂度O(n + m)，空间复杂度O(n)
class Solution {
public:
    ListNode* FindFirstCommonNode(ListNode* h1, ListNode* h2) {
        if (h1 == nullptr || h2 == nullptr) {
            return nullptr;
        }

        std::map<ListNode*, int> map;
        while (h1) {
            map[h1] = h1->val;
            h1 = h1->next;
        }

        while (h2) {
            if (map.count(h2) == 1) {
                return h2;
            }
            h2 = h2->next;
        }

        return nullptr;
    }
};
```

```python
# python
class Solution:
    def FindFirstCommonNode2(self, h1, h2):
        """
        2. 循环法，高效的迭代解法
        时间复杂度O(n + m)，空间复杂度O(1)
        """
        t1, t2 = h1, h2
        while t1 != t2:
            t1 = t1.next if t1 != None else h2
            t2 = t2.next if t2 != None else h1
        return t1
```

### 37. 数字在排序数组中出现的次数

**题目描述：**

> 统计一个数字在排序数组中出现的次数。（从小到大的有序数组，而且都是正整数）

**解题思路：**

- 常规思路：遍历数组，进行统计计数，复杂度为O(n)，缺点在于没有利用有序这一条件
- 普通二分查找：首先使用二分查找确定是否存在，当存在时返回一个任意的相等的索引，以此为基础向左右两边查找，直到两边都不相等。（这种方式实现不够简洁，但是高效）
- 高效思路：利用元素都是正整数这一特点，不使用二分查找来寻找某一元素，而去查找左边界索引，这样查找[k, k+1]区间，最终返回差即可。需要注意的细节是寻找左边界时考虑到数组末端的特殊情况。
- 其他思路，递归

**参考代码：**

```cpp
// cpp
class Solution {
public:
    int GetNumberOfK(vector<int> data ,int k) {
        if (data.empty()) {
            return 0;
        }
        
        int first = binSearch(data, k);
        int last = binSearch(data, k + 1);
        
        return last - first;
    }
    
    int binSearch(vector<int>& data, int k) {
        int l = 0;
        int h = data.size();
        
        while (l < h) {
            int m = l + (h - l) / 2;
            if (data[m] < k) {
                l = m + 1;
            } else {
                h = m;
            }
        }
        return l;
    }
};
```

```python
# python
class Solution:
    def GetNumberOfK(self, data, k):
        first = self.binarySearch(data, k)
        last = self.binarySearch(data, k + 1)
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

### 38. 二叉树的深度

**题目描述：**

> 输入一棵二叉树，求该树的深度。从根结点到叶结点依次经过的结点（含根、叶结点）形成树的一条路径，最长路径的长度为树的深度。

**解题思路：**

- 递归直接求解即可
- 或者层次遍历，BFS求最大层次，当然也可以DFS就是麻烦一些

**参考代码：**

```cpp
// cpp
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

```python
# python
class Solution:
    def TreeDepth2(self, root):
        """
        迭代法，bfs，寻找最深的层次
        """
        if root == None:
            return 0
        
        ret = 0
        last = [root]

        while last:
            curr = []
            for node in last:
                if node.left:
                    curr.append(node.left)
                if node.right:
                    curr.append(node.right)
            last = curr
            ret += 1
        
        return ret
```

### 39. 平衡二叉树

**题目描述：**

> 输入一棵二叉树，判断该二叉树是否是平衡二叉树。

**解题思路：**

- 平衡二叉树的定义就是：左右子树的高度差小于等于1，而且左右子树也是平衡二叉树
- 分析定义，只要递归判断各个结点，保证左右子树的高度差小于等于1即可
- 方法一：先序遍历，自顶向下递归调用，存在优化空间（大量的重复判断）
- 方法二：后序遍历，当不是平衡树时，提前剪枝

**参考代码：**

```cpp
// cpp
class Solution {
public:
    // 1. 个人解法，先序遍历，自顶向下递归调用，存在优化空间
    bool isBalanced_Solution1(TreeNode* root) {
        if (root == nullptr) {
            return true;
        }

        return abs(depth(root->left) - depth(root->right)) <= 1 && isBalanced_Solution1(root->left) && isBalanced_Solution1(root->right);
    }

    // 获取树的深度
    int depth(TreeNode* root) {
        if (root == nullptr) {
            return 0;
        }
        return 1 + std::max(depth(root->left), depth(root->right));
    }
};

```

```python
# python
class Solution():
    def isBalanced_Solution2(self, root):
        """
        2. 后序遍历，提前剪枝
        """
        return self.depthAndJudge(root) != -1

    def depthAndJudge(self, root):
        """
        返回当前树的高度，如果是-1，表明是非平衡二叉树
        """
        if root == None:
            return 0
        
        left = self.depthAndJudge(root.left)
        if left == -1:
            return -1
        
        right = self.depthAndJudge(root.right)
        if right == -1:
            return -1
        
        if abs(left - right) > 1:
            return -1
        
        return 1 + max(left, right)
```

### 40. 数组中只出现一次的数字

**题目描述：**

> 一个整型数组里除了两个数字之外，其他的数字都出现了两次。请写程序找出这两个只出现一次的数字。

**解题思路：**

- 常规思路：使用哈希map法，时间复杂度为O(2n)，空间复杂度为O(n)

- 高效思路，需要一些关于异或的知识：

  > 基本规则：相等异或为0，不等异或为1
  >
  > 交换规则：异或可以交换顺序
  >
  > 0运算规则：一个数异或0，结果是自身
  >
  > 数组规则：若数组内除了一个数字之外，其他的数字都出现了两次，则遍历异或则可求出该数字

- 本题的高效思路是：

  > 关键点是通过异或来寻找一个掩码mask，使得遍历整个数组，将每个元素与这个mask作用后，会出现两种不同的结果，如0/1，这样就能将原始数组，分别划分为包含待求两个目标值的数字集合。
  >
  > 后续每个集合内分别遍历异或就可以得到两个目标值。

- 掩码的选择以及求解：

  > 可以获取一个只有一位为1的掩码mask，如00100，表明a和b最右边开始第一个不同的数位的位置。（异或运算，可以看作显示a与b二进制上每位是否不同）
  >
  > 首先，依次异或，最终的结果为待求的两个数字之间的异或，diff = a^b
  >
  > 其次，处理为掩码，diff &= -diff
  >
  > 最后，利用掩码划分为两个数组，每个数组遍历异或即可分别求出两个目标值

**参考代码：**

```cpp
// cpp
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
            if ((i & diff) == 0) { // 注意运算符优先级
                *num1 ^= i;
            } else {
                *num2 ^= i;
            }
        }
    }
};
```

```python
# python
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce2(self, array):
        """
        Pythonic方式，优化版
        """
        if array == []:
            return []
        
        return [i for i in array if array.count(i) == 1]

    def FindNumsAppearOnce(self, array):
        """
        高效解法
        """
        if array == []:
            return []
        
        diff = 0
        for i in array:
            diff ^= i
        #diff &= (diff & 0xffffffff)
        diff &= -diff

        result = [0, 0]
        for i in array:
            if (i & diff) == 0: 
                result[0] ^= i
            else:
                result[1] ^= i
        return result
```

### 41. 和为S的连续正数序列

**题目描述：**

> 小明很喜欢数学,有一天他在做数学作业时,要求计算出9~16的和,他马上就写出了正确答案是100。但是他并不满足于此,他在想究竟有多少种连续的正数序列的和为100(至少包括两个数)。没多久,他就得到另一组连续正数和为100的序列:18,19,20,21,22。现在把问题交给你,你能不能也很快的找出所有和为S的连续正数序列? Good Luck!（输出所有和为S的连续正数序列。序列内按照从小至大的顺序，序列间按照开始数字从小到大的顺序）

**解题思路：**

- 常规思路：本质是等差序列求和的问题，根据能否整数进行因数分解，特别注意是对 2*sum 进行因数分解，结果为 num * midTwice，然后根据 [num, midTwice] 组合的奇偶性质，判断能否满足要求，后续利用 [num, midTwice] 来输出 [l, h] 序列。需要注意的地方有：num要从大往小遍历，这样才能保证最终输出的结果是从小到大。另一个就是需要检测一下l的大小，防止l出现小于等于0的情况，时间复杂度O(n/2)
- 高效解法：双指针解法，从最小的窗口开始划窗，使用中间变量时刻更新当前这两个指针之间的所有元素的和，然后两个指针配合移动，从而实现找到满足条件的解。找到第一个解后，需要跳出并继续寻找下一个解。（这种方式思路简单，容易编写代码，但是好像复杂度高于O(n/2)）

**参考代码：**

```cpp
// cpp
class Solution {
public:
    // 常规解法（优化版）
    // midTwice * num = sum * 2
    std::vector<std::vector<int>> FindContinuousSequence2(int sum) {
        int l = 0;
        int h = 0;
        int midTwice = 0;      // 目标序列中间值的二倍
        int num = sum / 2 + 1; // 目标序列的数量（长度）
        std::vector<std::vector<int>> result;

        while (num >= 2) {
            if ((sum * 2) % num == 0) { // 存在约数
                midTwice = (sum * 2) / num;
                if ((num + midTwice) % 2 == 1) { // 确保一奇一偶
                    l = midTwice / 2 - num / 2 + midTwice % 2;
                    h = midTwice / 2 + num / 2;
                    add_vec(result, l, h);
                }
            }
            num--;
        }
        return result;
    }

    // 双指针解法
    // 效率一般
    std::vector<std::vector<int>> FindContinuousSequence(int sum) {
        if (sum < 3) {
            return std::vector<std::vector<int>>{};
        }

        int l = 1;
        int h = 2;
        int currSum = 3;
        std::vector<std::vector<int>> result;
 

        while (h <= sum / 2 + 1) {
            currSum = (l + h) * (h - l + 1) / 2;
            if (currSum > sum) {
                l++;
            } else if (currSum < sum) {
                h++;
            } else { // 此时相等
                add_vec(result, l, h);
                l++;
            }
        }
        
        return result;
    }

    // 用于添加的函数
    void add_vec(std::vector<std::vector<int>>& vec, int& l, int& h) {
        // 注意要去除l为负数的情况
        if (l <= 0) {
            return;
        }

        std::vector<int> tmp;
        for (int i = l; i <= h; i++) {
            tmp.push_back(i);
        }
        vec.push_back(tmp);
    }
}
```

```python
# python
class Solution:
    def FindContinuousSequence2(self, tsum):
        """
        个人解法究极优化版
        num:      目标序列的数量（长度），倒序遍历保证输出正序
        midTwice: 目标序列中间值的二倍
        """
        result = []
        for num in range(tsum // 2 + 1, 1, -1):
            midTwice = (tsum * 2) // num
            if num * midTwice == tsum * 2 and (num + midTwice) % 2 == 1:
                # 存在约数，且是一奇一偶
                l = midTwice // 2 - num // 2 + midTwice % 2
                h = midTwice // 2 + num // 2
                if l > 0: # 去除l为负数的情况
                    result.append(list(range(l, h + 1)))

        return result

    def FindContinuousSequence(slef, tsum):
        """
        参考解法
        """
        if tsum < 3:
            return []

        l = 1
        h = 2
        result = []

        while l <= tsum // 2 + 1:
            currSum = (l + h) * (h - l + 1) // 2
            if currSum > tsum:
                l += 1
            elif currSum < tsum:
                h += 1
            else:
                result.append(list(range(l, h + 1))) # 此时相等
                l += 1

        return result
```

### 42. 和为S的两个数字

**题目描述：**

> 输入一个递增排序的数组和一个数字S，在数组中查找两个数，使得他们的和正好是S，如果有多对数字的和等于S，输出两个数的乘积最小的。（对应每个测试案例，输出两个数，小的先输出。）

**解题思路：**

- 常规思路：暴力枚举，时间复杂度O(n^2)
- 其它思路：hash方法，时间复杂度O(n)，空间复杂度O(n)
- 高效思路：双指针，从两端向中间查找，首先查找到满足要求的两个数即为输出结果，时间复杂度O(n)
- 其它高效思路：双指针+二分查找，每次双指针移动的时候不采用+1/-1的方式移动，而是采用二分的方式移动，时间复杂度O(logn*logn)，数据量大时高效

**参考代码：**

```cpp
// cpp
class Solution {
public:
    // 高效思路：双指针
    std::vector<int> FindNumbersWithSum(std::vector<int> array, int sum) {
        int l = 0;
        int h = array.size() - 1;
        std::vector<int> result;

        while (l < h) {
            int currSum = array[l] + array[h];
            if (currSum == sum) {
                result.push_back(array[l]);
                result.push_back(array[h]);
                break;
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

```python
# python
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        """
        高效方式：双指针
        """
        l = 0
        h = len(array) - 1
        result = []

        while l < h:
            currSum = array[l] + array[h]
            if currSum == tsum:
                result += [array[l], array[h]]
                break
            elif currSum < tsum:
                l += 1
            elif currSum > tsum:
                h -= 1

        return result
```

### 43. 左旋转字符串

**题目描述：**

> 汇编语言中有一种移位指令叫做循环左移（ROL），现在有个简单的任务，就是用字符串模拟这个指令的运算结果。对于一个给定的字符序列S，请你把其循环左移K位后的序列输出。例如，字符序列S=”abcXYZdef”,要求输出循环左移3位后的结果，即“XYZdefabc”。是不是很简单？OK，搞定它！

**解题思路：**

- 常规思路：直接借助stl实现子串切分以及拼接
- 其它思路：使用两个相同的原始字符串str拼接为tmp，然后从tmp的第n处，提取长为str.size()的字串即可
- 正常思路：自行编写字符串翻转函数，对原始字符串的两部分分别翻转，然后整体翻转即可

**参考代码：**

```cpp
// cpp
class Solution {
public:
    // 高效解法：两部分分别翻转，然后整体翻转
    std::string LeftRotateString2(std::string str, int n) {
        if (str.empty() || n == 0) {
            return str;
        }

        str_reverse(str, 0, n - 1);
        str_reverse(str, n, str.size() - 1);
        str_reverse(str, 0, str.size() - 1);
        return str;
    }

    // 工具函数，实现翻转（对称）
    void str_reverse(std::string& str, int l, int h) {
        for (; l < h; l++, h--) {
            char tmp = str[l];
            str[l] = str[h];
            str[h] = tmp;
        }
    }
};
```

```python
class Solution():
    def LeftRotateString2(self, s, n):
        """
        两两部分翻转，然后整体翻转
        """
        if s == "" or n <= 0 or n >= len(s):
            return s
        
        tmp = list(s)
        self.str_reverse(tmp, 0, n - 1)
        self.str_reverse(tmp, n, len(s) - 1)
        self.str_reverse(tmp, 0, len(s) - 1)
        return "".join(tmp)

    def str_reverse(self, s, l ,h):
        """
        对s[l:h]实现翻转
        注意s是一个列表
        """
        while l < h:
            s[l], s[h] = s[h], s[l]
            l += 1
            h -= 1
    
```

### 44. 翻转单词顺序列

**题目描述：**

> 牛客最近来了一个新员工Fish，每天早晨总是会拿着一本英文杂志，写些句子在本子上。同事Cat对Fish写的内容颇感兴趣，有一天他向Fish借来翻看，但却读不懂它的意思。例如，“student. a am I”。后来才意识到，这家伙原来把句子单词的顺序翻转了，正确的句子应该是“I am a student.”。Cat对一一的翻转这些单词顺序可不在行，你能帮助他么？

**解题思路：**

- 暴力解法：借助python-stl，实现字符串分割，翻转
- 常规解法：先翻转每个单词，然后再翻转整个字符串（优点是不需要额外的空间）
- 注意：leetcode中的题目增加了额外的要求，一是删除字符串前后的空格，二是保证相邻两个单词之间仅有一个空格

**参考代码：**

```cpp
// cpp
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

    // 工具函数：翻转字符串
    void str_reverse(std::string& str, int l, int h) {
        for (; l < h; l++, h--) {
            char tmp = str[l];
            str[l] = str[h];
            str[h] = tmp;
        }
    }
};
```

```python
# python
class Solution():
    def ReverseSentence(self, s):
        """
        字符串翻转法
        """
        if s == "":
            return s

        l = 0
        h = 0
        length = len(s)
        tmp = list(s)

        while l <= h and h <= length:
            if h == length or s[h] == " ":
                self.str_reverse(tmp, l, h - 1)
                l = h + 1
            h += 1
        self.str_reverse(tmp, 0, length - 1)

        return "".join(tmp)

    def str_reverse(self, s, l, h):
        """
        工具函数，字符串翻转
        注意s是一个列表
        """
        while l < h:
            s[l], s[h] = s[h], s[l]
            l += 1
            h -= 1
```

### 45. 扑克牌顺子

**题目描述：**

> LL今天心情特别好,因为他去买了一副扑克牌,发现里面居然有2个大王,2个小王(一副牌原本是54张^_^)...他随机从中抽出了5张牌,想测测自己的手气,看看能不能抽到顺子,如果抽到的话,他决定去买体育彩票,嘿嘿！！“红心A,黑桃3,小王,大王,方片5”,“Oh My God!”不是顺子.....LL不高兴了,他想了想,决定大\小 王可以看成任何数字,并且A看作1,J为11,Q为12,K为13。上面的5张牌就可以变成“1,2,3,4,5”(大小王分别看作2和4),“So Lucky!”。LL决定去买体育彩票啦。 现在,要求你使用这幅牌模拟上面的过程,然后告诉我们LL的运气如何， 如果牌能组成顺子就输出true，否则就输出false。为了方便起见,你可以认为大小王是0。

**解题思路：**

- 题目分析：本题抽象为输入一个vector，数量和数值大小未知，也有可能相等（需要保证是5个数，并且每个数都在0-13之间），判断能否构成顺子，其中0可以代替1-13中的任意一个数。

- 个人常规解法：

  > 1）判断元素个数是否为5，不是则返回false
>
  > 2）遍历全部元素，判断非0元素的重复性，获取最大值，非0最小值
>
  > 3）在无非0重复元素的情况下，只有当[max, min]长度小于等于5时，结果构成顺子

- 参考解法：首先进行排序，然后一次遍历，期间进行重复性判断，根据前后两个元素的差值来选择使用相应数量的癞子补全，最终检测剩余癞子的个数是否大于等于0，代码更加简化

**参考代码：**

```cpp
// cpp
#include <algorithm>
#include <map>
class Solution {
public:
    // 个人解法
    // 修复版，使用map处理重复情况
    bool IsContinuous2(std::vector<int> numbers) {
        if (numbers.size() != 5) {
            return false;
        }

        int min = 14;
        int max = 0;
        std::map<int, int> map;

        for (auto i : numbers) {
            if (i == 0) {
                continue;
            }
            if (++map[i] == 2) { // 非0重复性判断
                return false;
            }
            if (i < min) { // 更新最小值 
                min = i;
            }
            if (i > max) { // 更新最大值
                max = i;
            }
        }

        // 在无非0重复的情况下
        return max - min <= 4;
    }

    // 参考答案解法
    bool IsContinuous(std::vector<int> numbers) {
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

```python
# python
class Solution():
    def IsContinuous2(self, numbers):
        """
        个人解法修改版，pythonic
        """
        if len(numbers) != 5:
            return False

        # 去除非0重复
        for i in numbers:
            if i != 0 and numbers.count(i) > 1:
                return False 
        
        tmp_no_zero = [i for i in numbers if i != 0]
        return max(numbers) - min(tmp_no_zero) <= 4

    def IsContinuous(self, numbers):
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

### 46. 圆圈中最后剩下的数

**题目描述：**

> 每年六一儿童节,牛客都会准备一些小礼物去看望孤儿院的小朋友,今年亦是如此。HF作为牛客的资深元老,自然也准备了一些小游戏。其中,有个游戏是这样的:首先,让小朋友们围成一个大圈。然后,他随机指定一个数m,让编号为0的小朋友开始报数。每次喊到m-1的那个小朋友要出列唱首歌,然后可以在礼品箱中任意的挑选礼物,并且不再回到圈中,从他的下一个小朋友开始,继续0...m-1报数....这样下去....直到剩下最后一个小朋友,可以不用表演,并且拿到牛客名贵的“名侦探柯南”典藏版(名额有限哦!!^_^)。请你试着想下,哪个小朋友会得到这份礼品呢？(注：小朋友的编号是从0到n-1)
>
> 如果没有小朋友，请返回-1

**解题思路：**

- 常规思路：使用数组来模拟报数的过程，循环求解，时间复杂度较大

- 其它思路：使用单向循环链表来求解，每个结点存储是否被选中的标志bool sign，不断遍历该链表，根据间隔m来选中结点，直到剩下最后一个结点退出

- 高效思路：

  > 本质是一个约瑟夫环的问题，考虑编号为[0, 1, 2, ..., m-1, m, ..., n - 1]的序列，排除编号为[m - 1]后的序列为[0, 1, 2, ..., m, ..., n - 1]。将该序列看做从[m]开始的新序列为[m, ..., n - 1, 0, 1, 2, ..., m - 2]，此时可以通过公式映射为新序列[0, 1, 2, ..., m-1, m, ..., n - 2]，由此成为一个新的子问题。（注意子问题中的0映射为父问题中的m）
  >
  > s(n, m)表示长为n的序列，依次选中n-1个元素，最后一个元素为解。s(n-1, m)表示长为n-1的序列，依次选中n-2个元素，最后一个元素为解。本次选中的元素，在上一次一定未被选中，相邻两次之间的迭代关系为：s(n, m) = (s(n-1, m) + m) % n
  >
  > 这个公式的含义是，将在长度为n-1的解的索引变换到长度为n的序列中的索引。（最终长度为1时的解为0，需要借助该公式不断迭代，得到长度为n时的解）

- 高效思路1：递归，考虑最终的的递归退出条件为n=1，此时返回0

- 高效思路2：动态规划，反向迭代

**参考代码：**

```cpp
// cpp
class Solution {
public:
    // 递归法
    // s(n)表示还剩下n个元素没有选中时的解
    // 递推公式： s(n) = (s(n-1) + m) % n 
    int LastRemaining_Solution3(int n, int m) {
        if (n == 0) {
            return -1;
        }
        if (n == 1) {
            return 0;
        }
        return (LastRemaining_Solution3(n - 1, m) + m) % n;
    }

    // 动态规划，反向迭代，反向的递推公式
    int LastRemaining_Solution4(int n, int m) {
        if (n == 0) {
            return -1;
        }
        int s = 0;
        for (int i = 2; i <= n; i++) {
            s = (s + m) % i;
        }
        return s;
    }
};
```

```python
# python
class Solution:
    def LastRemaining_Solution1(self, n, m):
        """
        暴力枚举
        """
        if n <= 0 or m <= 0:
            return -1

        i = -1
        step = 0
        count = n
        sign = [False] * n

        while count > 0:
            i = (i + 1) % n
            if sign[i]:
                continue
        
            step += 1
            if step == m:
                sign[i] = True
                step = 0
                count -= 1
    
        return i 
```

### 47. 前N项正整数求和

**题目描述：**

> 求1+2+3+...+n，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。

**解题思路：**

- 根据题目，可以使用的运算符有：加法、减法、移位、逻辑运算。
- 迭代法累加：无法使用循环，因为for和while无法使用。
- 递归法累加：由于不能使用if语句，因此正常形式的递归也无法使用，但是可以借助&&的短路特性来实现递归。
- 公式法：(n+1)*n/2，需要考虑如何实现乘法，可以利用sizeof(二维数组实现)，也可以利用pow(n, 2) + n，来实现，也可以编写快速乘法函数。

**参考代码：**

```cpp
// cpp
class Solution {
public:
    // 递归解法
    // 利用&&短路特性，代替if条件判断
    int Sum_Solution1(int n) {
        int sum = n;
        bool tmp = n > 0 && (sum += Sum_Solution1(n - 1)) > 0;
        return sum;
    }

    // 无脑sizeof法
    int Sum_Solution2(int n) {
        char tmp[n][n+1];
        return sizeof(tmp) >> 1;
    }

    // 快速乘法
    int Sum_Solution4(int n) {
        return multiply(n, n + 1) >> 1;
    }

    // 自定义乘法
    int multiply(int a, int b) {
        int res = 0;
        (a&1) && (res += b);
        a >>= 1; b <<=1;
        a && (res += multiply(a, b));
        return res;
    }
};
```

```python
# python
class Solution():
    def Sum_Solution1(self, n):
        """
        递归解法
        """
        tmp = n and self.Sum_Solution1(n - 1)
        return n + tmp

    def Sum_Solution2(self, n):
        """
        利用sum函数
        """
        return sum(list(range(1, n + 1)))

    def Sum_Solution3(self, n):
        """
        利用乘方
        """
        return (n**2 + n) >> 1
```

### 48. 不用加减乘除做加法

**题目描述：**

> 写一个函数，求两个整数之和，要求在函数体内不得使用+、-、*、/四则运算符号。

**解题思路：**

- 题目分析：本质是数字电路中加法器的实现，一位加法器：a^b为本位和，(a&b) <<1为进位
- 常规思路：对每位执行一位加法，本位和与进位之间也是加法的运算，整体上可以借助递归实现
- 其它思路：也可以通过循环来实现迭代，递归终止的条件为，进位为0，直接返回本位和
- 注意：负数的强制左移，需要使用unsigned int进行类型转换，而python对负数的位运算则要麻烦

**参考代码：**

```cpp
// cpp
class Solution {
public:
    // 递归实现
    int Add(int a, int b) {
        return b == 0 ? a : Add(a ^ b, (a & b) << 1);
    }

    // 循环实现
    // 注意强制负数向左移位需要类型转换
    int Add2(int a, int b) {
        int tmp = 0;
        while (b != 0) {
            tmp = a ^ b;
            b = (unsigned int)(a & b) << 1;
            a = tmp;
        }
        return a;
    }
};
```

```python
# python
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
```

### 49. 把字符串转换成整数

**题目描述：**

> 将一个字符串转换成一个整数，要求不能使用字符串转换整数的库函数。 数值为0或者字符串不是一个合法的数值则返回0。输入一个字符串,包括数字字母符号,可以为空，如果是合法的数值表达则返回该数字，否则返回0。

**解题思路：**

- 关键点在于：特殊情况分析，考虑正负号，考虑非法数值，考虑int溢出
- 注意：leetcode对应的题目，增加了更多的限制，如数字串的首位不能为0，数字串有可能过长导致long类型溢出

**参考代码：**

```cpp
// cpp
class Solution {
public:
    // 个人答案，优化版，不使用pow函数
    int StrToInt(std::string str) {
        if (str.empty()) {
            return 0;
        }
        
        int sign = 1;
        long sum = 0;
        int maxInt = 0x7fffffff;
        int minInx = 0x80000000;

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
            sum = sum * 10 + int(str[i] - '0');
        }
        sum *= sign;

        // 考虑int溢出
        if (sum > maxInt || sum < minInx) {
            return 0;
        } else {
            return sum;
        }
    }
};
```

```python
# python
class Solution:
    def StrToInt(self, s):
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

- 常规思路：依次遍历每个元素，计算两边延伸的乘积，复杂度O(n*(n-1))
- 其他思路：外层循环遍历数组，将当前位置修改为1，内层循环遍历求数据乘积，之后再恢复修改，复杂度O(n^2)
- 高效思路：两次遍历，第一次遍历计算由左侧元素构成的乘积数组，第二次遍历在之前的基础上，叠加由右侧元素构成的乘积数组，复杂度O(2n)

**参考代码：**

```c++
// cpp
class Solution {
public:
   // 高效思路，两次遍历，区分左右侧元素构成的乘积数组
    std::vector<int> multiply(const std::vector<int>& A) {
        if (A.empty()) {
            return A;
        }
        
        int tmp = 1;
        std::vector<int> ret;
        for (auto i : A) {
            ret.push_back(tmp);
            tmp *= i;
        }
        
        tmp = 1;
        for (int i = A.size() - 1; i >= 0; i--) {
            ret[i] *= tmp;
            tmp *= A[i];
        }
        
        return ret;
    }
};
```

```python
# python
class Solution:
    def multiply(self, A):
        """
        高效思路，两次遍历，复杂度O(2n)
        """
        if A == []:
            return []
        
        tmp = 1
        result = []
        for i in A:
            result.append(tmp)
            tmp *= i
        
        tmp = 1
        for i in range(len(A) - 1, -1, -1):
            result[i] *= tmp
            tmp *= A[i]
        
        return result
```

### 52. 正则表达式匹配

**题目描述：**

> 请实现一个函数用来匹配包括'.'和'*'的正则表达式。模式中的字符'.'表示任意一个字符，而'*'表示它前面的字符可以出现任意次（包含0次）。 在本题中，匹配是指字符串的所有字符匹配整个模式。例如，字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，但是与"aa.a"和"ab*a"均不匹配

**解题思路：**

- 两种思路，一是递归，二是动态规划，关键是把各种情况讨论清楚

- 递归回溯法，其实就是把所有可能的情况全部试一遍，通过不停的剪去s和p相同的首部，直到某一个或两个都被剪空，就可以得到结论了。

  > 比较f(s, p)时，需要考虑p当前字符的下一位是否为'*'
  >
  > 对于不含有'*'的情况，比较当前字符是否匹配（包括'.'情况），并进行递归即可：f(s, p) = (s[0] == p[0]?) && f(s+1, p+1)
  >
  > 对于含有'\*'的情况，要复杂的多，此时存在两种匹配情况，一是将p的当前字符以及*作为空，二是\*将发挥作用，补上一位p的当前字符，二者比较结果相同后s跳到下一位继续比较（注意p不会跳到下一位，因为不确定\*应该补上多少位字符），此时有：
  >
  > f(s, p) = f(s, p+2) || ((s == p) && f(s+1, p))

- 可以发现本题存在递推关系，因此可以利用动态规划进行求解，注意可以自顶向下，或者自下向顶进行递推：

  > 自下向顶：dp(m, n)表示s在m右侧的序列，与p在n开始的序列，是否匹配
  >
  > 自顶向下：dp(m, n)表示s在m左侧的序列，与p在n左侧的序列，是否匹配
  >
  > 源代码仅给出了从左到右遍历的方式，后续待补充

**参考代码：**

```cpp
// cpp
// c++
class Solution {
public:
    // 递归优化版
    bool match2(char* str, char* pattern) {
        if (*pattern == '\0') {
            return *str == '\0';
        }
        
        // 此时的情况是 *pattern != '\0'
        bool first_match = false;
        if (*str != '\0' && (*pattern == '.' || *pattern == *str)) {
            first_match = true;
        }
        
        // 此时考虑 *(pattern + 1) 是否为 '*'
        if (*(pattern + 1) == '\0' || *(pattern + 1) != '*') {
            return first_match && match2(str + 1, pattern + 1);
        } else {
            return match2(str, pattern + 2) || (first_match && match2(str + 1, pattern));
        }
    }
};
```

```python
# python
class Solution:
    def match3(self, s, p):
        """
        动态规划版本
        """
        if p == "":
            return s == ""
        
        m = len(s)
        n = len(p)
        
        dp = [[False] * (n + 1) for i in range(m + 1)]
        dp[0][0] = True
        if m != 0 and (p[0] == "." or p[0] == s[0]):
            dp[1][1] = True
        if p[0] == "*":
            dp[0][1] = True
        for i in range(n):
            if p[i] == "*" and dp[0][i - 1] == True:
                dp[0][i + 1] = True

        for i in range(m):
            for j in range(1, n):
                if s[i] == p[j] or p[j] == ".":
                    dp[i + 1][j + 1] = dp[i][j]
                if p[j] == "*":
                    if s[i] != p[j - 1] and p[j - 1] != ".":
                        dp[i + 1][j + 1] = dp[i + 1][j - 1]
                    else:
                        dp[i + 1][j + 1] = (dp[i][j + 1] or dp[i + 1][j - 1])
        
        return dp[m][n]
```

### 53. 表示数值的字符串

**题目描述：**

> 请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。例如，字符串"+100","5e2","-123","3.1416"和"-1E-16"都表示数值。 但是"12e","1a3.14","1.2.3","+-5"和"12e+4.3"都不是。

**解题思路：**

- 常规思路：依次遍历，排出不满足条件的情况。

  > 第一个符号位特殊处理，然后while遍历，记录三个情况：has_value，dot_cnt，e_cnt
  >
  > 特殊情况返回false或者true，两个*或者.同时出现则false，不能在先有e的情况下出现.，后续出现+-符号位时必须在e后边

- 高效思路：对字符串以第一个e进行切分，分别判断指数和底数是否满足条件，注意特殊情况

- 注意：leetcode的版本要更为复杂，本题python存在开挂解法：try except

**参考代码：**

```cpp
// cpp
class Solution {
public:
    bool isNumeric(char* str) {
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
            } else { // 以下不会出现数值
                has_value = false;
                if (*str == '.' && e_cnt == 0) { // 注意不能在先有e的情况下出.小数点
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

```python
# python
class Solution:
    def isNumeric1(self, s):
        """
        牛客网版本，已经AC
        注意s是字符串
        """
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
```

### 54. 字符流中第一个不重复的字符

**题目描述：**

> 请实现一个函数用来找出字符流中第一个只出现一次的字符。例如，当从字符流中只读出前两个字符"go"时，第一个只出现一次的字符是"g"。当从该字符流中读出前六个字符“google"时，第一个只出现一次的字符是"l"。如果当前字符流没有存在出现一次的字符，返回#字符。

**解题思路：**

- 常规思路：使用hash来记录次数，使用string来记录顺序
- 其它思路：使用hash来记录次数，使用队列queue来记录顺序（只记录出现一次的字符的先后顺序）

**参考代码：**

```cpp
// cpp
class Solution {
public:
    // ===== 使用hash + string =====
    std::string s; // 用来记录顺序
    unsigned char hash[256] = {0};
    
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

```python
# python
class Solution:
    def __init__(self):
        self.str = ""
        self.hash = []

    def Insert(self, ch):
        if ch != None:
            self.str += ch
            self.hash[ord(ch)] += 1
    
    def FirstAppearingOnce(self):
        for ch in self.str:
            if self.hash[ord(ch)] == 1:
                return ch
        return "#"
```

### 55. 链表中环的入口结点

**题目描述：**

> 给一个链表，若其中包含环，请找出该链表的环的入口结点，否则，输出null。

**解题思路：**

- 基本思路：hash法，使用map记录已经检索过的节点，当下一个节点位于map中时，则找到了环的入口
- 双指针：快慢指针法，第一次遍历（快2慢1指针在某处相遇），第二次遍历（移动快指针到head，然后二者以速度1遍历），第二次相遇的位置就是环的入口节点。（原理为数学推导）
- 其它思路：表记法，顺序遍历，对已经遍历过节点，利用val进行标记，缺点是会改变原有数据

**参考代码：**

```cpp
// cpp
class Solution {
public:
    // 1. 哈希表解法
    // 时间复杂度O(n)，空间复杂度O(n)
    ListNode* EntryNodeOfLoop1(ListNode* head) {
        if (head == nullptr) {
            return nullptr;
        }

        std::map<ListNode*, int> map;
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

    // 2. 快慢指针解法
    // 时间复杂度 > O(n)，空间复杂度O(1)
    ListNode* EntryNodeOfLoop2(ListNode* head) {
        if (head == nullptr) {
            return nullptr;
        }

        ListNode* p = head;
        ListNode* q = head;
        
        // 第一次快慢追踪相遇
        while (p && q && q->next) {
            p = p->next;
            q = q->next->next;
            if (p == q) {
                break;
            }
        }
        // 防止特殊情况
        if (p != q) {
            return nullptr;
        }

        // 移动位置后，第二次同速追踪相遇
        p = head;
        while (p != q) {
            p = p->next;
            q = q->next;
        }
        return p;
    }
};
```

```python
# python
class Solution:
    def EntryNodeOfLoop4(self, head):
        """
        4. 标记法，利用链表存储标记
        时间复杂度O(n)，空间复杂度O(1)
        缺点是破化了原有数据
        """
        if head == None:
            return None
        
        while head:
            if head.val == 666:
                return head
            else:
                head.val = 666
                head = head.next
        
        return None
```

### 56. 删除链表中重复的结点

**题目描述：**

> 在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，重复的结点不保留，返回链表头指针。 例如，链表1->2->3->3->4->4->5 处理后为 1->2->5

**解题思路：**

- 注意本题在牛客与leetcode的区别，前者删除head链表中重复的节点，后者删除head链表中值为val的节点，显然后者要容易，而前者看似简单，其实很麻烦
- 需要考虑的几点：检测到重复后需要删除，头部也有可能重复，所以需要加一个辅助的头节点
- 单独写一个函数，用来判断当前结点的后方有多少个是重复的
- 注意python中传入参数的引用的使用，另一种思路是函数返回多个值

**参考代码：**

```cpp
// cpp
class Solution {
public:
   // 利用辅助函数，检测当前节点后续的重复次数
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
            // 检测接下来有多少个节点相同，如果不同则返回cnt，并修改tmp指针
            if (checkSame(curr->next, tmp) == 0) {
                curr = curr->next;
            } else {
                curr->next = tmp;
            }
        }
        
        return new_head->next;
    }

    // 输出一个结点，返回从这里开始有多少个重复的结点
    // next_head为不重复的下一个结点，这里注意要用引用
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
};
```

```python
# python
class Solution:
    def deleteDuplication(self, head):
        """
        第一次的方式，利用辅助函数，检测当前节点后续的重复次数
        """
        if head == None:
            return None
        
        new_head = ListNode.ListNode(0)
        new_head.next = head
        curr = new_head
        
        while curr != None:
            cnt, tmp = self.checkSame(curr.next)
            if cnt == 0:
                curr = curr.next
            else:
                curr.next = tmp
                
        return new_head.next

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

- 核心难点：如何在添加元素的时候保持有序（从有序序列中查找中位数则很简单）

- 常规思路：利用stl排序

- 其它思路：二分查找，从而实现有序插入

- 高效思路：利用大顶堆和小顶堆数据结构，实现序列有序（在数据量较大时，性能优越）

  > 大顶堆保存较小的一半元素，小顶堆保存较大的一半元素。
  >
  > 中位数由两个堆顶元素之中获得（根据总元素个数，当为奇数时返回大顶堆堆顶元素，当为偶数时返回两个堆顶元素的均值）

**参考代码：**

```cpp
// cpp
// 优先队列（堆）方法
class Solution {
private:
    std::priority_queue<int> maxQueue; // 大顶堆
    std::priority_queue<int, std::vector<int>, std::greater<int>> minQueue; // 小顶堆
public:
    void Insert(int num) {
        // 先向大顶堆插入新元素，然后将大顶堆堆顶pop-push进入小顶堆
        maxQueue.push(num);
        minQueue.push(maxQueue.top());
        maxQueue.pop();

        // 从小顶堆向大顶堆回推，保证二者size相等或者相差为1
        if (maxQueue.size() < minQueue.size()) {
            maxQueue.push(minQueue.top());
            minQueue.pop();
        }
    }

    double GetMedian() {
        if (maxQueue.size() > minQueue.size()) {
            return maxQueue.top();
        } else {
            return (maxQueue.top() + minQueue.top()) * 0.5;
        }
    }
};
```

```python
# python
# 其它方法
class Solution:
    def __init__(self):
        self.data = []
    
    def GetMedian1(self):
        """
        获取中位数
        """
        if self.data == []:
            return 0
        
        length = len(self.data)
        if length % 2 == 1:
            return self.data[length // 2]
        else:
            return (self.data[length // 2] + self.data[length // 2 - 1]) / 2

    def Insert1_sort(self, num):
        """
        方法一：stl排序
        """
        self.data.append(num)
        self.data.sort()
    
    def Insert1_find(self, num):
        """
        方法二：遍历寻找插入位置，保证插入有序
        """
        if self.data == []:
            self.data.append(num)
            return
        
        i = 0
        while i < len(self.data) and num > self.data[i]:
            i += 1
        
        self.data.insert(i, num)
    
    def Insert1_binSearch(self, num):
        """
        方法三：利用二分查找，插入有序
        """
        index = self.binarySearch(num)
        self.data.insert(index, num)
    
    def binarySearch(self, num):
        """
        二分查找左边界
        """
        if self.data == []:
            return 0
        
        l = 0
        h = len(self.data) - 1

        while l <= h:
            m = l + (h - l) // 2
            if num >= self.data[m]:
                l = m + 1
            elif num < self.data[m]:
                h = m - 1
        
        return l
```

### 64. 滑动窗口的最大值

**题目描述：**

> 给定一个数组和滑动窗口的大小，找出所有滑动窗口里数值的最大值。例如，如果输入数组{2,3,4,2,6,2,5,1}及滑动窗口的大小3，那么一共存在6个滑动窗口，他们的最大值分别为{4,4,6,6,6,5}； 针对数组{2,3,4,2,6,2,5,1}的滑动窗口有以下6个： {[2,3,4],2,6,2,5,1}， {2,[3,4,2],6,2,5,1}， {2,3,[4,2,6],2,5,1}， {2,3,4,[2,6,2],5,1}， {2,3,4,2,[6,2,5],1}， {2,3,4,2,6,[2,5,1]}。

**解题思路：**

- 常规思路：正常窗口检测，每次使用stl求最大值
- 高效思路：每次平移后，不需要全部排序求最大值，只需要两点，确定之前的最大值是否被丢弃，如果丢弃则需要更新最大值，将新来的值与当前最大值比较输出即可
- 解决思路1：使用临时变量保存上一次最大值，只有在上一次最大值被移出后才使用stl求新的最大值（效果不大）
- 解决思路2：使用最大堆实现，c++中的最大堆移动任意元素后需要重新生成最大堆，效率不高
- 解决思路3：双端队列，保存最大值、次大值等等，两端删除，前端删除过期元素，后端删除较小的元素，每次从头部取最大值（比较高效）
- 高效思路：动态规划（后续待补充）

**参考代码：**

```C++
// cpp
// 高效解法见源代码
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

```python
# python
# 高效解法见源代码

class Solution:
    def maxInWindows2(self, num, size):
        """
        优化版
        """
        if size <= 0 or size > len(num):
            return []
        
        return [max(num[i:i+size]) for i in range(len(num) - size + 1)]
    
    def maxInWindows4(self, num, size):
        """
        使用双端队列
        """
        if size <= 0 or size > len(num):
            return []
        
        ret, deq = [], []

        for i in range(len(num)):
            while deq != [] and num[i] > num[deq[-1]]:
                deq.pop(-1)
            if deq != [] and deq[0] < i - size + 1:
                deq.pop(0)
            deq.append(i)
            if i >= size - 1:
                ret.append(num[deq[0]])
        
        return ret
```



### 65. 矩阵中的路径

**题目描述：**

> 请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。路径可以从矩阵中的任意一个格子开始，每一步可以在矩阵中向左，向右，向上，向下移动一个格子。如果一条路径经过了矩阵中的某一个格子，则该路径不能再进入该格子。

**解题思路：**

- 思路：递归回溯法，DFS

  > 回溯法的基本做法是搜索，或是一种组织得井井有条的，能避免不必要搜索的穷举式搜索法。这种方法适用于解一些组合数相当大的问题。回溯法指导思想——走不通，就掉头。
  >
  > 设计过程：(1) 确定问题的解空间；(2) 确定结点的扩展规则；(3) 搜索。

- 算法流程：

  ```python
  result = []
  def backtrack(路径, 选择列表):
      if 满足结束条件:
          result.add(路径)
          return
      for 选择 in 选择列表:
          做选择
          backtrack(路径, 选择列表)
          撤销选择
  ```

- python存在其它思路：直接转换为二维列表求解（留待后续补充吧）

**参考代码：**

```cpp
// cpp
class Solution {
public:
    bool hasPath(char* matrix, int rows, int cols, char* str) {
        if (matrix == nullptr || str == nullptr || rows <= 0 || cols <= 0) {
            return false;
        }

        bool* flag = new bool[rows * cols];
        memset(flag, false, rows * cols);

        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (checkPath(matrix, str, flag, rows, cols, i, j, 0)) {
                    return true;
                }
            }
        }

        // 注意delete
        delete [] flag;
        return false;
    }

    bool checkPath(char* matrix, char* str, bool* flag, int rows, int cols, int i, int j, int k) {
        // 找到路径的判断
        if (str[k] == '\0') {
            return true;
        }

        // 各处错误判断
        int index = i * cols + j;
        if (i < 0 || i >= rows || j < 0 || j > cols || flag[index] == true || str[k] != matrix[index]) {
            return false;
        }

        // 此时：str[k] == maxtrix[index]
        flag[index] = true;
        if (checkPath(matrix, str, flag, rows, cols, i + 1, j, k + 1) ||
            checkPath(matrix, str, flag, rows, cols, i - 1, j, k + 1) ||
            checkPath(matrix, str, flag, rows, cols, i, j + 1, k + 1) ||
            checkPath(matrix, str, flag, rows, cols, i, j - 1, k + 1)) {
            return true;         // 从四个方向递归回溯，找到了路径
        } else {
            flag[index] = false; // 注意这里要恢复flag
            return false;        // 四个方向都没有找到
        }
    }
};
```

```python
# python
class Solution:
    def hasPath(self, matrix, rows, cols, path):
        """
        第一次的方式，递归回溯
        matrix: 一维字符串
        path: 一维字符串
        """
        if not matrix or not path or rows <= 0 or cols <= 0:
            return False
        
        matrix = list(matrix)        # 原来是一维字符串
        flag = [False] * rows * cols # 表示全都没有遍历过
        
        for i in range(rows):
            for j in range(cols):
                if self.checkPath(matrix, rows, cols, i, j, path, 0, flag):
                    return True
        
        return False
    
    def checkPath(self, matrix, rows, cols, i, j, path, k, flag):
        index = i * cols + j
        
        if i < 0 or i >= rows or j < 0 or j >= cols or k >= len(path) or matrix[index] != path[k] or flag[index] == True:
            return False
        
        if k == len(path) - 1:
            return True
        
        flag[index] = True
        
        if self.checkPath(matrix, rows, cols, i - 1, j, path, k + 1, flag) or \
           self.checkPath(matrix, rows, cols, i + 1, j, path, k + 1, flag) or \
           self.checkPath(matrix, rows, cols, i, j - 1, path, k + 1, flag) or \
           self.checkPath(matrix, rows, cols, i, j + 1, path, k + 1, flag):
            return True
        
        flag[index] = False
        return False
```

### 66. 机器人的运动范围

**题目描述：**

> 地上有一个m行和n列的方格。一个机器人从坐标0,0的格子开始移动，每一次只能向左，右，上，下四个方向移动一格，但是不能进入行坐标和列坐标的数位之和大抓例如，当k为18时，机器人能够进入方格（35,37），因为3+5+3+7 = 18。但是，它不能进入方格（35,38），因为3+5+3+8 = 19。请问该机器人能够达到多少个格子？

**解题思路：**

- 题目分析：注意本题并只是要求多少满足要求的方格，还要求了方格之间必须连通！
- 解题思路：递归回溯法，走过就标记，没有可走的了就回溯（注意回溯之前并不清除标记），与65题很类似，但是要简单，因为只需要检测上方和右方共两个方向即可。
- 最终可以作图看一下运动范围，结果还有规律的，见源代码。

**参考代码：**

```cpp
// cpp
class Solution {
public:
    int cnt = 0; // 最终输出结果
    bool* flag;  // 类内变量，标记数组
    
    int movingCount(int threshold, int rows, int cols) {
        if (rows < 0 || cols < 0 || threshold < 0) {
            return 0;
        }

        this->cnt = 0;
        this->flag = new bool[rows * cols];
        memset(this->flag, false, rows * cols);

        checkPath(threshold, rows, cols, 0, 0);
        return this->cnt;
    }

    void checkPath(int threshold, int rows, int cols, int i, int j) {
        // 直接返回的条件：出界，当前方格已标记，当前方格不可进入
        int index = i * cols + j;
        if (i >= rows || j >= cols || this->flag[index] || sum(i) + sum(j) > threshold) {
            return;
        }

        // 此时当前方格可以进入
        this->flag[index] = true;
        this->cnt++;

        checkPath(threshold, rows, cols, i + 1, j); // 检测上方
        checkPath(threshold, rows, cols, i, j + 1); // 检测下方
        return;
    }

    // 获取一个数的数位之和
    int sum(int a) {
        int ret = 0;
        while (a != 0) {
            ret += a % 10;
            a /= 10;
        }
        return ret;
    }
};
```

```python
# python
class Solution:
    def __init__(self):
        self.count = 0
        self.flag = []

    def movingCount(self, threshold, rows, cols):
        """
        递归回溯，优化版
        只用搜索上方和右方
        """
        if threshold < 0 or rows < 0 or cols < 0:
            return 0
        
        self.count = 0
        self.flag = [[0 for i in range(cols)] for j in range(rows)]

        self.checkPath(threshold, rows, cols, 0, 0)
        return self.count

    def checkPath(self, threshold, rows, cols, i, j):
        """
        搜索函数
        """
        index = i * cols + j
        if i >= rows or j >= cols or self.flag[i][j] or self.my_sum(i) + self.my_sum(j) > threshold:
            return
        
        self.flag[i][j] = 1
        self.count += 1

        self.checkPath(threshold, rows, cols, i + 1, j)
        self.checkPath(threshold, rows, cols, i, j + 1)
        return

    def my_sum(self, a):
        """
        求取整数a的各个数位数字的和
        另一种求和方式为：
        tmp = list(map(int, list(str(a))))
        return sum(tmp)
        """
        ret = 0
        while a != 0:
            ret += a % 10
            a //= 10
        return ret
    
```

### 67. 剪绳子

**题目描述：**

> 给你一根长度为n的绳子，请把绳子剪成整数长的m段（m、n都是整数，n>1并且m>1），每段绳子的长度记为k[0],k[1],...,k[m]。请问k[0]xk[1]x...xk[m]可能的最大乘积是多少？例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。

**解题思路：**

- 常规思路：递归法，动态规划

  > ​    递推关系为：f(n) = max(i*(n-i), i*f(n-i))
  >
  > ​    表示长为n的绳子，分出i为一段，剩下的可以继续分或者不分
  >
  > ​    注意i需要遍历1到n

- 高效思路：贪心法

  > 全部分为长度为1的线段，没有意义，乘积为1
  >
  > 分为若干段时，这几段越接近，乘积越大（均值不等式）
  >
  > 不能出现1，出现1还不如把1加到之前那个上边，乘积更大一些
  >
  > 简单推导，可以发现3的效率最高，2次之，1效率最低
  >
  > 因此贪心法就是优先分3，其次分2

**参考代码：**

```cpp
// cpp
class Solution {
public:
    // 递归法，时间复杂度O(n^2)
    int cutRope1(int n) {
        if (n <= 3) {
            return n - 1;
        }

        int ret = 0;
        for (int i = 2; i <= n / 2 + 1; i++) {
            ret = max(ret, max(i * (n - i), i * cutRope3(n - i)));
        }

        return ret;
    }

    // 动态规划
    // 时间复杂度O(n^2)，空间复杂度O(n)
    int cutRope2(int n) {
        int dp[n + 1] = {0, 1, 2};
        for (int i = 3; i <= n; i++) {
            for (int j = 2; j <= i / 2 + 1; j++) {
                dp[i] = max(dp[i], max(j * (i - j), j * dp[i - j]));
            }
        }

        return dp[n];
    }
};
```

```python
# python
class Solution:
    def cutRope3(self, n):
        """
        贪心法
        """
        if n <= 3:
            return n - 1
        cnt3 = n // 3 - 1 if n % 3 == 1 else n // 3
        cnt2 = (n - cnt3 * 3) // 2
        return 2**cnt2 * 3**cnt3
```

