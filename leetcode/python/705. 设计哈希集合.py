#!/bin/bash python
"""
705. 设计哈希集合

思路：
两种方法构建哈希：大数组法，不定长拉链法
参考资料：https://leetcode-cn.com/problems/design-hashset/solution/xiang-jie-hashset-de-she-ji-zai-shi-jian-4plc/
"""

class MyHashSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        超大数组法，由于 0 <= key <= 1e6
        因此确定hash数组长度为1e6
        """
        self.h = [0] * 1000001


    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        self.h[key] = 1


    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        self.h[key] = 0


    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        return self.h[key] == 1

    # ================================

class MyHashSet2:

    def __init__(self):
        """
        Initialize your data structure here.
        不定长拉链法
        """
        self.buckets = 1009
        self.tabel = [[] for _ in range(self.buckets)]
    
    def getHash(self, key):
        """
        进行hash函数操作
        """
        return key % self.buckets

    def add(self, key: int) -> None:
        """
        添加key
        """
        hashkey = self.getHash(key)
        if key in self.tabel[hashkey]:
            return
        else:
            self.tabel[hashkey].append(key)

    def remove(self, key: int) -> None:
        """
        移除key
        """
        hashkey = self.getHash(key)
        if key in self.tabel[hashkey]:
            self.tabel[hashkey].remove(key)
        return

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        hashkey = self.getHash(key)
        return key in self.tabel[hashkey]