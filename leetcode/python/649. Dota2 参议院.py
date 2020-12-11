#!/bin/bash python
"""
649. Dota2 参议院

思路：
1. 一开始我以为只要统计R和D不各自的个数即可，取多的一方，相等的时候取先手的一方
2. 后来发现根本不是这么回事，例如"RDDRDR"，最终是D获胜
3. 基本的思路是贪心，即每个候选人优先杀死那些在他右侧不同的人，然后有机会再杀死左侧不同的人
4. 暴力的方式就是，设置一个flag数组，标记每个候选人是否还存活，然后每轮依次遍历所有活着的候选人，每个候选人去杀死一个不同的人，只有当全部持相同意见的时候退出。
5. 考虑第一个人操作后，等下一轮才会操作，因此可以把他放到数组的最后方，形成循环队列，这里每次把当前已经操作过的人放到队列后方，同时把当前杀死的人从队列中剔除（这里不是严格的队列，会从队列的中间pop）
6. 为了避免上述情况，使用两个循环队列，分别存储各自的候选人位置，然后分别各自循环移位，进行判断（注意在将首元素放到末尾后，元素值应该加上len(senate)，因为这表示下一轮，否则先后顺序会错）
"""

class Solution(object):
	def predictPartyVictory(self, senate):
		"""
		:type senate: str
		:rtype: str
		"""
		if senate == []:
			return "Dire"
		
		queue = list(senate)
		while queue:
			# 移动首元素到末尾
			curr = queue.pop(0)
			queue.append(curr)
			# 行使权力，尝试找到一名反对者
			i = 0
			while i < len(queue) and queue[i] == curr:
				i += 1
			# 杀死最近的一名反对者
			if i != len(queue):
				queue.pop(i)
			else: # 如果没有反对者
				break
		return "Dire" if curr == "D" else "Radiant"
	
	def predictPartyVictory2(self, senate):
		"""
		双队列方法
		"""
		if senate == []:
			return "Dire"
		# 构造两个队列，存储下标
		qd, qr = [], []
		for i in range(len(senate)):
			if senate[i] == "D":
				qd.append(i)
			elif senate[i] == "R":
				qr.append(i)
		# 遍历判断
		while qd and qr:
			if qd[0] < qr[0]:
				qr.pop(0)
				qd.append(qd.pop(0) + len(senate))
			else:
				qd.pop(0)
				qr.append(qr.pop(0) + len(senate))
		# 返回结果
		return "Dire" if qd else "Radiant"