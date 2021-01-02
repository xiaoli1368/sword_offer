/*
cpp中优先队列用法：
#include<algorithm>    堆算法
#include<functional>   堆算法中要用的到greater函数

less<int>()
greater<int>()

make_heap(v.begin(), v.end()); // 在v上创建堆，默认大顶堆

v.push_back(new_val);
push_heap(v.begin(), v.end()); // 这样添加新元素

pop_heap(v.begin(), v.end()); // 把堆首元素交换到末尾，不需要调整了
v.pop_back(); // 这样再清除掉
*/

class Solution {
public:
    int lastStoneWeight(vector<int>& stones) {
        if (stones.empty()) {
            return 0;
        }

        make_heap(stones.begin(), stones.end(), less<int>()); // 大顶堆
        while (stones.size() > 1) {
            int y = stones[0];
            pop_heap(stones.begin(), stones.end(), less<int>());
            stones.pop_back();

            int x = stones[0];
            pop_heap(stones.begin(), stones.end(), less<int>());
            stones.pop_back();

            if (x != y) {
                stones.push_back(y - x);
                push_heap(stones.begin(), stones.end());
            }
        }

        return (stones.empty() ? 0 : stones[0]);
    }
};