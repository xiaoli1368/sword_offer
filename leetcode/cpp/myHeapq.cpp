// 个人实现的小顶堆

#include <iostream>
#include <vector>
#include <assert.h>

template <class T>
void swap(std::vector<T>& vec, int a, int b) {
    T tmp = vec[a];
    vec[a] = vec[b];
    vec[b] = tmp;
}

template <class T>
void shift_up(std::vector<T>& vec, int i) {
    while (1) {
        int p = (i - 1) / 2;
        if (p >= 0 && vec[p] > vec[i]) {
            swap(vec, i, p);
            i = p;
        } else {
            break;
        }
    }
}

template <class T>
void shift_down(std::vector<T>& vec, int n, int i) {
    while (1) {
        int smallest = i;
        int l = 2 * i + 1;
        int r = 2 * i + 2;
        if (l < n && vec[l] < vec[smallest]) {
            smallest = l;
        }
        if (r < n && vec[r] < vec[smallest]) {
            smallest = r;
        }
        if (smallest != i) {
            swap(vec, i, smallest);
            i = smallest;
        } else {
            break;
        }
    }
}

template <class T>
void heapify(std::vector<T>& vec) {
    assert(!vec.empty());
    for (int i = vec.size()/2-1; i >= 0; i--) {
        shift_down(vec, vec.size(), i);
    }
}

template <class T>
T heappop(std::vector<T>& vec) {
    assert(!vec.empty());
    swap(vec, 0, vec.size() - 1);
    shift_down(vec, vec.size(), 0);
    int ret = vec.back();
    vec.pop_back();
    return ret;
}

template <class T>
void heappush(std::vector<T>& vec, T num) {
    vec.push_back(num);
    shift_up(vec, vec.size() - 1);
}

template <class T>
void printf_1d_vec(const std::vector<T>& vec) {
    for (auto & num : vec) {
        std::cout << num << ", ";
    }
    std::cout << std::endl;
}

int main(int argc, char* argv[])
{
    std::vector<int> vec = {5, 2, 6, 2, 0, 5, 9, 12, 3};
    printf_1d_vec(vec);
    heapify(vec);
    printf_1d_vec(vec);
    heappop(vec);
    printf_1d_vec(vec);
    heappush(vec, -1);
    printf_1d_vec(vec);
    return 0;
}