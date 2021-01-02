class Solution {
public:
    bool canPlaceFlowers(vector<int>& vec, int n) {
        int cnt = 0;
        for (int i = 0; i < vec.size(); i++) {
            if (vec[i] == 0 && (i - 1 < 0 || vec[i - 1] == 0) && (i + 1 >= vec.size() || vec[i + 1] == 0)) {
                cnt += 1;
                vec[i] = 1;
                if (cnt >= n) {
                    break;
                }
            }
        }
        return cnt >= n;
    }
};