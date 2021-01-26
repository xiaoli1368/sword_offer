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
	std::vector<std::vector<int>> vec2d(10, vec); // 初始化了一个二维vec
	
	// 排序
	// lambda表达式的使用
	std::sort(vec.begin(), vec.end()); // 一维排序，默认由小到大
	std::sort(vec.begin(), vec.end(), [](int a, int b) -> bool {return a < b;}); // 使用lambda表达式，由大到小
	std::sort(vec2d.begin(), vec2d.end(), [](std::vector<int> a, std::vector<int> b) -> bool {return a[1] < b[1];}); //二维排序，仅对第2列排序 

	// 求和
	std::accumulate(vec.begin(), vec.end(), 0); // 0表示初始sum=0

	// ===== map ==================================================
	std::map<int, int> map;

	// 判断是否存在
	map.count(5); // 不存在则返回0
	
	return 0;
}