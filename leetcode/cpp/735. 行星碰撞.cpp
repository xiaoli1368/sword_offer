class Solution {
public:
    vector<int> asteroidCollision(vector<int>& asteroids) {
        vector<int> stack;
        for (const int& curr : asteroids) {
            bool flag = true;
            while (!stack.empty() && stack.back() > 0 && curr < 0) {
                if (stack.back() == -curr) {
                    flag = false;
                    stack.pop_back();
                    break;
                } else if (stack.back() > -curr) {
                    flag = false;
                    break;
                } else {
                    stack.pop_back();
                }
            }
            if (flag) {
                stack.push_back(curr);
            }
        }
        return stack;
    }
};