#include <iostream>

class Solution {
public:
	bool duplicate(int numbers[], int length, int* duplication) {
		int i = 0;
		int index = 0;
		while (i < length) {
	        if (numbers[i] == i) {
			    i++;
			} else if (numbers[i] != numbers[numbers[i]]) {
				index = numbers[i];
				numbers[i] = numbers[index];
				numbers[index] = index;
		    } else {
			    duplication[0] = numbers[i];
				return true;
			}
		}
		return false;
	}
};

int main (int argc, char* argv[])
{
	int numbers[] = {2, 3, 1, 0, 2, 5, 3};
	int duplication[] = {0};
	Solution s;
	if (s.duplicate(numbers, 7, duplication)) {
		printf("Ture %d\n", duplication[0]);
	} else {
	    printf("False\n");
	}
    return 0;
}
