# https://leetcode.com/explore/learn/card/fun-with-arrays/523/conclusion/3574/

def sortedSquares(self, nums: List[int]) -> List[int]:
        sq_sorted = [i*i for i in nums]
        return sorted(sq_sorted)