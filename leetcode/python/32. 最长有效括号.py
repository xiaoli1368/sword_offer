#!/bin/bash python
"""
32. 最长有效括号

每道题需要想清楚几个问题：
1. 我是如何想到的？
2. 我是如何进行优化的？
3. 后续有哪些follow up？

思路一：
使用堆栈一次处理，然后再次遍历

思路二：
直接堆栈一次遍历，小技巧是先保存上一次没有消去的末尾
栈内保持下标，每次使用下标的差计算长度，（其中用到了上次没有消去的尾部）

思路三：
动态规划
dp[i]表示以s[i]结尾的最长有效子串长度
if dp[i] == "(": dp[i] = 0
step = dp[i - 1]
if s[i - step - 1] == ")": dp[i] = 0
if s[i - step - 1] == "(": dp[i] = 2 + step + dp[i - step - 2]
   )  (  )  )  (  (  (  )  )  )
0  0  0  2  0  0  0  0  2  4  6
"""

class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == "":
            return 0
        
        n = len(s)
        stack = []
        tmp = [0] * n
        for i in range(n):
            if s[i] == ")" and stack and s[stack[-1]] == "(":
                tmp[i] = 1
                tmp[stack[-1]] = 1
                stack.pop()
            else:
                stack.append(i)
        print(tmp)

        mmax = 0
        ssum = 0
        for i in range(n):
            if tmp[i] == 0:
                ssum = 0
            else:
                ssum += tmp[i]
            mmax = max(mmax, ssum)
        return mmax

    # ===== 错解 =====
    def longestValidParentheses(self, s: str) -> int:
        """
        )())((()))
        初始化ret, curr，表示历史最大长度，当前长度
        如果出现了(, 则push入栈
        如果出现了), 并且可以在栈内匹配，curr += 2, ret = max(ret, curr)
        如果出现了), 且无法匹配，curr = 0

        这种方式是错误的，无法解决：()((), 中间那个(起到了阻隔作用，但是检测不出来，对比
        ()()   return 4
        ()(()  return 2
        ()(()) return 6
        """
        ret, curr, stack = 0, 0, []
        for char in s:
            if char == "(":
                stack.append(char)
            elif stack and stack[-1] == "(":
                curr += 2
                ret = max(ret, curr)
                stack.pop()
            else:
                curr = 0
                stack.append(char)
        return ret

    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        只要相消就意味着出现了合法字符串，就要进行更新
        stack存储下标，stack[-1]的含义为：上一次没有消去的符号位置
        当前子串长度为：i - stack[-1]
		需要对stack增加-1前置pos
        """
        ret, stack = 0, [-1]
        for i, char in enumerate(s):
            if len(stack) >= 2 and s[stack[-1]] == "(" and char == ")":
                stack.pop()
                ret = max(ret, i - stack[-1])
            else:
                stack.append(i)
        return ret

    def longestValidParentheses(self, s: str) -> int:
        """
        动态规划
        dp[i]表示以s[i]结尾的最长有效子串长度
        if s[i] == "(":
            dp[i] = 0
        else:
            step = dp[i - 1]
            if s[i - step - 1] == ")": dp[i] = 0
            if s[i - step - 1] == "(": dp[i] = 2 + step + dp[i - step - 2]
           )  (  )  )  (  (  (  )  )  )
        0  0  0  2  0  0  0  0  2  4  6
        注意增加前导0，防止越界，同时全部初始化为0，并且有一种情况才会更新长度: 
        当前dp[i]处与last_match完成匹配，并且中间也是匹配的，中间长度为dp[i-1]
        if s[i-1] == ")" and s[i - dp[i-1] - 2] == "(":
            dp[i] = 2 + dp[i-1] + dp[i - dp[i-1] - 2]
        """
        ret, n = 0, len(s)
        dp = [0] * (n + 1)
        for i in range(2, n + 1):
            last_length = dp[i - 1]
            last_match = i - dp[i - 1] - 2
            if s[i - 1] == ")" and last_match >= 0 and s[last_match] == "(":
                dp[i] = 2 + last_length + dp[last_match]
                ret = max(ret, dp[i])
        return ret