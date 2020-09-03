"""
Given an array of integers, find out whether there are
two distinct indices i and j in the array such that the
absolute difference between nums[i] and nums[j] is at most t
and the absolute difference between i and j is at most k.


Example 1:

Input: nums = [1,2,3,1], k = 3, t = 0
Output: true
"""

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: list, k: int, t: int) -> bool:
        if t == 0 and len(nums) == len(set(nums)):
            return False
        for i in range(len(nums)):
            for j in range(i + 1, i + k + 1):
                if j >= len(nums):
                    break
                if abs(nums[i] - nums[j]) <= t:
                    return True
        return False

# Test solution
s = Solution()
print(s.containsNearbyAlmostDuplicate(nums = [1,2,3,1], k = 3, t = 0))
print(s.containsNearbyAlmostDuplicate(nums = [1,0,1,1], k = 1, t = 2))
print(s.containsNearbyAlmostDuplicate(nums = [1,5,9,1,5,9], k = 2, t = 3))
print(s.containsNearbyAlmostDuplicate(nums = [-1, -1], k = 1, t = -1))
print(s.containsNearbyAlmostDuplicate(nums = [1, 2, 3, 1], k = 3, t = 0))
print(s.containsNearbyAlmostDuplicate(nums = [-3, 3], k = 2, t = 4))
