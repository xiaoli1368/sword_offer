class Solution {
public:
    vector<int> getArray(unordered_map<int, vector<int>>& d, int n) {
        if (d.count(n) == 0) {
            vector<int> curr, left = getArray(d, (n + 1) / 2), right = getArray(d, n / 2);
            for (const int& x : left) {
                curr.push_back(2 * x - 1);
            }
            for (const int& x : right) {
                curr.push_back(2 * x);
            }
            d[n] = curr;
        }
        return d[n];
    }

    vector<int> beautifulArray(int N) {
        unordered_map<int, vector<int>> d;
        d[1] = vector<int>(1, 1);
        return getArray(d, N);
    }
};