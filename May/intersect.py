# https://leetcode.com/problems/intersection-of-two-arrays-ii/submissions/

from collections import Counter

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        cntr = Counter(nums1)
        cntr &= Counter(nums2)
        res = []
        for k in cntr.keys():
            res += ([k] * cntr[k])
        return res