#include <stdio.h>
#include <string>
#include <vector>

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

	// 动态规划
	std::string longestPalidrome3(std::string s) {
		if (s.empty()) {
			return std::string();
		}

		int n = s.size();
		int maxLen = 0, l = 0, r = 0;
		std::vector<std::vector<bool>> dp(n, std::vector<bool>(n, false));

		for (int i = n - 1; i >= 0; i--) {
			for (int j = 0; j < n; j++) {
				if (i <= j && s[i] == s[j]) {
					dp[i][j] = i + 1 <= j - 1 ? dp[i + 1][j - 1] : true;
				}
				if (dp[i][j] && maxLen < j - i + 1) {
					maxLen = j - i + 1;
					l = i;
					r = j;
				}
			}
		}

		return s.substr(l, maxLen);
	}
};

int main(int argc, char* argv[])
{
	Solution s;
	std::string ss = "babadabsadfl";
	printf("%s\n", s.longestPalidrome(ss).c_str());
	printf("%s\n", s.longestPalidrome2(ss).c_str());
	printf("%s\n", s.longestPalidrome3(ss).c_str());
	return 0;
}