# https://leetcode.com/problems/sort-array-by-increasing-frequency/

from collections import Counter

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        count = Counter(nums).most_common()
        count.sort(key = lambda x: x[0], reverse=True)
        count.sort(key = lambda x: x[1])
        
        res = []
        for i in count:
            v, n = i
            res.extend([v] * n)
    
        return res