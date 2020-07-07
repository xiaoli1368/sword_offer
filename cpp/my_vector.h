// 个人使用的一些关于vector的快捷函数

#ifndef MY_VECTOR_H
#define MY_VECTOR_H

#include <vector>
#include <stdlib.h>
#include <stdio.h>
#include <time.h>

// 创建range形式的vector
std::vector<int> vector_CreatRange(int start, int end, int step=1) {
    // 注意循环条件，包含对step三种符号形式的考虑
    std::vector<int> ret;
    for (int i = start; step * (end - i ) > 0; i += step) {
        ret.push_back(i);
    }
    return ret;
}

// 获得随机形式的vector
std::vector<int> vector_CreatRandom(int min, int max, int num) {
    std::vector<int> ret;
    if (min > max || num <= 0) {
        return ret;
    }

    srand(time(nullptr));
    while (ret.size() < num) {
        int curr = rand() % (max - min) + min;
        ret.push_back(curr);
    }

    return ret;
}

// 打印一维vec
void printf_1d_vec(std::vector<int>& vec) {
    if (vec.empty()) {
        return;
    }

    for (auto & i : vec) {
        printf("%d, ", i);
    }
    printf("\n");
}

// 打印二维vec
void printf_2d_vec(std::vector<std::vector<int>>& vec) {
    if (vec.empty()) {
        return;
    }

    for (auto & i : vec) {
        for (auto & j : i) {
            printf("%d, ", j);
        }
        printf("\n");
    }
}

#endif
