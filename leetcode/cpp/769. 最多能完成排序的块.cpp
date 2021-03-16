class Solution {
public:
    int maxChunksToSorted(vector<int>& arr) {
        int cnt = 0, maxIndex = 0;
        for (int i = 0; i < arr.size(); i++) {
            if (maxIndex < arr[i]) {
                maxIndex = arr[i];
            }
            if (maxIndex == i) {
                cnt += 1;
            }
        }
        return cnt;
    }
};