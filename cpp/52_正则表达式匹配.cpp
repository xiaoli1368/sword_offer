class Solution {
public:
    bool match(char* str, char* pattern) {
        if (*str == '\0' && *pattern == '\0') {
            return true;
        }
        if (*str != '\0' && *pattern == '\0') {
            return false;
        }
        
        // 剩下的情况是 *pattern != '\0'
        // 此时考虑 *(pattern + 1) 是否为 '*'
        
        if (*(pattern + 1) != '*') { // 后一位不是 '*'
            if (*str == *pattern || (*str != '\0' && *pattern == '.')) {
                return match(str + 1, pattern + 1);
            } else {
                return false;
            }
        } else { // 后一位是 '*'
            if (*str == *pattern || (*str != '\0' && *pattern == '.')) {
                // 注意这里，不确定 * 会重复几次，因此需要 ||
                return match(str + 1, pattern) || match(str, pattern + 2);
            } else { // * 被当作空
                return match(str, pattern + 2);
            }
        }
    }
};