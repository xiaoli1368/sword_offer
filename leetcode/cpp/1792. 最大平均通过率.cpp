class Solution {
public:
    typedef pair<int, int> pairClass;

    struct cmp {
        bool operator() (const pairClass& x, const pairClass& y) {
            double xa = x.first, xb = x.second, ya = y.first, yb = y.second;
            return (xa + 1) / (xb + 1) - xa / xb < (ya + 1) / (yb + 1) - ya / yb;
        }
    };

    double maxAverageRatio(vector<vector<int>>& classes, int extraStudents) {
        double ret = 0, a, b;
        priority_queue<pairClass, vector<pairClass>, cmp> q;
        for (const auto& vec : classes) {
            ret += double(vec[0]) / vec[1];
            q.push(make_pair(vec[0], vec[1]));
        }
        for (int i = 0; i < extraStudents; i++) {
            pairClass p = q.top();
            a = p.first++, b = p.second++;
            ret += (a + 1) / (b + 1) - a / b;
            q.pop();
            q.push(p);
        }
        return ret / classes.size();
    }
};