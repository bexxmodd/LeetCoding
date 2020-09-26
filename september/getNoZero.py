# https://leetcode.com/problems/convert-integer-to-the-sum-of-two-no-zero-integers/

def getNoZeroIntegers(n: int) -> list:
    result = [0] * 2
    for i in range(0, n + 1):
        if str(i).count('0') == 0:
            remainder = n - i
            if str(remainder).count('0') == 0:
                result[0] = i
                result[1] = remainder
                return result

print(getNoZeroIntegers(1010)) # [11, 999]