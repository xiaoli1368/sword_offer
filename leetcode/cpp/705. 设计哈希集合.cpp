class MyHashSet {
public:
    int buckets;
    vector<vector<int>> tabel;

    /** Initialize your data structure here. */
    MyHashSet() {
        buckets = 1009;
        tabel.resize(buckets);
    }

    void add(int key) {
        vector<int>& vec = tabel[key % buckets];
        if (find(vec.begin(), vec.end(), key) == vec.end()) {
            vec.push_back(key);
        }
        return;
    }
    
    void remove(int key) {
        vector<int>& vec = tabel[key % buckets];
        auto it = find(vec.begin(), vec.end(), key);
        if (it != vec.end()) {
            vec.erase(it);
        }
        return;
    }
    
    /** Returns true if this set contains the specified element */
    bool contains(int key) {
        vector<int>& vec = tabel[key % buckets];
        return find(vec.begin(), vec.end(), key) != vec.end();
    }
};

/**
 * Your MyHashSet object will be instantiated and called as such:
 * MyHashSet* obj = new MyHashSet();
 * obj->add(key);
 * obj->remove(key);
 * bool param_3 = obj->contains(key);
 */