#!/bin/bash python
"""
用python实现图

邻接表形式，两个类：
Vertex，单个顶点，内部使用字典保存了，与当前node连接的其它node，以及边形成的weight
Graph, 记录所有的顶点，每个顶点都是Vertex类别，存在由名称到对象的映射
"""


class Vertex(object):
    # 顶点类

    def __init__(self, key):
        self.id = key
        self.connectedTo = dict()
    
    def addNeighbor(self, nbr, weight=0):
        self.connectedTo[nbr] = weight
    
    def __str__(self):
        return str(self.id) + " connectedTo: " + str([x.id for x in self.connectedTo])
    
    def getConnections(self):
        return self.connectedTo.keys()
    
    def getId(self):
        return self.id
    
    def getWeight(self, nbr):
        return self.connectedTo[nbr]


class Graph(object):
    # 图类

    def __init__(self):
        self.vertList = dict()
        self.numVertices = 0
    
    def addVertex(self, key):
        self.numVertices += 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex
    
    def getVertex(self, n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None
    
    def __contains__(self, n):
        return n in self.vertList
    
    def addEdge(self, f, t, cost=0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], cost)
    
    def getVertices(self):
        return self.vertList.keys()
    
    def __iter__(self):
        return iter(self.vertList.values())


if __name__ == "__main__":
    # 新建空图
    g = Graph()
    print(g)

    # 添加6个顶点
    for i in range(6):
        g.addVertex(i)
    print(g.vertList)

    # 添加几条边
    g.addEdge(0, 1, 5)
    g.addEdge(0, 5, 2)
    g.addEdge(1, 2, 4)
    g.addEdge(2, 3, 9)
    g.addEdge(3, 4, 7)
    g.addEdge(3, 5, 3)
    g.addEdge(4, 0, 1)
    g.addEdge(5, 4, 8)
    g.addEdge(5, 2, 1)

    # 打印所有的边以及权重
    for v1 in g:
        for v2, w in v1.connectedTo.items():
            print("from {} to {}, cost is {}".format(v1.getId(), v2.getId(), w))    







