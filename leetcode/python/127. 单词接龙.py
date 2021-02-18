#!/bin/bash python
"""
127. 单词接龙

思路：
基本思路是BFS，但是存在很多的优化技巧
"""

class Solution:
	# ===== 朴素的单向BFS方法 =====
    def canChange(self, a, b):
        """
        判断ab是否只有一位字母不同
        """
        if len(a) != len(b):
            return False
        diff = 0
        for i in range(len(a)):
            if a[i] != b[i]:
                diff += 1
            if diff > 1:
                return False
        return True

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
        后续思路，双向bfs优化
        对两单词差一位的优化
        """
        step = 1
        queue = [beginWord]
        visited = set()
        while queue:
            size = len(queue)
            for _ in range(size):
                currWord = queue.pop(0)
                if currWord == endWord:
                    return step
                else:
                    # 添加下一层的queue
                    for nextWord in wordList:
                        if nextWord not in visited and self.canChange(currWord, nextWord):
                            visited.add(nextWord)
                            queue.append(nextWord)
            step += 1
        return 0
	
	# ===== 单向BFS优化版 =====
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
        后续思路，双向bfs优化
        对两单词差一位的优化
        """
        step = 1
        queue = deque()
        queue.append(beginWord)
        wordSet = set(wordList) # 所有待选单词
        visited = set(beginWord) # 已访问单词
        while queue:
            size = len(queue)
            for _ in range(size):
                currWord = queue.popleft()
                if currWord == endWord:
                    return step
                # 初始化下一层，将当前单词的每个字母替换为a-z，判断是否位于字典
                # 这里相当于使用了hash来进行优化
                s = list(currWord)
                for i in range(len(currWord)): # 第i个字母
                    oriChar = s[i]
                    for j in range(ord("a"), ord("z") + 1): # 替换目标
                        newChar = chr(j)
                        if newChar != oriChar:
                            s[i] = newChar
                            nextWord = "".join(s)
                            if nextWord in wordSet and nextWord not in visited:
                                visited.add(nextWord)
                                queue.append(nextWord)
                    s[i] = oriChar
            step += 1
        return 0

    # ===== 双向BFS优化版 =====
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
        后续思路，双向bfs优化
        1. 使用两个queue，两个visited，一个全局的set哈希
		2. 每次通过比较，从较小的一端开始BFS
        """
        # 初始化
        step = 1
        lqueue, rqueue = deque(), deque()
        lqueue.append(beginWord)
        rqueue.append(endWord)
        lvisited, rvisived, wordSet = set(), set(), set(wordList)
        lvisited.add(beginWord)
        rvisived.add(endWord)

        # 特殊情况
        if endWord not in wordSet:
            return 0

        while lqueue and rqueue:
            # 从遍历空间更小的一端开始
            if len(lqueue) > len(rqueue):
                lqueue, rqueue = rqueue, lqueue
                lvisited, rvisived = rvisived, lvisited
            size = len(lqueue)
            for _ in range(size):
                currWord = lqueue.popleft()
                if currWord in rvisived:
                    return step
                # 初始化下一层，将当前单词的每个字母替换为a-z，判断是否位于字典
                # 这里相当于使用了hash来进行优化
                s = list(currWord)
                for i in range(len(currWord)): # 第i个字母
                    oriChar = s[i]
                    for j in range(ord("a"), ord("z") + 1): # 替换目标
                        newChar = chr(j)
                        if newChar != oriChar:
                            s[i] = newChar
                            nextWord = "".join(s)
                            if nextWord not in lvisited and nextWord in wordSet:
                                lvisited.add(nextWord)
                                lqueue.append(nextWord)
                    s[i] = oriChar
            step += 1
        return 0