"""
https://leetcode.com/problems/minimum-cost-to-move-chips-to-the-same-position/
"""

class Solution:

    def minCostToMoveChips(self, position) -> int:
        table = dict()
        for i in position:
            if i not in table:
                table[i] = 1
            else:
                table[i] += 1
        moving_towards = 0
        for i in table:
            if table[i] > moving_towards:
                moving_towards = table[i]

        for i in table:
            if table[i] > moving_towards:
                diff = table[i] - moving_towards
                



s = Solution()
print('[1,2,3] -->', s.minCostToMoveChips([1,2,3]))
print('[2,2,2,3,3] --> ', s.minCostToMoveChips([2,2,2,3,3]))