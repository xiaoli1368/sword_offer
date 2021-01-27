class Solution {
public:
    vector<int> partitionLabels(string s) {
        if (s.empty()) {
            return vector<int>{};
        }

        unordered_map<char, int> map;
        for (int i = 0; i < s.size(); i++) {
            map[s[i]] = i;
        }

        vector<int> ret;
        int start = 0, end = 0;
        for (int i = 0; i < s.size(); i++) {
            end = max(end, map[s[i]]); // 更新最大右边界
            if (i == end) { // 到达右边界则更新
                ret.push_back(end - start + 1);
                start = i + 1;
            }
        }
        return ret;
    }
};