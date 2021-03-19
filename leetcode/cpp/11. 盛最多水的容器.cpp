class Solution {
public:
    int maxArea(vector<int>& height) {
        int ret = 0, l = 0, h = height.size() - 1;
        while (l < h) {
            ret = max(ret, min(height[l], height[h]) * (h - l));
            if (height[l] < height[h]) {
                l += 1;
            } else {
                h -= 1;
            }
        }
        return ret;
    }
};