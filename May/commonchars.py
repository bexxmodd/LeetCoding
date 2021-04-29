# https://leetcode.com/problems/find-common-characters/

from collections import Counter

class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        cntr = collections.Counter(A[0])
        for a in A:
            cntr &= collections.Counter(a)
        return list(cntr.elements())