class Solution
{
public:
    string s; // 用来记录顺序
    char hash[256] = {0};
    
    // Insert one char from stringstream
    void Insert(char ch) {
        s += ch;
        hash[ch]++;
    }
    
    // return the first appearence once char in current stringstream
    char FirstAppearingOnce() {
        for (auto i : s) {
            if (hash[i] == 1) {
                return i;
            }
        }
        
        return '#';
    }
};