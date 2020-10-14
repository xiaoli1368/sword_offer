#include <stdio.h>
#include <string>
#include <vector>
#include <map>
#include <algorithm>

class Solution {
public:
	// 暴力方法
	std::vector<std::string> commonChars(std::vector<std::string>& a) {
		std::vector<std::string> ret;
		std::vector<std::string> b = a;
		if (a.empty()) {
			return ret;
		} 

		for (auto & chr : b[0]) {
			bool appendFlag = true;
			for (int j = 1; j < b.size(); j++) {
				int pos = b[j].find(chr);
				if (pos == b[j].npos) {
					appendFlag = false;
					break;
				}
				b[j].erase(b[j].begin() + pos);
			}
			if (appendFlag) {
				ret.push_back(std::string(1, chr));
			}
		}
		return ret;
	}

	// 哈希方法
	// cpp果然比python麻烦好多啊
	std::vector<std::string> commonChars2(std::vector<std::string>& a) {
		std::vector<std::string> ret;
		std::map<char, std::vector<int>> map;

		for (int i = 0; i < a.size(); i++) {
			for (int j = 0; j < a[i].size(); j++) {
				char chr = a[i][j];
				if (map.count(chr) == 0) {
					map[chr] = std::vector<int>(a.size(), 0);
				}
				map[chr][i] += 1;
			}
		}
		for (auto & it : map) {
			char chr = it.first;
			int num = *min_element(it.second.begin(), it.second.end());
			std::string tmp;
			for (int i = 0; i < num; i++) {
				tmp += chr;
			}
			ret.push_back(tmp);
		}
		return ret;
	}
};

// 辅助打印函数
void my_printf(std::vector<std::string> a) {
	for (auto & str : a) {
		printf("%s", str.c_str());
	}
	printf("\n");
}

int main(int argc, char* argv[])
{
	Solution s;
	std::vector<std::string> a = {"bella", "label", "roller"};
	my_printf(s.commonChars(a));
	my_printf(s.commonChars2(a));
	return 0;
}