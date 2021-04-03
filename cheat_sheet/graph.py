#!/bin/bash python
"""
图的经典知识
"""

# =======================================================
# 图的遍历

def binaryTree_bfs(root):
	"""
	二叉树层序遍历
	按层保存节点并返回：list[list]
	"""
	ret, queue = [], [root]
	while queue:
		curr, size = [], len(queue)
		for _ in range(size):
			node = queue.pop(0)
			curr.append(node.val)
			if node.left:
				queue.append(node.left) 
			if node.right:
				queue.append(node.right)
		ret.append(curr[:])
	return ret

def graph_bfs(v):
	"""
	看成多叉树，并且增加防止重复的代码
	"""
	ret, queue, visited = [], [v], {v}
	while queue: # 是否继续遍历
		data, size = [], len(queue)
		for _ in range(size): # 遍历本层
			currNode = queue.pop(0)
			data.append(currNode.val)
			for nextNode in currNode.nextNode: # 遍历本层节点的所有后续节点
				if nextNode not in visited:
					queue.append(nextNode)
					visited.add(nextNode)
		ret.append(data[:])
	return ret

def binaryTree_dfs(root, ret):
	"""
	DFS先序遍历二叉树，保存结果到ret
	"""
	if root == None:
		return
	ret.append(root.val)
	binaryTree_dfs(root.left, ret)
	binaryTree_dfs(root.right, ret)
	return

def graph_dfs(v, ret):
	"""
	进行图的DFS，结果保存到ret
	注意需要添加标记的逻辑
	"""
	ret, visited = list(), set()
	def dfs_(currNode, ret, visited):
		if currNode == None or currNode in visited:
			return
		ret.append(currNode.val)
		for nextNode in currNode.nextNode:
			dfs_(nextNode, ret, visited)
	dfs_(v, ret, visited)
	return ret

# =======================================================
# 拓扑排序
# 有向无环图才具备，但也可以用来判断是否有环
# 参考题目：



# =======================================================
# 新建图
# 参考链接：https://www.runoob.com/python3/python-topological-sorting.html

from collections import defaultdict

class Graph(object):
	# 使用字典来定义有向图（不带权）
	# 本质上是邻接链表

	def __init__(self, vertices):
		"""
		初始化
		vertices表示图的顶点个数
		defaultdict接受一个type，当key不存在时返回默认type
		"""
		self.graph = defaultdict(list)
		self.V = vertices
	
	def addEdge(self, u, v, doubleDirection=False):
		"""
		添加一条从u到v的有向边
		"""
		self.graph[u].append(v)
		if doubleDirection:
			self.graph[v].append(u)
	
	def bfs(self, v):
		"""
		从顶点v开始
		获取bfs遍历结果，保存到二维list
		看成多叉树，并且增加防止重复的代码
		"""
		ret, queue, visited = [], [v], {v}
		while queue: # 是否继续遍历
			data, size = [], len(queue)
			for _ in range(size): # 遍历本层
				currNode = queue.pop(0)
				data.append(currNode)
				for nextNode in self.graph[currNode]: # 遍历本层节点的所有后续节点
					if nextNode not in visited:
						queue.append(nextNode)
						visited.add(nextNode)
			ret.append(data[:])
		return ret
	
	def dfs(self, v):
		"""
		进行图的DFS，结果保存到ret
		注意需要添加标记的逻辑
		"""
		ret, visited = list(), set()
		def dfs_(currNode, ret, visited):
			if currNode == None:
				return
			ret.append(currNode)
			visited.add(currNode)
			for nextNode in self.graph[currNode]:
				if nextNode not in visited:
					visited.add(nextNode)
					dfs_(nextNode, ret, visited)
		dfs_(v, ret, visited)
		return ret


if __name__ == "__main__":
	g = Graph(6)
	g.addEdge(5, 2, True)
	g.addEdge(5, 0, True) 
	g.addEdge(4, 0, True) 
	g.addEdge(4, 1, True) 
	g.addEdge(2, 3, True) 
	g.addEdge(3, 1, True)
	print(g.graph)
	print(g.bfs(5)) 
	print(g.dfs(5))
