class Solution {
public:
    int eraseOverlapIntervals(vector<vector<int>>& intervals) {
        if (intervals.empty()) {
            return 0;
        }

        // 使用lambda表达式进行排序
        sort(intervals.begin(), intervals.end(), [](vector<int> a, vector<int> b) {return a[1] < b[1];});

        int cnt = 0, last = 0;
        for (int curr = 1; curr < intervals.size(); curr++) {
            if (intervals[curr][0] >= intervals[last][1]) {
                last = curr;
            } else {
                cnt += 1;
            }
        }
        return cnt;
    }
};