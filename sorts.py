import random
from typing import List, TypeVar

T = TypeVar('T')


def insertion_sort(arr: List[T]) -> None:
    """
    Insertion Sort

    Time:
        O(n^2) - Worst Case
        O(n) - Best Case

    Space:
        O(1) as sorting happens in-place
    """
    for i in range(1, len(arr)):
        tmp = arr[i]  # value
        hole = i  # index
        while hole > 0 and arr[hole - 1] > tmp:
            arr[hole] = arr[hole - 1]
            hole -= 1
        arr[hole] = tmp

def bubble_sort(arr: List[T]) -> None:
    """
    Bubble Sort

    Time:
        O(n^2)

    Space:
        O(1) as sorting happens in-place
    """
    for i, _ in enumerate(arr):
        is_sorted = True
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                is_sorted = False
        if is_sorted:
            return


def merge_sort(arr: List[T]) -> None:
    if len(arr) < 2:
        return

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    merge_sort(left)
    merge_sort(right)
    _merge(left, right, arr)


def _merge(left: List[T], right: List[T], origin: List[T]) -> None:
    i = k = j = 0
    while i < len(left) and j < len(right):

        if left[i] <= right[j]:
            origin[k] = left[i]
            i += 1
        else:
            origin[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        origin[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        origin[k] = right[j]
        j += 1
        k += 1


def quick_sort(arr: List[T]) -> List[T]:
    """
    Quick sort algorithm with D&C strategy that produces sorted list

    Time:
        O(n*long(n)) - Average
        [considered worst case with Random pivot picking strategy]
        O(n^2) - worst case without randomized pivot picking

    Space:
        O(n) - Because we have to create a new list
    """
    size = len(arr)
    if size < 2:
        return arr
    pivot = random.randint(0, size - 1)
    left = []
    right = []
    for i in range(size):
        if i != pivot:
            if arr[i] < arr[pivot]:
                left.append(arr[i])
            else:
                right.append(arr[i])
    return quick_sort(left) + [arr[pivot]] + quick_sort(right)


def qsort(arr):
    """
    In-place quick sort algorithm with D&C strategy

    Time:
        O(n*long(n)) - Average
        [considered worst case with Random pivot picking strategy]
        O(n^2) - worst case without randomized pivot picking

    Space:
        O(1)
    """
    __qsort(arr, 0, len(arr) - 1)


def __qsort(arr, start, end):
    if start < end:
        pivot_idx = partition(arr, start, end)
        __qsort(arr, start, pivot_idx - 1)
        __qsort(arr, pivot_idx + 1, end)


def partition(arr, start, end) -> int:
    pivot = arr[random.randint(0, end)]
    index = start
    for i in range(start, end):
        if arr[i] <= pivot:
            arr[i], arr[index] = arr[index], arr[i]
            index += 1
    arr[index], arr[end] = arr[end], arr[index]
    return index


if __name__ == '__main__':
    a = [2, 4, 1, 6, 8, 5, 3, 7]
    bubble_sort(a)
    b = [8, 11, 13, 16, 9, 6, 23, 7]
    merge_sort(b)
    c = [2, 44, 41, 63, 88, 52, 3, 37]
    qsort(c)
    d = [7, 2, 4, 1, 5, 3]
    insertion_sort(d)
    print('Bubble Sort', a)
    print('Merge Sort', b)
    print('Quick Sort', c)
    print('Insertion Sort', d)
