class MinStack {
public:
    /** initialize your data structure here. */
    stack<int> comSt, minSt;
    MinStack() {
    }
    
    void push(int val) {
        comSt.push(val);
        if (minSt.empty() || minSt.top() >= val) {
            minSt.push(val);
        }
    }
    
    void pop() {
        if (comSt.top() == minSt.top()) {
            minSt.pop();
        }
        comSt.pop();
    }
    
    int top() {
        return comSt.top();
    }
    
    int getMin() {
        return minSt.top();
    }
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(val);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */