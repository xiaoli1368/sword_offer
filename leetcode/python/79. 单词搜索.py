#!/bin/bash python
"""
79. 单词搜索

思路：
也是标准的回溯法
"""

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        标志的回溯法，flag标记是否遍历过
        """
        # 特殊情况
        if board == [] or word == "":
            return False
        
        def dfs(board, word, flag, dires, row, col, i, j, index):
            """
            回溯法
            返回是否找到了
            """
            # 如果index已经超出了，则已经找到
            if index >= len(word):
                return True
            # 如果越界，或者已经遍历过，或者没有匹配上，则没有找到
            if i < 0 or j < 0 or i >= row or j >= col or flag[i][j] == True or board[i][j] != word[index]:
                return False
            # 没有越界，没有遍历过，已经匹配上了
            flag[i][j] = True
            for d in dires:
                x, y = i + d[0], j + d[1]
                if dfs(board, word, flag, dires, row, col, x, y, index + 1):
                    return True
            flag[i][j] = False
            return False
        
        # 初始化
        row = len(board)
        col = len(board[0])
        flag = [[False] * col for _ in range(row)]
        dires = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        # 找到入口开始遍历
        for i in range(row):
            for j in range(col):
                if dfs(board, word, flag, dires, row, col, i, j, 0):
                    return True
        return False