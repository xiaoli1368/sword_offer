// 用来记录cpp_stl中常见的用法

#include <map>
#include <unordered_map>
#include <vector>
#include <algorithm>
#include <numeric>

int main(int argc, char* argv[])
{
	// ===== vector ===============================================
	std::vector<int> vec(10); // 这里其实是初始化了10个0，暂时略去。
	
	// 排序
	std::sort(vec.begin(), vec.end());

	// 求和
	std::accumulate(vec.begin(), vec.end(), 0); // 0表示初始sum=0

	// ===== map ==================================================
	std::map<int, int> map;

	// 判断是否存在
	map.count(5); // 不存在则返回0
	
	return 0;
}