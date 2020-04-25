class Solution {
public:
    bool isNumeric(char* str) {
        // 参数合法性判断
        if (str == nullptr) {
            return false;
        }
        
        // 处理首位的符号位
        if (*str == '+' || *str == '-') {
            str++;
        }
        
        // 辅助参数
        int e_cnt = 0;
        int dot_cnt = 0;
        bool has_value = false;
        
        // 为了简化代码
        str--;
        while (*(++str) != '\0') {
            if (*str >= '0' && *str <= '9') {
                has_value = true;
            } else {
                // 以下不会出现数值
                has_value = false;
                if (*str == '.' && e_cnt == 0) { // 注意不能在先有e的情况下出现.
                    dot_cnt++;
                } else if (*str == 'e' || *str == 'E') {
                    e_cnt++;
                } else if ((*str == '+' || *str == '-') && (*(str - 1) == 'e' || *(str - 1) == 'E')) { // 再次出现符号位时，前一位必须为e
                    continue;
                } else {
                    return false;
                }
                
                // 合法性判断
                if (e_cnt >= 2 || dot_cnt >= 2) { // 两个e或者两个.出现时，即为false
                    return false;
                }
            }
        }
        return has_value;
    }

};
