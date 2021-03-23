class Solution {
public:
    int add(int x, int y) {return x + y;}
    int sub(int x, int y) {return x - y;}
    int mul(int x, int y) {return x * y;}
    int div(int x, int y) {return x / y;}
    typedef int (Solution::*func)(int, int);

    int evalRPN(vector<string>& tokens) {
        int x, y;
        stack<int> st;
        unordered_map<string, func> d;
        d["+"] = &Solution::add;
        d["-"] = &Solution::sub;
        d["*"] = &Solution::mul;
        d["/"] = &Solution::div;
        for (const string& curr : tokens) {
            if (d.count(curr) > 0) {
                y = st.top(), st.pop();
                x = st.top(), st.pop();
                st.push((this->*d[curr])(x, y));
            } else {
                st.push(stoi(curr));
            }
        }
        return st.top();
    }
};