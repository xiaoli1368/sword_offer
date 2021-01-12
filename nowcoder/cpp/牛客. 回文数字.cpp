class Solution {
public:
    /**
     * 
     * @param x int整型 
     * @return bool布尔型
     */
    bool isPalindrome(int x) {
        // write code here
        if (x < 0) {
            return false;
        }
        
        int curr = x;
        long y = 0;
        
        while (curr > 0) {
            int right = curr % 10;
            curr = (curr - right) / 10;
            y = y * 10 + right;
        }
        return x == y;
    }
};