#include <stdio.h>
#include <string>

class Solution {
public:
    // ===== 工具函数 =====
	// 使用栈处理字符串（这里是stl的字符串代替了栈）
	std::string getStrByStack(std::string s) {
		std::string ss;
		for (auto & i : s) {
			if (i != '#') {
				ss += i;
			} else if (!ss.empty()) {
				ss.pop_back();
			}
		}
		return ss;
	}

	// 栈法
    bool backspaceCompare(std::string s, std::string t) {
		std::string ss = getStrByStack(s);
		std::string tt = getStrByStack(t);
		return ss == tt;
	}

	// 获取字符串s在p索引之前的一个有效字符的索引
	int jump(std::string s, int p) {
		int skip = 0;
		p -= 1;
		while (p >= 0) {
			if (s[p] == '#') {
				p -= 1;
				skip += 1;
			} else if (skip > 0) {
				p -= 1;
				skip -= 1;
			} else {
				break;
			}
		}
		return p;
	}

	// 双指针法
	bool backspaceCompare2(std::string s, std::string t) {
		int p = s.size(), q = t.size();
		while (p >= 0 && q >= 0) {
			p = jump(s, p);
			q = jump(t, q);
			if (p >= 0 && q >= 0 && s[p] != t[q]) {
				return false;
			}
		}
		return p < 0 && q < 0;
	}
};

int main(int argc, char* argv[])
{
	Solution s;
	std::string s1 = "nzp#o#g";
	std::string t1 = "b#nzp#o#g";
	printf("%d\n", s.backspaceCompare(s1, t1));
	printf("%d\n", s.backspaceCompare2(s1, t1));
	return 0;
}