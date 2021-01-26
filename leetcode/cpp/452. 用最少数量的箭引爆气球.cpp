class Solution {
public:
    int findMinArrowShots(vector<vector<int>>& points) {
        if (points.empty()) {
            return 0;
        }

        // 使用lambda表达式对第一列排序
        sort(points.begin(), points.end(), [](vector<int>& a, vector<int>& b) -> bool {return a[0] < b[0];});

        int cnt = 0;
        long x1 = long(INT_MIN) - 1;
        long y1 = x1;
        for (int i = 0; i < points.size(); i++) {
            long x2 = points[i][0];
            long y2 = points[i][1];
            if (x2 <= y1) {
                x1 = x2;
                y1 = (y1 < y2 ? y1 : y2);
            } else {
                cnt += 1;
                x1 = x2;
                y1 = y2;
            }
        }
        return cnt;
    }
};