class MyQueue {
public:
    /** Initialize your data structure here. */
    stack<int> s1, s2;
    MyQueue() {

    }

    // 把非空的s1元素push到已空的s2
    void push_s1_s2() {
        if (s2.empty()) {
            while (!s1.empty()) {
                s2.push(s1.top());
                s1.pop();
            }
        }
    }
    
    /** Push element x to the back of queue. */
    void push(int x) {
        s1.push(x);
    }
    
    /** Removes the element from in front of queue and returns that element. */
    int pop() {
        push_s1_s2();
        if (!s2.empty()) {
            int ret = s2.top();
            s2.pop();
            return ret;
        }
        return -1;
    }
    
    /** Get the front element. */
    int peek() {
        push_s1_s2();
        if (!s2.empty()) {
            return s2.top();
        }
        return -1;
    }
    
    /** Returns whether the queue is empty. */
    bool empty() {
        return s1.empty() && s2.empty();
    }
};

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue* obj = new MyQueue();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->peek();
 * bool param_4 = obj->empty();
 */