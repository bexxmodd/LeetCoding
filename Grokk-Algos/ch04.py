from typing import List, TypeVar

T = TypeVar('T')

def rec_sum(nums: List[int]) -> int:
    if not nums:
        return 0
    elif len(nums) == 1:
        return nums[0]
    return nums[0] + rec_sum(nums[1:])

def elem_count(nums: List[int]) -> int:
    if not nums:
        return 0
    else:
        return 1 + elem_count(nums[1:])

def max_val(nums: List[int]) -> int:
    if len(nums) == 2:
        return nums[0] if nums[0] > nums[1] else nums[1]
    sub_max= max_val(nums[1:])
    return nums[0] if nums[0] > sub_max else sub_max

def binary_search(x: int, nums: List[int]) -> int:
    mid = len(nums) // 2
    if not nums:
        return None
    if nums[mid] == x:
        return x
    return binary_search(x, nums[mid:]) if x > nums[mid] else binary_search(x, nums[:mid])


###############################################################################
################################ QUICK SORT ###################################
###############################################################################

def qsort(array: List[T]) -> List[T]:
    # base case
    if len(array) < 2:
        return array

    left = []
    right = []
    for item in array[1:]:
        if item <= array[0]:
            left.append(item)
        else:
            right.append(item)
    return qsort(left) + [array[0]] + qsort(right)


###############################################################################
########################### BREADTH FIRST SEARCH ##############################
###############################################################################

from collections import deque
from typing import TypeVar

T = TypeVar('T')

def bfs(start: T, target: T, graph) -> int:
    depth = 0
    frontier = deque()
    frontier.appendleft(graph[start])
    visited = set()
    while frontier:
        current = frontier.pop()
        if current == target:
            return depth
        for child in current.neighbors():
            if child not in visited:
                frontier.appendleft(graph[current])
    return -1




if __name__ == '__main__':
    print(rec_sum([1, 5, 3, 6, 9, 2]))
    print(elem_count([1, 5, 3, 6, 9, 2]))
    print(max_val([1, 5, 3, 6, 9, 2]))
    print(binary_search(3, [1, 3, 5, 6, 8, 9]))
    print(qsort([7, 1, 5, 3, 6, 9, 2]))

    morning = {
        'shower': ('wake up'),
        'wake up': ('shower', 'brush teeth'),
        'brush teeth': ('wake up', 'eat breakfast'),
        'eat breakfast': ('brush teeth')
    }
    print(bfs('wake up', 'eat breakfast', morning))

