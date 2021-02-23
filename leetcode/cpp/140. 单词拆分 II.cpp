class Solution {
public:
    bool dfs(vector<string>& ret, vector<string>& path, unordered_set<int>& pos, const string& s, const vector<string>& wordDict, int i) {
        if (i >= s.size()) {
            string tmp;
            for (int i = 0; i < path.size(); i++) {
                tmp += (i < path.size() - 1 ? path[i] + " " : path[i]);
            }
            ret.push_back(tmp);
            return true;
        }
        bool found = false;
        for (const string& word : wordDict) {
            int j = i + word.size();
            if (j <= s.size() && pos.count(j) == 0 && word == s.substr(i, word.size())) {
                path.push_back(word);
                if (dfs(ret, path, pos, s, wordDict, j)) {
                    found = true;
                }
                path.pop_back();
            }
        }
        if (!found) {
            pos.insert(i);
        }
        return found;
    }

    vector<string> wordBreak(string s, vector<string>& wordDict) {
        if (s.empty() || wordDict.empty()) {
            return vector<string>{};
        }
        unordered_set<int> pos;
        vector<string> ret, path;
        dfs(ret, path, pos, s ,wordDict, 0);
        return ret;
    }
};