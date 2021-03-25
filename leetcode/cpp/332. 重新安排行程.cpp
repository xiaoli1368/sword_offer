class Solution {
public:
    vector<string> findItinerary(vector<vector<string>>& tickets) {
        vector<string> ans;
        if (tickets.empty()) {
            return ans;
        }
        unordered_map<string, multiset<string>> hash;
        for (const auto& ticket : tickets) {
            hash[ticket[0]].insert(ticket[1]);
        }
        stack<string> s;
        s.push("JFK");
        while (!s.empty()) {
            string next = s.top();
            if (hash[next].empty()) {
                ans.push_back(next);
                s.pop();
            } else {
                s.push(*hash[next].begin());
                hash[next].erase(hash[next].begin());
            }
        }
        reverse(ans.begin(), ans.end());
        return ans;
    }
};