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

// ===== 轻微优化版 =====
class Solution {
public:
    typedef struct Point {
        int freq;
        int start;
        int len;
        Point(int f=0, int s=0, int l=0) : freq(f), start(s), len(l) {}
    } Point;

    int findShortestSubArray(vector<int>& nums) {
        unordered_map<int, Point> map;
        int max_freq = 0, min_len = nums.size();
        for (int val, i = 0; i < nums.size(); i++) {
            // 更新hash
            val = nums[i];
            if (map.count(val) == 0) {
                map[val] = Point(1, i, 1);
            } 
            map[val].freq += 1;
            map[val].len = i - map[val].start + 1;
            const auto& p = map[val];
            // 更新长度
            if (p.freq >= max_freq) {
                min_len = (p.freq > max_freq ? p.len : min(min_len, p.len));
                max_freq = p.freq;
            }
        }
        return min_len;
    }
};