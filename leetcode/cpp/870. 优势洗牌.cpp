class Solution {
public:
    int binarySearch(const vector<int>& vec, int target) {
        int l = 0, h = vec.size() - 1;
        while (l < h) {
            int m = l + (h - l) / 2;
            if (vec[m] > target) {
                h = m;
            } else {
                l = m + 1;
            }
        }
        return (vec[l] > target ? l : 0);
    }

    vector<int> advantageCount(vector<int>& A, vector<int>& B) {
        vector<int> ret;
        sort(A.begin(), A.end());
        for (const int& target : B) {
            auto delIter = A.begin() + binarySearch(A, target);
            ret.push_back(*delIter);
            if (delIter != A.end()) {
                A.erase(delIter);
            } else {
                A.pop_back();
            }
        }
        return ret;
    }
};