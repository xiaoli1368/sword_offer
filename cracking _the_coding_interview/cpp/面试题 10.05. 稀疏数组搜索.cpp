#include <vector>
#include <string>

class Solution {
public:
    int findString(std::vector<std::string>& words, std::string s) {
		int l = 0;
		int h = words.size() - 1;

		while (l <= h) {
			int m = l + (h - l) / 2;

			// 对空字符串进行特殊处理
			while (m < h && words[m] == "") {
				m++;
			}
			if (m == h && words[m] != s) {
				h = m - 1;
				continue;
			}

			if (words[m] == s) {
				return m;
			} else if (words[m] > s) {
				h = m - 1;
			} else if (words[m] < s) {
				l = m + 1;
			}
		}

		return -1;
    }
}