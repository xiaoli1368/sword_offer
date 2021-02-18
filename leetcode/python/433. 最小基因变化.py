#!/bin/bash python
"""
433. 最小基因变化

思路：
双向BFS，与127同
"""

class Solution(object):
    def minMutation(self, start, end, bank):
        """
        :type start: str
        :type end: str
        :type bank: List[str]
        :rtype: int
        与127单词接龙基本上是一道题，双端BFS
        """
        # 初始化
        step = 0
        letters = ["A", "C", "G", "T"]
        lqueue, rqueue = deque(), deque()
        lqueue.append(start)
        rqueue.append(end)
        lvisited, rvisited, wordSet = set(), set(), set(bank)
        lvisited.add(start)
        rvisited.add(end)

        # Double-BFS
        while lqueue and rqueue:
            if len(lqueue) > len(rqueue):
                lqueue, rqueue = rqueue, lqueue
                lvisited, rvisited = rvisited, lvisited
            size = len(lqueue)
            for i in range(size):
                currWord = lqueue.popleft()
                if currWord in rvisited:
                    return step
                for j in range(len(currWord)):
                    for char in letters:
                        nextWord = currWord[:j] + char + currWord[j+1:]
                        if nextWord not in lvisited and nextWord in wordSet:
                            lvisited.add(nextWord)
                            lqueue.append(nextWord)
            step += 1
        return -1