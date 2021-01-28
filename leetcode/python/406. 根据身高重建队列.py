#!/bin/bash python
"""
406. 根据身高重建队列

思路：
贪心算法，先排序，然后依次每个元素进行插入

思路一：
优先对前面更高者少的人排序，然后相同前面更高者，优先对更低的人排序
1. 对第二项从小到大排序，对第一项从小到大排序
2. 对每个元素进行插入，需要对ret进行遍历，直到找到满足cnt的最靠右的位置
3. 这道题比较麻烦的地方在于，直到完全遍历数据前，都无法确定之前的每个数据的最终位置

更加高效的思路二：
1. 对第一项从大到小排序，第二项从小到大排序
2. 也就是优先处理个子更高的人，优先处理前边人更小的人，因为高个子人是看不到矮子的
3. 然后直接在每个元素前面更高的人的索引位置插入
"""

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        """
        贪心算法
        优先对前面更高者少的人排序，然后相同前面更高者，优先对更低的人排序
        1. 对第二项从小到大排序，对第一项从小到大排序
        2. 对每个元素进行插入，需要对ret进行遍历，直到找到满足cnt的最靠右的位置
        3. 这道题比较麻烦的地方在于，直到完全遍历数据前，都无法确定之前的每个数据的最终位置
        """
        if people == []:
            return []
        
        people.sort(key=lambda x : (x[1], x[0]))

        ret = []
        for height, bigCnt in people:
            # 统计当索引到i时，比height更高的人数超过bigCnt
            i = cnt = 0
            while i < len(ret) and cnt <= bigCnt:
                if ret[i][0] >= height:
                    cnt += 1
                    if cnt > bigCnt:
                        break
                i += 1
            ret.insert(i, [height, bigCnt])
        return ret

    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        先按照第二项进行排序，然后依次插入
        """
        if people == []:
            return []
        
        # 排序
        people.sort(key=lambda x : (-x[0], x[1]))

        # 插入
        ret = []
        for height, num in people:
            ret.insert(num, [height, num])
        
        # 返回结果
        return ret