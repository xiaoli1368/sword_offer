#!/bin/bash python
"""
308. 二维区域和检索 - 可变

思路：
因为存在update函数可以任意更新一点值
因此如果继续使用二维前缀和则会比较麻烦，因此更新点[i,j]值后
则需要更新其右下角所有位置的累加和

更加高效的思路是使用多次循环累加的行前缀和
1. 在获取目前结果时，需要累加各个行的累加和
2. 在update之后，只需要更新[i,j]右侧同一行的累加和即可

参考链接：https://michael.blog.csdn.net/article/details/107417676?utm_medium=distribute.pc_relevant.none-task-blog-searchFromBaidu-8.control&dist_request_id=&depth_1-utm_source=distribute.pc_relevant.none-task-blog-searchFromBaidu-8.control
"""

