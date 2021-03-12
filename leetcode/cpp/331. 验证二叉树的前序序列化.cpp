class Solution {
public:
    // 进行字符串分割
    vector<string> split(const string& preorder) {
        vector<string> ret;
        int start = 0; // 表示上一次非逗号起始点
        for (int i = 1; i <= preorder.size(); i++) {
            if (i == preorder.size() || preorder[i] == ',') {
                ret.push_back(preorder.substr(start, i - start));
                start = i + 1;
            }
        }
        return ret;
    }

	// 堆栈方法
    bool isValidSerialization2(string preorder) {
        vector<string> stack, vec = split(preorder);
        for (const string& node : vec) {
            stack.push_back(node);
            int n = stack.size();
            while (n >= 3 && stack[n-1] == "#" && stack[n-2] == "#" && stack[n-3] != "#") {
                stack.pop_back(), stack.pop_back(), stack.pop_back();
                stack.push_back("#");
                n = stack.size();
            }
        }
        return stack.size() == 1 && stack[0] == "#";
    }

	// 递归方法
    bool dfs(const vector<string>& vec, int& i) {
        if (i >= vec.size()) {
            return false;
        } else if (vec[i] == "#") {
            i += 1;
            return true;
        } else {
            i += 1;
            return dfs(vec, i) && dfs(vec, i);
        }
    }

    bool isValidSerialization(string preorder) {
        int i = 0;
        vector<string> vec = split(preorder);
        return dfs(vec, i) && i >= vec.size();
    }
};