// 这里自行定义了数据结构，感觉还不错

class StockSpanner {
public:
    typedef struct DataPair {
        int day;
        int price;
        DataPair(int day=0, int price=0) : day(day) , price(price) {}
    } DataPair;

    int day = 0;
    std::stack<DataPair> st;
    StockSpanner() {}
    
    int next(int price) {
        day += 1;
        while (!st.empty() && st.top().price <= price) {
            st.pop();
        }
        int ret = day - (st.empty() ? 0 : st.top().day);
        st.push(DataPair(day, price));
        return ret;
    }
};

/**
 * Your StockSpanner object will be instantiated and called as such:
 * StockSpanner* obj = new StockSpanner();
 * int param_1 = obj->next(price);
 */