class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        if (numbers.empty()) {
            return vector<int>{0, 0};
        }

        int l = 0, h = numbers.size() - 1;
        while (l < h) {
            int ssum = numbers[l] + numbers[h];
            if (ssum == target) {
                return vector<int>{l + 1, h + 1};
            } else if (ssum < target) {
                l += 1;
            } else if (ssum > target) {
                h -= 1;
            }
        }
        return vector<int>{0, 0};
    }
};