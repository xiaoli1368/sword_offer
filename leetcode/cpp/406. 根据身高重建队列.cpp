class Solution {
public:
    vector<vector<int>> reconstructQueue(vector<vector<int>>& people) {
        if (people.empty()) {
            return vector<vector<int>>{};
        }

        sort(people.begin(), people.end(), [](vector<int>& a, vector<int>& b) -> bool {return a[0] > b[0] || (a[0] == b[0] && a[1] < b[1]);});

        vector<vector<int>> ret;
        for (auto & peo : people) {
            int height = peo[0];
            int num = peo[1];
            ret.insert(ret.begin() + num, vector<int>{height, num});
        }
        return ret;

    }
};