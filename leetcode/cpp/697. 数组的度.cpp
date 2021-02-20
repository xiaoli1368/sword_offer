class Solution {
public:
    typedef struct Point {
        int freq;
        int left;
        int right;
        Point(int freq=0, int left=0, int right=0) : freq(freq), left(left), right(right) {}
    } Point;

    int findShortestSubArray(vector<int>& nums) {
        int maxFre = 0, minLen = 0, currLen, val;
        unordered_map<int, Point> map;
        for (int i = 0; i < nums.size(); i++) {
            // 更新hash
            val = nums[i];
            if (map.count(val) == 0) {
                map[val] = Point(1, i, i);
            } 
            map[val].freq += 1; 
            map[val].right = i;
            const auto& d = map[val];
            // 更新长度
            if (d.freq >= maxFre) {
                currLen = d.right - d.left + 1;
                minLen = (d.freq > maxFre ? currLen : min(minLen, currLen));
                maxFre = d.freq;
            }
        }
        return minLen;
    }
};