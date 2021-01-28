def findShortestSubArray(nums):
    min_length = 0
    degree = 0
    count = {}
    first_seen = {}
    for i, n in enumerate(nums):
        if n not in first_seen:
            first_seen[n] = i
        count[n] = count.get(n, 0) + 1
        if count[n] > degree:
            degree = count[n]
            min_length = (i - first_seen[n]) + 1
        elif count[n] == degree:
            min_length = min(min_length, (i - first_seen[n]) + 1)
    return min_length

print(findShortestSubArray([1,2,2,3,1,4,2])