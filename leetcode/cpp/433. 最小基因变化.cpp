class Solution {
public:
    int minMutation(string start, string end, vector<string>& bank) {
        // 初始化
        int step = 0, size;
        string letters = "ACGT", currWord;
        queue<string> lqueue, rqueue;
        lqueue.push(start), rqueue.push(end);
        unordered_set<string> lvisited, rvisited, wordSet(bank.begin(), bank.end());
        lvisited.insert(start), rvisited.insert(end);

        // Double-BFS
        while (!lqueue.empty() && !rqueue.empty()) {
            if (lqueue.size() > rqueue.size()) {
                swap(lqueue, rqueue);
                swap(lvisited, rvisited);
            }
            size = lqueue.size();
            for (int i = 0; i < size; i++) {
                currWord = lqueue.front();
                lqueue.pop();
                if (rvisited.count(currWord) > 0) {
                    return step;
                }
                for (int j = 0; j < currWord.size(); j++) {
                    char oriChar = currWord[j];
                    for (const char & newChar : letters) {
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
        return -1;
    }
};