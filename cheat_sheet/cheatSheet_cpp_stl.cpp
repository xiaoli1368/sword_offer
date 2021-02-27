// 用来记录cpp_stl中常见的用法

#include <map>
#include <set>
#include <queue>
#include <deque>
#include <unordered_map>
#include <unordered_set>
#include <vector>
#include <algorithm>
#include <numeric>
#include <cmath>
#include <iostream>

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

	// 迭代器遍历
	for (const auto & p : vec) {
		std::cout << p << std::endl;
	}

	// 拼接内部字符串
	// 要求内部单词之间以空格拼接，最后一处没有空格
	std::string tmp;
	std::vector<std::string> wordDict = {"adb", "fasdf", "fsad"};
	for (int i = 0; i < wordDict.size(); i++) {
		tmp += (i < wordDict.size() - 1 ? wordDict[i] + " " : wordDict[i]);
	}

	// ===== string ==============================================
	std::string s = "123";

	// 字符串和数字互相转换
	std::string s = std::to_string(123);
	int val = std::stoi(s);

	// 提取子串
	auto tmp = s.substr(1, 2); // 提取区间[start, start + size]

	// ===== map ==================================================
	std::map<int, int> map;

	// 判断是否存在
	map.count(5); // 不存在则返回0

	// 遍历
	for (const auto & p : map) {
		std::cout << p.first << " " << p.second << std::endl;
	}
	for (auto it = map.begin(); it != map.end(); it++) {
		std::cout << it->first << " " << it->second << std::endl;
	}
	for (auto it = map.cbegin(); it != map.cend(); it++) {
		std::cout << it->first << " " << it->second << std::endl;
	}

	// 自定义key/value
	// 注意value可以自定义为struct，但是key自定义后需要重载运算符，否则编译报错

	// ===== set =================================================
	std::set<int> set;

	// 插入
	set.insert(10);

	// 删除
	set.erase(10);

	// 弹出第一个元素
	int first = *set.begin();

	// 判断是否存在
	set.count(10); // 不存在则返回0

	// ===== queue ===============================================
	std::queue<int> queue;

	// 压入
	queue.push(10);

	// 获取并弹出头部
	int first = queue.front();
	queue.pop();

	// queue常见的几个用法：
	queue.front();
	queue.back();
	queue.push(10);
	queue.pop();
	queue.size();
	queue.empty();

	// deque常见用法：
	std::deque<int> deque;
	deque.front();
	deque.back();
	deque.push_front(10);
	deque.push_back(10);
	deque.pop_front();
	deque.pop_back();

	// ===== 其它 =================================================
	// 整数边界
	int int_min = INT_MIN; // 最小整形
	int int_max = INT_MAX; // 最大整形

	// 交换
	std::unordered_set<int> sa, sb;
	std::swap(sa, sb);

	// 二分查找
	// lower_bound, upper_bound, equal_range, binary_search
	// 在 [first, last) 区域内查找不小于 val 的元素
	// ForwardIterator lower_bound (ForwardIterator first, ForwardIterator last, const T& val);
	// 在 [first, last) 区域内查找第一个不符合 comp 规则的元素
	// ForwardIterator lower_bound (ForwardIterator first, ForwardIterator last, const T& val, Compare comp);
	std::vector<int> vec3 = {1, 3, 5, 6, 9};
	auto itr = std::lower_bound(vec3.begin(), vec3.end(), 4); // 返回迭代器，可以使用*itr

	// 退出
	return 0;
}