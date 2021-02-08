class Solution {
public:
    // 判断是否为字母
    bool judge(char c) {
        return ('a' <= c && c <= 'z') || ('A' <= c && c <= 'Z');
    }

    // 修改字母的大小写
    void change(string& s, int i) {
        int diff = 'a' - 'A';
        if ('a' <= s[i] && s[i] <= 'z') {
            s[i] -= diff;
        } else if ('A' <= s[i] && s[i] <= 'Z') {
            s[i] += diff;
        }
    }

    // dfs
    void dfs(vector<string>& ret, string& s, int i) {
        // 越界
        if (i >= s.size()) {
            ret.push_back(s);
            return;
        }
        // 数字跳过，获取字母不改跳过
        dfs(ret, s, i + 1);
        // 字母修改后进入下一层
        if (judge(s[i])) {
            change(s, i);
            dfs(ret, s, i + 1);
            change(s, i);
        }
        return;
    }

    vector<string> letterCasePermutation(string s) {
        vector<string> ret;
        if (!s.empty()) {
            dfs(ret, s, 0);
        }
        return ret;
    }
};