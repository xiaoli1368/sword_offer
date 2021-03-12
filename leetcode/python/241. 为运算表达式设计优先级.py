#!/bin/bash python
"""
241. 为运算表达式设计优先级

思路：
递归或者动态规划
"""

class Solution(object):
    def diffWaysToCompute(self, s):
        """
        :type input: str
        :rtype: List[int]
        注意到只有三种符号，+-*
        不含除法，这是个好消息，否则还需要处理除0的问题
        如果原始的字符中含有n个运算符，则需要进行n次运算
        通过增加括号可以改变这n次运算的先后顺序，总的遍历空间为全排列：O(n!)
        DFS回溯法，对n个运算符，先从中任意挑选一个，得出结果后填充到该位置
        特别注意到要求返回的结果ret中是包括重复值的
        可以递归实现，遍历所有的运算符，然后获取左侧所有的取值，获取右侧所有的取值
        然后获取左右侧所有的组合取值，注意递归的最特殊情况就是s为纯数字字符，直接返回int(s)
        """
        ret = []
        if s == "":
            return []
        for i in range(len(s)):
            if s[i] == "+" or s[i] == "-" or s[i] == "*":
                left = self.diffWaysToCompute(s[:i])
                right = self.diffWaysToCompute(s[i+1:])
                for l in left:
                    for r in right:
                        if s[i] == "+": ret.append(l + r)
                        elif s[i] == "-": ret.append(l - r)
                        elif s[i] == "*": ret.append(l * r)
        return ret if ret != [] else [int(s)]

    # ===== 一个错误的版本 =====
    def getValue(self, a, b, sign):
        """
        进行运算
        """
        if sign == "+": return a + b
        if sign == "-": return a - b
        if sign == "*": return a * b
    
    def getList(self, d, s, l, h):
        """
        保存结果到ret
        """
        ret = []
        if l > h:
            return []
        for i in range(l, h + 1):
            if s[i] == "+" or s[i] == "-" or s[i] == "*":
                if i in d:
                    left, right = d[i][0], d[i][1]
                else:
                    left = self.getList(d, s, l, i - 1)
                    right = self.getList(d, s, i + 1, h)
                    d[i] = [left[:], right[:]]
                    print(i, d[i])
                for l in left:
                    for r in right:
                        ret.append(self.getValue(l, r, s[i]))
        return ret if ret != [] else [int(s[l:h+1])]

    def diffWaysToCompute(self, s: str) -> List[int]:
        """
        优化空间
        一是传递的str，导致出现大量的形参，可以尝试传递引用+边界
        二是递归存在大量的重复，可以尝试记忆化搜索
        记录每个符号的左右可能的取值
        ret 表示最终所有可能的取值
        tmp为字典，表示索引为i的符号左右两侧可能的取值分别为什么
        注意必须传递全部s，否则索引i会出现错位

        这种方式是有问题的：
        [2 * 3 - 4 + 5]
        在计算*两侧时，已经往右计算到了+两侧，但是注意此时+两侧对应的是[3 - 4 + 5]
        而以后在使用+两侧结果时，无法对应到 [2 * 3 - 4] + [5]
        也就是说只使用一个i索引来表示中间状态是不够的，需要使用二维dp
        """
        d = dict()
        return self.getList(d, s, 0, len(s) - 1)
	
	# ===== 以下是DP版本 ====

    def diffWaysToCompute(self, s):
        """
        :type input: str
        :rtype: List[int]
        动态规划，dp[i][j]表示区间[i:j]之前所有可能的取值，两端闭区间
        需要提取保存好所有的数字
        当i或者j有一个为运算符的时候，直接跳过
        dp[i][j] = dp[i][k] 运算符 dp[k][j]，遍历中间所有可能的运算符
        j依赖更小的k，因此从小往大遍历，同理i从大往小遍历，同时保证，i <= j
        """
        # 特殊情况
        if s == "":
            return []
        
        # 获取vec
        l, vec, d = 0, [], {"+", "-", "*"}
        for h in range(len(s) + 1):
            if h == len(s) or s[h] in d:
                vec.append(int(s[l:h]))
                l = h + 1
                if h != len(s):
                    vec.append(s[h])

        # 初始化dp 
        n = len(vec)
        dp = [[[] * n for _ in range(n)] for _ in range(n)]
        for i in range(n - 1, -1, -1):
            if vec[i] in d:
                continue
            for j in range(i, n):
                if vec[j] in d:
                    continue
                if i == j:
                    dp[i][j].append(vec[i])
                else:
                    for k in range(i + 1, j):
                        if vec[k] in d:
                            left = dp[i][k - 1]
                            right = dp[k + 1][j]
                            for l in left:
                                for r in right:
                                    if vec[k] == "+": dp[i][j].append(l + r)
                                    if vec[k] == "-": dp[i][j].append(l - r)
                                    if vec[k] == "*": dp[i][j].append(l * r)
        return dp[0][len(vec) - 1]

class Solution(object):
    def diffWaysToCompute(self, s):
        """
        :type input: str
        :rtype: List[int]
        动态规划，dp[i][j]表示区间[i:j]之前所有可能的取值，两端闭区间
        dp[i][j] = dp[i][k] 运算符 dp[k][j]，遍历中间所有可能的运算符
        将数据和符号分开的优化版本
        """
        # 特殊情况
        if s == "":
            return []
        
        # 初始化
        l, nums, signs = 0, [], []
        d = {"+": (lambda x, y : x + y),
             "-": (lambda x, y : x - y),
             "*": (lambda x, y : x * y)}
        for h in range(len(s) + 1):
            if h == len(s) or s[h] in d:
                nums.append(int(s[l:h]))
                l = h + 1
                if h != len(s):
                    signs.append(s[h])

        # 初始化dp 
        n = len(nums)
        dp = [[[] * n for _ in range(n)] for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if i == j:
                    dp[i][j].append(nums[i])
                    continue
                for k in range(i, j):
                    func, left, right = d[signs[k]], dp[i][k], dp[k + 1][j]
                    for l in left:
                        for r in right:
                            dp[i][j].append(func(l, r))
        return dp[0][n - 1]