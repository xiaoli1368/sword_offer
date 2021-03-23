class Solution {
public:
    // 参考链接：https://briangordon.github.io/2014/08/the-skyline-problem.html
    // multiset内部自动排序，注意将左边界高度设置为负值
    // 如果一个位置既有建筑物进来，又有建筑物离开，会先选择进来的。
    vector<vector<int>> getSkyline(vector<vector<int>>& buildings) {
        int last = 0, curr = 0;
        vector<vector<int>> ret;
        multiset<pair<int, int>> lines;
        multiset<int> heights;
        heights.insert(0);
        
        // 所有的建筑物转换为两道竖线，[pos, height]
        // 高度为负值，表示左边界，内部进行排序，pos越小，height越小的在前面
        // height越小，表示右边界高度越大
        for (const auto& b : buildings) {
            lines.insert(make_pair(b[0], -b[2]));
            lines.insert(make_pair(b[1], b[2]));
        }

        // 依次遍历
        // 左边界高度直接入堆，右边界高度直接出堆
        // 只有高度与上一次不同，出现转折点，
        for (const auto& line : lines) {
            if (line.second < 0) {
                heights.insert(-line.second);
            } else {
                heights.erase(heights.find(line.second));
            }
            curr = *heights.rbegin();
            if (curr != last) {
                ret.push_back({line.first, curr});
                last = curr;
            }
        }
        return ret;
    }
};