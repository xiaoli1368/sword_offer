class Solution {
public:
    int getAbs(const int& x) {
        return x >= 0 ? x : -x;
    }

    int getGcd(int a, int b) {
        return b == 0 ? a : getGcd(b, a % b);
    }

    string getHash(const vector<int>& p1, const vector<int>& p2) {
        int A = p1[1] - p2[1], B = p2[0] - p1[0], gcd;
        if (A == 0) {
            return "0,1";
        } else if (B == 0) {
            return "1,0";
        } else if (getAbs(A) >= 1 && getAbs(B) >= 1) {
            gcd = getGcd(getAbs(A), getAbs(B));
            gcd = (A < 0 ? -gcd : gcd);
            A /= gcd;
            B /= gcd;
        }
        return to_string(A) + "," + to_string(B);
    }

    // c++中将pair<int,int>作为map的key需要重新定义比较函数
    // 可以使用map<key, map<key, index>>来嵌套表示
    // 这里直接将pair<int, int>转换为string来作为key
    int maxPoints(vector<vector<int>>& points) {
        int ret = 1, n = points.size();
        unordered_map<string, int> d;
        for (int i = 0; i < n; i++) {
            d.clear();
            for (int j = i + 1; j < n; j++) {
                string key = getHash(points[i], points[j]);
                d[key] += 1;
                ret = max(ret, 1 + d[key]);
            }
        }
        return ret;
    }
};