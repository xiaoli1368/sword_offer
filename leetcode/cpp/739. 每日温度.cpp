class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& vec) {
        if (vec.empty()) {
            return vec;
        }

        std::stack<int> stack;
        std::vector<int> ret(vec.size(), 0);

        for (int i = 0; i < vec.size(); i++) {
            while (!stack.empty() && vec[stack.top()] < vec[i]) {
                int j = stack.top();
                stack.pop();
                ret[j] = i - j;
            }
            stack.push(i);
        }
        return ret;
    }
};