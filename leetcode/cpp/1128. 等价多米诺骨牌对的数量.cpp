class Solution {
public:
    int numEquivDominoPairs(vector<vector<int>>& dominoes) {
        int i, j, key, cnt;
        int num[100] = {0};
        for (auto & vec : dominoes) {
            i = vec[0];
            j = vec[1];
            key = (i < j ? i*10+j : j*10+i);
            cnt += num[key];
            num[key] += 1;
        }
        return cnt;
    }

    int numEquivDominoPairs(vector<vector<int>>& dominoes) {
        int i, j, cnt;
        map<pair<int, int>, int> map;
        for (auto & vec : dominoes) {
            i = vec[0];
            j = vec[1];
            auto key = (i < j ? make_pair(i, j) : make_pair(j, i));
            cnt += map[key];
            map[key] += 1;
        }
        return cnt;
    }
};