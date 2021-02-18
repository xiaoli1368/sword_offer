class Solution {
public:
	// ===== 朴素的单向BFS方法（超时了）=====

    // 判断两字符串是否最多只有一位不同
    bool canChange(const string& a, const string& b) {
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

    int ladderLength(string beginWord, string endWord, vector<string>& wordList) {
        int step = 1, size;
        queue<string> queue;
        queue.push(beginWord);
        unordered_set<string> visited;

        while (!queue.empty()) {
            size = queue.size();
            for (int i = 0; i < size; i++) {
                string currWord = queue.front();
                queue.pop();
                if (currWord == endWord) {
                    return step;
                }
                for (const string& nextWord : wordList) {
                    if (visited.count(nextWord) == 0 && canChange(currWord, nextWord)) {
                        queue.push(nextWord);
                        visited.insert(nextWord);
                    }
                }
            }
            step += 1;
        }
        return 0;
    }

	// ===== 单向BFS优化方法（可以AC） =====
	int ladderLength(string beginWord, string endWord, vector<string>& wordList) {
        int step = 1, size;
        queue<string> queue;
        queue.push(beginWord);
        unordered_set<string> wordSet(wordList.begin(), wordList.end());

        while (!queue.empty()) {
            size = queue.size();
            for (int i = 0; i < size; i++) {
                string currWord = queue.front();
                queue.pop();
                if (currWord == endWord) {
                    return step;
                }
                // 改为对当前单词的修改，使用hash
                for (int j = 0; j < currWord.size(); j++) {
                    char oriChar = currWord[j];
                    for (char newChar = 'a'; newChar <= 'z'; newChar++) {
                        if (newChar != currWord[j]) {
                            currWord[j] = newChar;
                            if (wordSet.count(currWord) > 0) {
                                queue.push(currWord);
                                wordSet.erase(currWord);
                            }
                        }
                    }
                    currWord[j] = oriChar;
                }
            }
            step += 1;
        }
        return 0;
    }

	// ===== 双向BFS优化版 =====
	int ladderLength(string beginWord, string endWord, vector<string>& wordList) {
        // 初始化
        int step = 1, size;
        queue<string> lqueue, rqueue;
        lqueue.push(beginWord);
        rqueue.push(endWord);
        unordered_set<string> lvisited, rvisited, wordSet(wordList.begin(), wordList.end());
        lvisited.insert(beginWord);
        rvisited.insert(endWord);

        // 特殊情况
        if (wordSet.count(endWord) == 0) {
            return 0;
        }

        while (!lqueue.empty() && !rqueue.empty()) {
            // 从较小的一段开始遍历
            if (lqueue.size() > rqueue.size()) {
                swap(lqueue, rqueue);
                swap(lvisited, rvisited);
            }
            size = lqueue.size();
            for (int i = 0; i < size; i++) {
                string currWord = lqueue.front();
                lqueue.pop();
                if (rvisited.count(currWord) > 0) {
                    return step;
                }
                // 改为对当前单词的修改，使用hash
                for (int j = 0; j < currWord.size(); j++) {
                    char oriChar = currWord[j];
                    for (char newChar = 'a'; newChar <= 'z'; newChar++) {
                        if (newChar != currWord[j]) {
                            currWord[j] = newChar;
                            if (lvisited.count(currWord) == 0 && wordSet.count(currWord) > 0) {
                                lqueue.push(currWord);
                                lvisited.insert(currWord);
                            }
                        }
                    }
                    currWord[j] = oriChar;
                }
            }
            step += 1;
        }
        return 0;
    }
};