class Solution {
public:
    void dfs(const vector<vector<int>>& isConnected, vector<bool>& visited, int n, int i) {
        visited[i] = true;
        for (int j = 0; j < n; j++) {
            if (isConnected[i][j] == 1 && visited[j] == false) {
                dfs(isConnected, visited, n, j);
            }
        }
    }

    int findCircleNum(vector<vector<int>>& isConnected) {
        // 特殊情况
        if (isConnected.empty()) {
            return 0;
        }

        // 初始化
        int cnt = 0, n = isConnected.size();
        vector<bool> visited(n, false);

        // 找打入口
        for (int i = 0; i < n; i++) {
            if (visited[i] == false) {
                cnt += 1;
                dfs(isConnected, visited, n, i);
            }
        }
        return cnt;
    }

	// ===== BFS的方式 =====
    int findCircleNum(vector<vector<int>>& isConnected) {
        // 特殊情况
        if (isConnected.empty()) {
            return 0;
        }

        // 初始化
        int first, curr, cnt = 0, n = isConnected.size();
        unordered_set<int> city, visited;
        for (int i = 0; i < n; i++) {
            city.insert(i);
        }

        // BFS
        while (!city.empty()) {
            cnt += 1;
            queue<int> q;
            first = *city.begin();
            city.erase(first);
            q.push(first);
            while (!q.empty()) {
                curr = q.front();
                q.pop();
                visited.insert(curr);
                city.erase(curr);
                for (int i = 0; i < n; i++) {
                    if (isConnected[curr][i] == 1 && visited.count(i) == 0) {
                        q.push(i);
                        visited.insert(i);
                        city.erase(i);
                    }
                }
            }
        }
        return cnt;
    }
};