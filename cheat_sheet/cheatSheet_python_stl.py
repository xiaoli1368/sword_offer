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

# ===== str =================================================

# 初始化
s1 = [chr(i) for i in range(ord("a"), ord("z") + 1)] # 字母列表a-z

# ===== dict ================================================

# 初始化
d1 = dict.fromkeys(range(10), 0)
d2 = dict(zip("abc", [1, 2, 3]))

import collections
c1 = collections.Counter("asdjj")
