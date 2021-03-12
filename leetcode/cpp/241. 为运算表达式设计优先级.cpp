class Solution {
public:
    vector<int> diffWaysToCompute(string s) {
        vector<int> ret;
        for (int i = 0; i < s.size(); i++) {
            if (s[i] == '+' || s[i] == '-' || s[i] == '*') {
                vector<int> left = diffWaysToCompute(s.substr(0, i));
                vector<int> right = diffWaysToCompute(s.substr(i + 1));
                for (const int& l : left) {
                    for (const int& r : right) {
                        switch (s[i]) {
                            case '+' : ret.push_back(l + r); break;
                            case '-' : ret.push_back(l - r); break;
                            case '*' : ret.push_back(l * r); break;
                        }
                    }
                }
            }
        }
        if (ret.empty()) ret.push_back(std::stoi(s));
        return ret;
    }

    vector<int> diffWaysToCompute(string s) {
        // 特殊情况
        vector<int> ret;
        if (s.empty()) {
            return ret;
        }

        // 初始化
        int num = 0;
        char sign = ' ';
        istringstream ss(s + "+");
        vector<int> nums;
        vector<char> signs;
        while(ss >> num && ss >> sign) {
            nums.push_back(num);
            signs.push_back(sign);
        }

        // 初始化dp
        int n = nums.size();
        vector<vector<vector<int>>> dp(n, vector<vector<int>>(n, vector<int>()));
        for (int i = n - 1; i >= 0; i--) {
            for (int j = i; j < n; j++) {
                if (i == j) {
                    dp[i][j].push_back(nums[i]);
                    continue;
                }
                for (int k = i; k < j; k++) {
                    for (const int& l : dp[i][k]) {
                        for (const int& r : dp[k + 1][j]) {
                            switch (signs[k]) {
                                case ('+') : dp[i][j].push_back(l + r); break;
                                case ('-') : dp[i][j].push_back(l - r); break;
                                case ('*') : dp[i][j].push_back(l * r); break;
                            }
                        }
                    }
                }
            }
        }
        return dp[0][n - 1];
    }
};