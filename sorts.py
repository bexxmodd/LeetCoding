from typing import List, TypeVar

T = TypeVar('T')



def merge_sort(arr: List[T]):
    if len(arr) == 2:
        if arr[0] > arr[1]:
            return [arr[1], arr[0]]
        else:
            return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    merge_sort(left)
    merge_sort(right)
    _merge(left, right, arr)


def _merge(left: List[T], right: List[T], origin: List[T]):
    i = k = j = 0
    while i < len(left) and j < len(right):

        if left[i] < right[j]:
            origin[k] = left[i]
            i += 1
        else:
            origin[k] = left[j]
            j += 1
        k += 1

    while j < len(left):
        origin[k] = right[j]
        j += 1
        k += 1
    while i < len(right):
        origin[k] = right[i]
        i += 1
        k += 1


if __name__ == '__main__':
    print(merge_sort([2, 4, 1, 6, 8, 5, 3, 7]), [1, 2, 3, 4, 5, 6, 7, 8])
