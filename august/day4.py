# Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

import math

class Solution:

    def isPowerOfFour(self, num: int) -> bool:
        if num <= 0:
            return False
        result = math.log(num, 4)
        return result.real.is_integer()


# Test
sol = Solution()
print(sol.isPowerOfFour(16))
print(sol.isPowerOfFour(64))
print(sol.isPowerOfFour(-2147483648))
print(sol.isPowerOfFour(81))
print(sol.isPowerOfFour(0))
print(sol.isPowerOfFour(1))
print(sol.isPowerOfFour(4))
print(sol.isPowerOfFour(-81))