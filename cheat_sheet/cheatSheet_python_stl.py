#!/bin/bash python
"""
记录一些常见的stl用法
"""

# ===== list ================================================

# 初始化
vec = [1, 4, 2, 6, 3]
vec2 = [[1, 3], [5, 0]]

# 初始化：第一个元素为1，后续5个元素为0
vec3 = [1] + [0] * 5

# 排序
vec.sort()
vec2.sort(key=lambda x : (x[0], -x[1]))

# 切片
vec3 = list(range(10))
vec4 = vec3[1:9:3] # [start:stop:step]

# ===== str =================================================

# 初始化
s1 = [chr(i) for i in range(ord("a"), ord("z") + 1)] # 字母列表a-z

# ===== dict ================================================

# 初始化
d1 = dict.fromkeys(range(10), 0)
d2 = dict(zip("abc", [1, 2, 3]))
d3 = dict.fromkeys(range(10), []) # 这种情况错误，所有的key指向同一个value引用了
d4 = {i : [], for i in range(10)} # 这种情况是可以的，不会出现引用

import collections
c1 = collections.Counter("asdjj")

# ===== set ================================================

# 初始化
lst1 = [1, 3, 4]
set1 = set(lst1)

# 错误的初始化方式
str1 = "abc"
set2 = set(str1) # set2: {"a", "b", "c"}
set3 = set()
set3.add(str1) # str3: {"abc"}

# ===== queue ==============================================
from collections import deque
queue = deque()
queue.append(5)
queue.popleft()

# ===== 其它 ===============================================
# 序列解包
a = 1
b = 2
a, b = b, a + b # 赋值后[a, b]分别为[2, 3]，不会影响，因为右侧先封装包，再左侧解包

# 通过缓存加速
# 使用python的一个本地库：functools，拥有一个装饰器，叫@functools.lru_cache
# 它能够缓存函数最近的N个调用，当缓存的值在特定时间内保持不变的时候这个非常好用
from functools import lru_cache
@lru_cache(maxsize=300)
def fibonacci(n):
	"""
	使用fibonacci递归函数时，会重复计算值。使用了lru_cache后，所有的重复计算只会执行一次。
	"""
	if n <= 2:
		return n
	return fibonacci(n - 1) + fibonacci(n - 2)