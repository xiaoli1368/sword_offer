#include <queue>
// 图的遍历

// 应用：判断是否为连通图
// 可以看作一个聚类问题，最终是否可以聚为一类
// 共有三种方法：并查集，DFS，BFS
// 例题 leetcode 547. 省份数量

// 对遍历的介绍，参考：https://blog.csdn.net/m0_46518461/article/details/109582126

// 教材P408，BFS代码
// 广度优先搜索，reach[i]用来标记从顶点v可到达的所有顶点

// 二叉树的层序遍历
queue = [root]
while queue:
	size = len(queue)
	for _ in range(size):
		node = queue.pop(0)
		if node.left:
			queue.append(node.left) 
		if node.right:
			queue.append(node.right)
return

// 邻接矩阵版本
void bfs(int v, int reach[], int label) {
	reach[v] = label; // 标记当前节点
	std::queue<int> q; // 初始化队列
	q.push(v);
	while (!q.empty()) {
		// 从队列中
		// 从队列中删除一个标记过的顶点
		int w = q.front();
		q.pop();

		// 标记所有没有到达的邻接与顶点w的顶点
		for (int u = 1; u <= n; u++) {
			if (a[w][u] != noEdge && reach[u] == 0) {
				q.push(u);
				reach[u] = label;
			}
		}

	}
}
