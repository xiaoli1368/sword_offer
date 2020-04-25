#include <algorithm>
class Solution {
public:
    vector<int> maxInWindows(const vector<int>& num, unsigned int size) {
        vector<int> ret;
        int length = num.size();
        
        if (size > length || size == 0) {
            return ret;
        }
        
        for (int i = 0; i <= length - size; i++) {
            ret.push_back(*std::max_element(num.begin() + i, num.begin() + i + size));
        }
        
        return ret;
    }
};
