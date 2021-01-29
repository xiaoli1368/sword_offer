#include <iostream>
#include <string>
#include <vector>

#define MAX(x, y) ((x) > (y) ? (x) : (y))

using namespace std;

class Solution {
public:
	int lengthOfLongestSubstringKDistinct(string s, int k) {
		// 特殊情况
		if (s.empty() || k <= 0) {
			return 0;
		}

		// 初始化
		int n = s.size();
		int l = 0, h = 0, cnt = 0, ret = 0;
		vector<int> chars(128, 0);

		// 滑窗法
		while (h < n) {
			// 移动右指针
			while (h < n && cnt <= k) {
				if (chars[s[h]] == 0) {
					cnt++;
				}
				chars[s[h]]++;
				if (cnt <= k) { // 注意这里终止指针递增
					h += 1;
				}
			}
			// 更新结果
			ret = MAX(ret, h - l);
			// 更新左指针
			while (l < h && cnt >= k) {
				chars[s[l]]--;
				if (chars[s[l]] == 0) {
					cnt--;
				}
				l += 1;
			}
		}
		return ret;
	}
};

int main(int argc, char* argv[])
{
	Solution s;
	std::cout << s.lengthOfLongestSubstringKDistinct("eceba", 2) << std::endl;
	std::cout << s.lengthOfLongestSubstringKDistinct("aa", 1) << std::endl;
	return 0;
}