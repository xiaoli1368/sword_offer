#!/bin/bash python
"""
手写二叉堆
"""

class myHeap(object):
	def __init__(self, desc=False):
		"""
		初始化，默认创建一个小顶堆
		"""
		self.heap = []
		self.desc = desc
	
	@property
	def size(self):
		"""
		返回当前堆的大小
		"""
		return len(self.heap)
	
	def top(self):
		"""
		返回堆顶元素
		"""
		return self.heap[0] if self.heap else None
	
	def push(self, item):
		"""
		添加元素
		1. 添加到末尾（此时只会影响一条分支上的大小关系）
		2. 把末尾元素依次上浮
		"""
		self.heap.append(item)
		self._shift_up(self.size - 1)
	
	def pop(self):
		"""
		弹出堆顶元素
		1. 记录堆顶元素的值
		2. 交换堆顶元素与末尾元素
		3. 删除数组末尾元素
		4. 新的堆顶元素向下调整
		5. 返回答案
		"""
		ret = self.heap[0]
		self._swap(0, self.size - 1)
		self.heap.pop()
		self._shift_down(0)
		return ret

	def _smaller(self, left, right):
		"""
		判断索引处的大小关系，与大小堆有关
		小顶堆，desc=False, smaller = left < right
		"""
		ret = self.heap[left] > self.heap[right]
		return ret if self.desc else not ret
	
	def _swap(self, i, j):
		"""
		交换两个索引处的元素
		"""
		self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
	
	def _shift_up(self, index):
		"""
		把当前index索引处的元素上浮
		在小顶堆中，当前元素小于父节点，上浮
		在大顶堆中，当前元素大于父节点，上浮
		并且持续上浮
		"""
		while index:
			parent = (index - 1) // 2
			if self._smaller(parent, index):
				break
			self._swap(index, parent)
			index = parent

	def _shift_down(self, index):
		"""
		把当前index索引处的元素下沉
		在小顶堆中，当前元素大于父节点，下沉
		在大顶堆中，当前元素小于父节点，下沉
		并且持续下沉
		"""
		i, n = index, self.size
		while 2 * i + 1 < n:
			smallest, l, r = i, 2 * i + 1, 2 * i + 2
			if l < n and self._smaller(l, smallest):
				smallest = l
			if r < n and self._smaller(r, smallest):
				smallest = r
			if smallest != i:
				self._swap(i, smallest)
				i = smallest
			else:
				break


if __name__ == "__main__":
	# just for test
	import random
	n = 20
	heap = myHeap(desc=False)
	vec = [random.randint(0, n * 2) for _ in range(n)]
	for i in range(n):
		heap.push(vec[i])
		if i >= n // 2:
			heap.pop()
		print("input: {:2d}, output: {}".format(vec[i], heap.heap))