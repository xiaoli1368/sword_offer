#include <iostream>
#include <vector>

class Solution {
public:
	bool Find(int target, std::vector<std::vector<int>> array) {
		int i = 0;
		int j = array[0].size() - 1;
		while (i < array.size() && j >= 0) {
	        if (target == array[i][j]) {
			    return true;
			} else if (target < array[i][j]) {
			    j--;
			} else {
			    i++;
			}
		}

		return false;
	}
};

int main(int argc, char* argv[])
{
    int target = 26;
	std::vector<std::vector<int>> array = {{1, 4, 7, 11, 15},
	                                       {2, 5, 8, 12, 19},
	                                       {3, 6, 9, 16, 22},
	                                       {10, 13, 14, 17, 24},
										   {18, 21, 23, 26, 30}};
	Solution s;
	if (s.Find(target, array)) {
	    std::cout << "Ture" << std::endl;
	} else {
        std::cout << "False" << std::endl;	
	}
	return 0;
}
