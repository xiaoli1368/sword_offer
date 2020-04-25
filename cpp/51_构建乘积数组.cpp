class Solution {
public:
    // 第一次的解法
    vector<int> multiply(const vector<int>& A) {
        vector<int> ret;
        if (A.empty()) {
            return ret;
        }
        
        for (int i = 0; i < A.size(); i++) {
            int tmp = 1;
            for (int j = 0; j < A.size(); j++) {
                if (j != i) {
                    tmp *= A[j]; 
                }
            }
            ret.push_back(tmp);
        }
        
        return ret;
    }

    // 更为高效的解法
    vector<int> multiply(const vector<int>& A) {
        if (A.empty()) {
            return A;
        }
        
        int tmp = 1;
        vector<int> ret(A.size());
        for (int i = 0; i < A.size(); i++) {
            ret[i] = tmp;
            tmp *= A[i];
        }
        
        tmp = 1;
        for (int i = A.size() - 1; i >= 0; i--) {
            ret[i] *= tmp;
            tmp *= A[i];
        }
        
        return ret;
    }
};