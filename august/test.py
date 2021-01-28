def findShortestSubArray(nums) -> int:
    C = {}
    for i, n in enumerate(nums):
        if n in C:
            C[n].append(i)
        else:
            C[n] = [i]
    print(C)
    M = max([len(i) for i in C.values()])
    print(M)
    return min([i[-1]-i[0] for i in C.values() if len(i) == M]) + 1


print(findShortestSubArray([1,2,2,3,1,4,2]))
print()
print(findShortestSubArray([1,2,2,3,1]))
