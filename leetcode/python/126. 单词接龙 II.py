#!/bin/bash python
"""
126. 单词接龙 II

思路：
正常BFS，期间保存映射关系，最终使用DFS回溯出路径
"""

class Solution(object):
	# ===== 朴素的单向BFS方法 =====
    def oneChange(self, s1, s2):
        """
        判断两个同长字符串，是否只有一位字符不同
        """
        ret = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                ret += 1
            if ret >= 2:
                return False
        return ret == 1
        
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        使用dict来记录path
        node : lastNode
        表示当前已经visited的节点，是由哪个节点访问到的，可以有多个父节点
        从end开始遍历到start
        """
        ret = []
        hasFound = False
        queue = [endWord]
        wordSet = set(wordList)
        visited = set(endWord)
        path = dict()
        
        # 特殊情况，目标单词不在词典内
        if endWord not in wordSet:
            return []
        wordSet.remove(endWord)
        wordSet.add(beginWord)
        
        # bfs获取path
        while queue and not hasFound:
            size = len(queue)
            wordSet = wordSet - visited
            for _ in range(size):
                currWord = queue.pop(0)
                if currWord == beginWord:
                    hasFound = True
                    break
                for lastWord in wordSet:
                    if self.oneChange(currWord, lastWord):
                        if lastWord not in visited:
                            queue.append(lastWord)
                        visited.add(lastWord)
                        if path.get(lastWord, None):
                            path[lastWord].append(currWord)
                        else:
                            path[lastWord] = [currWord]
        
        # 如果path中没有找到beginWord，则不存在这样的路径
        if not path.get(beginWord):
            return []
        
        # dfs遍历整个path
        tmp = [beginWord]
        def dfs(ret, path, tmp, endWord):
            if tmp[-1] == endWord:
                ret.append(tmp[:])
                return
            for nextWord in path[tmp[-1]]:
                tmp.append(nextWord)
                dfs(ret, path, tmp, endWord)
                tmp.pop()
        
        #print(path)
        dfs(ret, path, tmp, endWord)
        return ret
	
	# ===== 单向BFS优化版 =====
    def dfs(self, ret, path, d, endWord):
        """
        DFS回溯，得到最短路径
        从头到尾
        """
        currWord = path[-1]
        if currWord == endWord:
            ret.append(path[:])
            return
        for nextWord in d[currWord]:
            path.append(nextWord)
            self.dfs(ret, path, d, endWord)
            path.pop()
        return

    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        单向BFS，从end到start
        记录中间的路径，最后使用DFS回溯
        注意这种方式，需要区分是否为本层
		只有之前没有出现过，才入队queue
		只有之前没有出现过或者本层刚出现过，才保存映射关系（也就是本层以前没有出现过）
		注意从endWord开始，到beginWord结束，这样可以正向DFS
        """
        # 初始化
        d = dict()
        queue = deque()
        queue.append(endWord)
        visited, currLayer, wordSet = set(), set(), set(wordList)
        visited.add(endWord)
        wordSet.add(beginWord)

        # 特殊情况
        if endWord not in wordSet:
            return []

        # BFS更新 
        found = False
        while queue and not found:
            size = len(queue)
            currLayer.clear()
            for _ in range(size):
                currWord = queue.popleft()
                if currWord == beginWord:
                    found = True
                    break
                for i in range(len(currWord)):
                    for j in range(ord("a"), ord("z") + 1):
                        lastWord = currWord[:i] + chr(j) + currWord[i+1:]
                        val = lastWord in wordSet and lastWord not in visited
                        if val: # 合法则添加入队列
                            queue.append(lastWord)
                            visited.add(lastWord)
                            currLayer.add(lastWord)
                        if val or lastWord in currLayer: # 合法或出现在本层了
                            if lastWord not in d:
                                d[lastWord] = []
                            d[lastWord].append(currWord)
        
        # DFS回溯
        ret, path = [], [beginWord]
        if beginWord in d:
            self.dfs(ret, path, d, endWord)
        return ret

    # ===== 双向BFS版（错误版本） =====
    def dfs(self, ret, path, d, beginWord, endWord):
        """
        DFS回溯
        改变遍历方式，使得d可以包括其它的冗余链接
        """
        if beginWord == endWord:
            ret.append(path[:])
            return
        for nextWord in d[beginWord]:
            path.append(nextWord)
            self.dfs(ret, path, d, nextWord, endWord)
            path.pop()
        return
    
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        双向BFS
        注意使用reverse来表示记录链接的方向
        本质就是先使用BFS进行建图，这个图d包括了最短路径
        什么时候入队：只要之前没有在lvisited出现过，则入队，并且直接更新lvisited
        什么时候入图：只要之前层没有出现过，则入图，注意本层出现过也行
        """
        # 初始化
        found = reverse = False
        lqueue, rqueue = deque(), deque()
        lqueue.append(beginWord)
        rqueue.append(endWord)
        lvisited, rvisited, wordSet = set(), set(), set(wordList)
        lvisited.add(beginWord)
        rvisited.add(endWord)
        wordSet.add(beginWord)
        
        # 特殊情况
        if endWord not in wordSet:
            return []
        d = dict()
        for word in wordSet:
            d[word] = []

        # BFS更新 
		# 错误的方式会导致，结果未必就是最短的序列，最短的是Min，有可能把min+1也添加进去了
		# 如何保证添加的链接是最短的，
        # 为什么错误，这里把退出判断放在了外层，例如当前的queue内存在多个元素
        # 其中第3个在rvisited中出现，但是前两个没有出现，因此必须要对前两个元素进行遍历，才能退出
        # 问题是在对前两个元素的遍历过程中，可能就已经建立了冗余的链接
        while lqueue and rqueue and not found:
            #print(lqueue, rqueue, lvisited, rvisited)
            # 先保证小端遍历
            if len(lqueue) > len(rqueue):
                reverse = not reverse
                lqueue, rqueue = rqueue, lqueue
                lvisited, rvisited = rvisited, lvisited
            # 遍历当前层次
            size = len(lqueue)
            oriLayer = lvisited.copy()
            for _ in range(size):
                currWord = lqueue.popleft()
                if currWord in rvisited: # 在这里更新found会出问题
                    found = True
                    break
                for i in range(len(currWord)):
                    for j in range(ord("a"), ord("z") + 1):
                        nextWord = currWord[:i] + chr(j) + currWord[i+1:]
                        if nextWord != currWord and nextWord in wordSet and nextWord not in oriLayer:
                            # 加入队列的条件，当前层和本层都未出现过
                            if nextWord not in lvisited:
                                lqueue.append(nextWord)
                                lvisited.add(nextWord)
                            # 加入链接的条件，当前层没有出现过，右端没有出现过或在右端队列中
                            if nextWord not in rvisited or nextWord in rqueue:
                                if not reverse:
                                    d[currWord].append(nextWord)
                                else:
                                    d[nextWord].append(currWord)
                                #print(d)
        #print("out:")
        #print(lqueue, rqueue, lvisited, rvisited)
        #print(d)

        # DFS回溯
        ret, path = [], [beginWord]
        if beginWord in d:
            self.dfs(ret, path, d, beginWord, endWord)
        return ret

    # ===== 双向BFS（正确版本）=====
    def dfs(self, ret, path, d, beginWord, endWord):
        """
        DFS回溯
        改变遍历方式，使得d可以包括其它的冗余链接
        """
        if beginWord == endWord:
            ret.append(path[:])
            return
        for nextWord in d[beginWord]:
            path.append(nextWord)
            self.dfs(ret, path, d, nextWord, endWord)
            path.pop()
        return
    
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        双向BFS
        注意使用reverse来表示记录链接的方向
        本质就是先使用BFS进行建图，这个图d包括了最短路径
        什么时候入队：只要之前没有在lvisited出现过，则入队，并且直接更新lvisited
        什么时候入图：只要之前层没有出现过，则入图，注意本层出现过也行
		这里修改了found的更新位置
        """
        # 初始化
        found = reverse = False
        lqueue, rqueue = deque(), deque()
        lqueue.append(beginWord)
        rqueue.append(endWord)
        lvisited, rvisited, wordSet = set(), set(), set(wordList)
        lvisited.add(beginWord)
        rvisited.add(endWord)
        wordSet.add(beginWord)
        
        # 特殊情况
        if endWord not in wordSet:
            return []
        d = dict()
        for word in wordSet:
            d[word] = []

        # BFS更新 
        while lqueue and rqueue and not found:
            # 先保证小端遍历dd
            if len(lqueue) > len(rqueue):
                reverse = not reverse
                lqueue, rqueue = rqueue, lqueue
                lvisited, rvisited = rvisited, lvisited
            # 遍历当前层次
            size = len(lqueue)
            oriLayer = lvisited.copy()
            for _ in range(size):
                currWord = lqueue.popleft()
                for i in range(len(currWord)):
                    for j in range(ord("a"), ord("z") + 1):
                        nextWord = currWord[:i] + chr(j) + currWord[i+1:]
                        if nextWord != currWord and nextWord in wordSet and nextWord not in oriLayer:
                            # 入队列的条件，当前层和本层都未出现过
                            if nextWord not in lvisited:
                                lqueue.append(nextWord)
                                lvisited.add(nextWord)
                            # 添加链接
                            if not reverse:
                                d[currWord].append(nextWord)
                            else:
                                d[nextWord].append(currWord)
                            # 更新标志
                            if nextWord in rvisited and found == False:
                                found = True
		
        # DFS回溯
        ret, path = [], [beginWord]
        if beginWord in d:
            self.dfs(ret, path, d, beginWord, endWord)
        return ret

    # ===== 双向BFS究极优化版 =====
    def dfs(self, ret, path, graph, beginWord, endWord):
        """
        DFS回溯
        从graph中获取多条最短路径，保存到ret
        """
        if beginWord == endWord:
            ret.append(path[:])
            return
        for nextWord in graph[beginWord]:
            path.append(nextWord)
            self.dfs(ret, path, graph, nextWord, endWord)
            path.pop()
        return
    
    def bfs(self, beginWord, endWord, wordSet):
        """
        BFS
        遍历多条最短路径，保存到图graph中
        """
        # 初始化
        lqueue, rqueue = deque(), deque()
        lqueue.append(beginWord)
        rqueue.append(endWord)
        lvisited, rvisited = set(), set()
        lvisited.add(beginWord)
        rvisited.add(endWord)
        wordSet.add(beginWord)
        found = reverse = False
        graph = {word : [] for word in wordSet}

        # BFS更新graph哈希表
        while lqueue and rqueue and not found:
            # 保证小端遍历
            if len(lqueue) > len(rqueue):
                reverse = not reverse
                lqueue, rqueue = rqueue, lqueue
                lvisited, rvisited = rvisited, lvisited
            # 遍历当前层次，ori记录本层之前出现的元素
            size = len(lqueue)
            oriLayer = lvisited.copy()
            for _ in range(size):
                currWord = lqueue.popleft()
                for i in range(len(currWord)):
                    for j in range(ord("a"), ord("z") + 1):
                        # 获取下一层的有效单词：之前没有出现过，且位于字典内
                        nextWord = currWord[:i] + chr(j) + currWord[i+1:]
                        if nextWord in wordSet and nextWord not in oriLayer:
                            # 入队列的条件，当前层和本层都未出现过
                            if nextWord not in lvisited:
                                lqueue.append(nextWord)
                                lvisited.add(nextWord)
                            # 添加链接
                            if not reverse:
                                graph[currWord].append(nextWord)
                            else:
                                graph[nextWord].append(currWord)
                            # 更新标志
                            if nextWord in rvisited and found == False:
                                found = True
        return graph
        
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        双向BFS
        本质就是先使用BFS进行建图，这个图graph包括了最短路径
        使用reverse来表示记录链接的方向，found记录是否找到最短路径
        注意：只允许不同层直接链接，并且found在while循环前更新，否则会有冗余链接
        """
        # 特殊情况
        wordSet = set(wordList)
        wordSet.add(beginWord)
        if endWord not in wordSet:
            return []

        # BFS建图 + DFS回溯
        ret, path = [], [beginWord]
        graph = self.bfs(beginWord, endWord, wordSet)
        if beginWord in graph:
            self.dfs(ret, path, graph, beginWord, endWord)
        return ret


if __name__ == "___main__":
	"""
	以下是比较好的测试用例
	"""
	beginWord = "hit"
	endWord = "cog"
	wordList = ["hot", "hht", "hog", "dot","dog","lot","log","cog"]