#!/bin/bash python
"""
个人实现的小顶堆
"""

def shift_up(vec, i):
    """
    索引为i的元素上浮到合适位置
    """
    while True:
        p = (i - 1) // 2
        if p >= 0 and vec[p] > vec[i]:
            vec[i], vec[p] = vec[p], vec[i]
            i = p
        else:
            break


def shift_down(vec, n, i):
    """
    索引为i的元素下沉到合适位置
    """
    while True:
        smallest = i
        l = 2 * i + 1
        r = 2 * i + 2
        if l < n and vec[l] < vec[smallest]:
            smallest = l
        if r < n and vec[r] < vec[smallest]:
            smallest = r
        if smallest != i:
            vec[i], vec[smallest] = vec[smallest], vec[i]
            i = smallest
        else:
            break


def heapify(vec):
    """
    原地建堆
    """
    assert vec != []
    n = len(vec)
    for i in range(n//2-1, -1, -1):
        shift_down(vec, n, i)


def heappop(vec):
    """
    弹出最小值
    """
    assert vec != []
    n = len(vec)
    vec[0], vec[n - 1] = vec[n - 1], vec[0] # 交换堆首堆尾
    shift_down(vec, n - 1, 0) # 堆首下沉到合适位置
    return vec.pop()


def heappush(vec, num):
    """
    压入新元素
    """
    vec.append(num) # 堆尾添加新元素
    shift_up(vec, len(vec) - 1) # 堆尾上浮


if __name__ == "__main__":
    vec = [5, 2, 6, 2, 0, 5, 9, 12, 3]
    print(vec)
    heapify(vec)
    print(vec)
    heappop(vec)
    print(vec)
    heappush(vec, -1)
    print(vec)