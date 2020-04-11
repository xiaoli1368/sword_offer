#include <iostream>
#include <vector>
#include <string>

class Soliton {
public:
    std::string PrintMinNumber(std::vector<int> numbers) {
        std::string result;
        if (numbers.empty()) {
            return result;
        }

        int length = numbers.size();
        for (int i = 0; i < length - 1; i++) {
            for (int j = i + 1; j < length; j++) {
                std::string a = std::to_string(numbers[i]);
                std::string b = std::to_string(numbers[j]);
                if (a + b > b + a) {
                    int tmp = numbers[i];
                    numbers[i] = numbers[j];
                    numbers[j] = tmp;
                }
            }
        }

        for (auto i : numbers) {
            result += std::to_string(i);
        }
        return result;
    }
};

int main(int argc, char* argv[])
{
    Soliton s;
    std::vector<int> numbers = {3, 32, 321};

    std::cout << s.PrintMinNumber(numbers) << std::endl;
    return 0;
}