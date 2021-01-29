class Solution {
public:
    // 判断是否为回文串，并且动态修改了两个指针，会影响外部
    bool check(string s, int& l, int& h) {
        while (l < h && s[l] == s[h]) {
            l += 1;
            h -= 1;
        }
        return l >= h;
    }

    // 验证回文串
    bool validPalindrome(string s) {
        int l = 0, h = s.size() - 1;
        bool ret = check(s, l, h);
        int l1 = l, l2 = l + 1, h1 = h - 1, h2 = h;
        return (ret ? true : (check(s, l1, h1) || check(s, l2, h2)));
    }
};