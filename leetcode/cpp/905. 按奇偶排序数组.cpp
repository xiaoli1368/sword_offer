class Solution {
public:
    vector<int> sortArrayByParity(vector<int>& a) {
        if (a.empty()) {
            return a;
        }

        int even = 0;
        int odd = a.size() - 1;
        while (even < odd) {
            // 找到指向奇数的even指针
            while (even < odd && a[even] % 2 == 0) {
                even += 1;
            }
            // 找到指向偶数的odd指针
            while (even < odd && a[odd] % 2 == 1) {
                odd -= 1;
            }
            // 如果不越界，则进行交换
            if (even < odd) {
                int tmp = a[even];
                a[even] = a[odd];
                a[odd] = tmp;
            }
        }

        return a;
    }
};