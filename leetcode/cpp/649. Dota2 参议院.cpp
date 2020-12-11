class Solution {
public:
    string predictPartyVictory(string senate) {
        if (senate.empty()) {
            return "Dire";
        }
        // 构造两个队列
        std::queue<int> qd, qr;
        for (int i = 0; i < senate.size(); i++) {
            if (senate[i] == 'D') {
                qd.push(i);
            } else {
                qr.push(i);
            }
        }
        // 遍历判断
        while (!qd.empty() && !qr.empty()) {
            if (qd.front() < qr.front()) {
                qr.pop();
                qd.push(qd.front() + senate.size());
                qd.pop();
            } else {
                qd.pop();
                qr.push(qr.front() + senate.size());
                qr.pop();
            }
        }
        // 返回结果
        return (qd.empty() ? "Radiant" : "Dire");
    }
};