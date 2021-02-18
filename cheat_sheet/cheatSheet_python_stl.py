#!/bin/bash python
"""
记录一些常见的stl用法
"""

# ===== list ================================================

# 初始化
vec = [1, 4, 2, 6, 3]
vec2 = [[1, 3], [5, 0]]

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