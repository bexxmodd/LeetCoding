#include <iostream>
#include <vector>
#include <type_traits>
#include <concepts>

template<typename T>
concept Comparable = requires (T a, T b) { a < b; b < a; };

template<Comparable I>
int binary_search(int target, std::vector<I>& array) {
    if (array.empty())
        return -1;
    int mid = array.size() / 2;
    if (array[mid] == target)
        return mid;
    else if (array[mid] < target) {
        std::vector<I> sub(array.begin(), array.begin() + mid);
        return binary_search(target, sub);
    } else {
        std::vector<I> sub(array.begin() + mid, array.end());
        return binary_search(target, sub);
    }
}

int main() {
    std::vector<int> vec{};
    vec.push_back(1);
    vec.push_back(2);
    vec.push_back(3);
    vec.push_back(4);
    vec.push_back(6);
    vec.push_back(8);
    std::cout << binary_search(3, vec) << std::endl;
    return 0;
}
