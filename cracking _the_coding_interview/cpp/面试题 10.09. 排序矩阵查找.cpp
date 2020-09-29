#include <vector>

class Solution {
public:
    bool searchMatrix(std::vector<std::vector<int>>& matrix, int target) {
		if (matrix.empty()) {
			return false;
		}

		int row = 0;
		int col = matrix[0].size() - 1;

		while (row < matrix.size() && col >= 0) {
			if (matrix[row][col] == target) {
			    return true;
			} else if (matrix[row][col] > target) {
			    col -= 1;
     	    } else if (matrix[row][col] < target) {
			    row += 1;
            }
		}

		return false;
    }
};