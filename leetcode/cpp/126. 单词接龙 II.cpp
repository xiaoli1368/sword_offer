class Solution {
public:
	// ===== 朴素的单向BFS方法 =====

    // 判断两字符串是否最多只有一个字母不同
    bool canChange(string a, string b) {
        if (a.size() != b.size()) {
            return false;
        }
        int cnt = 0;
        for (int i = 0; i < a.size(); i++) {
            if (a[i] != b[i]) {
                cnt += 1;
                if (cnt > 1) {
                    return false;
                }
            }
        }
        return true;
    }

    // 进行DFS
    void dfs(vector<vector<string>>& ret, vector<string>& path, unordered_map<string, vector<string>>& d, const string& endWord) {
        string currWord = path.back();
        if (currWord == endWord) {
            ret.push_back(path);
            return;
        }
        for (const auto & nextWord : d[currWord]) {
            path.push_back(nextWord);
            dfs(ret, path, d, endWord);
            path.pop_back();
        }
        return;
    }

    vector<vector<string>> findLadders(string beginWord, string endWord, vector<string>& wordList) {
        // 初始化
        bool found = false;
        queue<string> queue;
        queue.push(endWord);
        unordered_set<string> visited, tmpSet, wordSet(wordList.begin(), wordList.end());
        visited.insert(endWord);
        wordSet.insert(beginWord);
        unordered_map<string, vector<string>> d;
        vector<vector<string>> ret;

        // 特殊情况
        if (wordSet.count(endWord) == 0) {
            return ret;
        }

        // 进行BFS
        while (!queue.empty()) {
            tmpSet = wordSet;
            int size = queue.size();
            for (int i = 0; i < size; i++) {
                string currWord = queue.front();
                queue.pop();
                if (currWord == beginWord) {
                    found = true;
                    break;
                }
                // 这种遍历方式，保证了不会出现前几层的元素
                for (const auto & lastWord : tmpSet) {
                    // 能够变化，则直接保存映射关系
                    if (canChange(currWord, lastWord)) {
                        d[lastWord].push_back(currWord);
                        // 之前没有出现过，则入队
                        if (visited.count(lastWord) == 0) {
                            queue.push(lastWord);
                            wordSet.erase(lastWord);
                            visited.insert(lastWord);
                        }
                    }
                }
            }
        }

        // 进行DFS
        if (d.count(beginWord) > 0) {
            vector<string> path = {beginWord};
            dfs(ret, path, d, endWord);
        }
        return ret;
    }

	// ===== 单向BFS优化版（注意DFS没有变化，因此略去） =====
	vector<vector<string>> findLadders(string beginWord, string endWord, vector<string>& wordList) {
        // 初始化
        bool found = false;
        queue<string> queue;
        queue.push(endWord);
        unordered_set<string> visited, currLayer, wordSet(wordList.begin(), wordList.end());
        visited.insert(endWord);
        wordSet.insert(beginWord);
        unordered_map<string, vector<string>> d;
        vector<vector<string>> ret;

        // 特殊情况
        if (wordSet.count(endWord) == 0) {
            return ret;
        }

        // 进行BFS
        while (!queue.empty()) {
            currLayer.clear();
            int size = queue.size();
            for (int i = 0; i < size; i++) {
                string currWord = queue.front();
                queue.pop();
                if (currWord == beginWord) {
                    found = true;
                    break;
                }
                // 改用生成的方式，注意要判断是否为本层出现的元素
                for (int j = 0; j < currWord.size(); j++) {
                    string lastWord = currWord;
                    for (char newChar = 'a'; newChar <= 'z'; newChar++) {
                        lastWord[j] = newChar;
                        bool inDict = (wordSet.count(lastWord) > 0);
                        bool notVisited = (visited.count(lastWord) == 0);
                        bool inCurrLayer = (currLayer.count(lastWord) > 0);
                        if (inDict && notVisited) {
                            queue.push(lastWord);
                            visited.insert(lastWord);
                            currLayer.insert(lastWord);
                        }
                        if ((inDict && notVisited) || inCurrLayer) {
                            d[lastWord].push_back(currWord);
                        }
                    }
                }
            }
        }

        // 进行DFS
        if (d.count(beginWord) > 0) {
            vector<string> path = {beginWord};
            dfs(ret, path, d, endWord);
        }
        return ret;
    }

	// ===== 双向BFS最终版（已经AC）=============================
    // 进行DFS，改变遍历方式，使得d
    void dfs(vector<vector<string>>& ret, vector<string>& path, unordered_map<string, vector<string>>& d, const string& beginWord, const string& endWord) {
        if (beginWord == endWord) {
            ret.push_back(path);
            return;
        }
        for (const auto & nextWord : d[beginWord]) {
            path.push_back(nextWord);
            dfs(ret, path, d, nextWord, endWord);
            path.pop_back();
        }
        return;
    }

    // 双向BFS
    vector<vector<string>> findLadders(string beginWord, string endWord, vector<string>& wordList) {
        // 初始化
        bool found = false, reversed = false;
        queue<string> lqueue, rqueue;
        lqueue.push(beginWord);
        rqueue.push(endWord);
        unordered_set<string> lvisited, rvisited, wordSet(wordList.begin(), wordList.end());
        lvisited.insert(beginWord);
        rvisited.insert(endWord);
        wordSet.insert(beginWord);
        vector<vector<string>> ret;
        unordered_map<string, vector<string>> d;

        // 特殊情况
        if (wordSet.count(endWord) == 0) {
            return ret;
        }
        for (const string& word : wordList) {
            d[word] = vector<string>{};
        }

        // 进行BFS
        while (!lqueue.empty() && !rqueue.empty() && !found) {
            // 保证小端遍历
            if (lqueue.size() > rqueue.size()) {
                swap(lqueue, rqueue);
                swap(lvisited, rvisited);
                reversed = !reversed;
            }
            // 遍历当前层
            int size = lqueue.size();
            unordered_set<string> oriLayer = lvisited;
            for (int i = 0; i < size; i++) {
                string currWord = lqueue.front();
                lqueue.pop();
                // 改用生成的方式，注意要判断是否为本层出现的元素
                for (int j = 0; j < currWord.size(); j++) {
                    string nextWord = currWord;
                    for (char newChar = 'a'; newChar <= 'z'; newChar++) {
                        nextWord[j] = newChar;
                        if (nextWord != currWord && wordSet.count(nextWord) > 0 && oriLayer.count(nextWord) == 0) {
                            // 入队的条件，之前从未出现过
                            if (lvisited.count(nextWord) == 0) {
                                lqueue.push(nextWord);
                                lvisited.insert(nextWord);
                            }
                            // 添加链接
                            if (!reversed) {
                                d[currWord].push_back(nextWord);
                            } else {
                                d[nextWord].push_back(currWord);
                            }
                            // 更新标志
                            if (rvisited.count(nextWord) > 0 && !found) {
                                found = true;
                            }
                        }
                    }
                }
            }
        }

        // 进行DFS
        if (d.count(beginWord) > 0) {
            vector<string> path = {beginWord};
            dfs(ret, path, d, beginWord, endWord);
        }
        return ret;
    }
};