#include <stdio.h>
#include <vector>
#include <stack>

#define MIN(x, y) ((x) < (y) ? (x) : (y))
#define MAX(x, y) ((x) > (y) ? (x) : (y))

class Solution {
public:
    // 暴力法
    int trap1(std::vector<int>& height) {
        int ret = 0;
        int n = height.size();
        for (int i = 0; i < n; i++) {
            int lmax = height[i], rmax = height[i];
            for (int j = 0; j < i; j++) {
                lmax = MAX(lmax, height[j]);
            }
            for (int j = i + 1; j < n; j++) {
                rmax = MAX(rmax, height[j]);
            }
            ret += MIN(lmax, rmax) - height[i];
        }
        return ret;
    }

    // 提前存储法
    int trap2(std::vector<int>& height) {
        if (height.empty()) {
            return 0;
        }
        int ret = 0;
        int n = height.size();
        std::vector<int> rlist = {height[0]};
        std::vector<int> llist = {height[n - 1]};
        for (int i = 1; i < n; i++) {
            llist.push_back(MAX(height[i], llist.back()));
        }
        for (int i = n - 2; i >= 0; i--) {
            rlist.push_back(MAX(height[i], rlist.back()));
        }
        for (int i = 0; i < n; i++) {
            ret += MIN(llist[i], rlist[n - i - 1]) - height[i];
        }
        return ret;
    }

    // 双指针法
    int trap3(vector<int>& height) {
        if (height.empty()) {
            return 0;
        }
        int ret = 0, l = 0, r = height.size() - 1;
        int lmax = height[l], rmax = height[r];
        while (l <= r) {
            lmax = max(lmax, height[l]);
            rmax = max(rmax, height[r]);
            if (lmax < rmax) {
                ret += lmax - height[l++];
            } else {
                ret += rmax - height[r--];
            }
        }
        return ret;
    }}

    // 单调栈法
    int trap4(std::vector<int>& height) {
        int ret = 0, bottom, width, diff_height;
        std::stack<int> stack;
        for (int i = 0; i < height.size(); i++) {
            while (!stack.empty() && height[i] > height[stack.top()]) {
				bottom = height[stack.top()];
                stack.pop();
                if (!stack.empty()) {
                	width = i - stack.top() - 1;
                	diff_height = MIN(height[i], height[stack.top()]) - bottom;
                	ret += width * diff_height;
				}
            }
            stack.push(i);
        }
        return ret;
    }
};

int main(int argc, char* argv[])
{
    Solution s;
    std::vector<int> height = {0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1};
    printf("%d\n", s.trap1(height));
    printf("%d\n", s.trap2(height));
    printf("%d\n", s.trap3(height));
    printf("%d\n", s.trap4(height));
    return 0;
}