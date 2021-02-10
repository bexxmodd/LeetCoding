def binary_search(data: list[int], 
                target: int,
                low: int,
                high: int) -> int:
    if low > high:
        return -1
    else:
        mid = int((low + high) / 2)
        if target == data[mid]:
            return mid
        elif target < data[mid]:
            return binary_search(data, target, low, mid-1)
        else:
            return binary_search(data, target, mid+1, high)
        

arr = [2, 3, 12, 5, 1, 9, 32 ,52, 45]
arr.sort()
print(binary_search(arr, 9, 0, len(arr)))
