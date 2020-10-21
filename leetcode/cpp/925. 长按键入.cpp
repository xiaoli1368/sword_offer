#include <stdio.h>
#include <string>

class Solution {
public:
    bool isLongPressedName(std::string name, std::string typed) {
        int p = 0;
        int q = 0;
        while (p < name.size() && q < typed.size()) {
            if (name[p] == typed[q]) {
                q += 1;
                p += 1;
                if (p > name.size() - 1) {
                    p = name.size() - 1;
                }
            } else if (p - 1 >= 0 && name[p - 1] == typed[q]) {
                q += 1;
            } else {
                return false;
            }
        }
        return p == name.size() - 1 && q == typed.size() && name[p] == typed[q - 1];
    }
};

int main(int argc, char* argv[])
{
    std::string name = "pyplrz";
    std::string typed = "ppyypllr";
    Solution s;
    printf("%d\n", s.isLongPressedName(name, typed));
    return 0;
}