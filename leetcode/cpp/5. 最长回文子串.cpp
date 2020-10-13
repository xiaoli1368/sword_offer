#include <stdio.h>
#include <string>

class Solution {
public:
    // 判断vec[l:r+1]是否为回文，左闭右开
	bool judge(std::string& s, int l, int r) {
		while (l < r) {
			if (s[l] != s[r]) {
				return false;
			}
			l += 1;
			r -= 1;
		}
		return true;
	}

	// 暴力法
	std::string longestPalidrome(std::string s) {
		int maxLen = 0, lastl = 0, lastr = 0;
		for (int l = 0; l < s.size(); l++) {
			for (int r = l + 1; r < s.size(); r++) {
				if (judge(s, l, r) && maxLen < r - l + 1) {
					maxLen = r - l + 1;
					lastl = l;
					lastr = r;
				}
			}
		}
		return s.substr(lastl, maxLen);
	}

	// 获取lr向两端延拓得最长边界，通过指针形式返回
	void getLength(std::string& s, int l, int r, int* ll, int* rr) {
		if (s[l] != s[r]) {
			*ll = r;
			*rr = l;
			return;
		}
		while (l - 1 >= 0 && r + 1 < s.size() && s[l - 1] == s[r + 1]) {
			l -= 1;
			r += 1;
		}
		*ll = l;
		*rr = r;
	}

	// 中心延拓法
	std::string longestPalidrome2(std::string s) {
		int maxLen = 0, lastl = 0, lastr = 0;
		for (int i = 0; i < 2 * s.size() - 1; i++) {
			int ll = 0, rr = 0, center = i / 2;
			if (i % 2 == 0) {
				getLength(s, center, center, &ll, &rr);
			} else {
				getLength(s, center, center + 1, &ll, &rr);
			}
			if (maxLen < rr - ll + 1) {
				maxLen = rr - ll + 1;
				lastl = ll;
				lastr = rr;
			}
		}
		return s.substr(lastl, maxLen);
	}
};

int main(int argc, char* argv[])
{
	Solution s;
	std::string ss = "babad";
	printf("%s\n", s.longestPalidrome(ss).c_str());
	printf("%s\n", s.longestPalidrome2(ss).c_str());
	return 0;
}