// 用来记录cpp_stl中常见的用法

#include <map>
#include <unordered_map>
#include <vector>
#include <algorithm>
#include <numeric>
#include <cmath>

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

	// 求极值（先求迭代器，后解引用）
	int minVal = *std::min_element(vec.begin(), vec.end());
	int maxVal = *std::max_element(vec.begin(), vec.end());

	// 搜索
	int target = 10;
	std::find(vec.begin(), vec.end(), target) != vec.end(); // 不等于末尾，表示搜索到了
	// 指定区间搜索
	int l = 1, h = 5;
	auto it = vec.begin();
	std::find(it + l, it + h, target) != it + h; // 特别注意这里的末尾应该是与h有关的

	// ===== map ==================================================
	std::map<int, int> map;

	// 判断是否存在
	map.count(5); // 不存在则返回0

	// ===== 其它 =================================================
	int int_min = INT_MIN; // 最小整形
	int int_max = INT_MAX; // 最大整形
	
	return 0;
}