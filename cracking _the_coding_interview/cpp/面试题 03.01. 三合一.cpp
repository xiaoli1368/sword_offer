class TripleInOne {
private:
    int stackSize;
    std::vector<int> len;
    std::vector<int> vec;
public:
    TripleInOne(int stackSize) {
        this->stackSize = stackSize;
        len = std::vector<int>(3, 0);
        vec = std::vector<int>(stackSize * 3, 0);
    }
    
    void push(int stackNum, int value) {
        if (len[stackNum] >= stackSize) {
            return;
        }
        vec[stackNum * stackSize + len[stackNum]] = value;
        len[stackNum] += 1;
    }
    
    int pop(int stackNum) {
        if (len[stackNum] <= 0) {
            return -1;
        }
        int ret = vec[stackNum * stackSize + len[stackNum] - 1];
        len[stackNum] -= 1;
        return ret;
    }
    
    int peek(int stackNum) {
        if (len[stackNum] <= 0) {
            return -1;
        }
        return vec[stackNum * stackSize + len[stackNum] - 1];
    }
    
    bool isEmpty(int stackNum) {
        return len[stackNum] == 0;
    }
};

/**
 * Your TripleInOne object will be instantiated and called as such:
 * TripleInOne* obj = new TripleInOne(stackSize);
 * obj->push(stackNum,value);
 * int param_2 = obj->pop(stackNum);
 * int param_3 = obj->peek(stackNum);
 * bool param_4 = obj->isEmpty(stackNum);
 */