"""Given a non-empty string check if it can be constructed by taking a substring
of it and appending multiple copies of the substring together. You may assume the given
string consists of lowercase English letters only and its length will not exceed 10000.

Example 1:

Input: "abab"
Output: True
Explanation: It's the substring "ab" twice.
"""

class Solution:

    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        if n == 1: return False
        
        for i in range(1, n):
            if n % i == 0:
                if s == s[:i] * (n // i):
                    return True
        return False



sol = Solution()
print(sol.repeatedSubstringPattern("abab")) # True
print(sol.repeatedSubstringPattern("aba")) # False
print(sol.repeatedSubstringPattern("ababba")) # False
print(sol.repeatedSubstringPattern("abcabcabcabc")) # True


# print(f"s[:{i}] --> {s[:i]} * {n} // {i} --> {n // i} will equal: {s[:i] * (n // i)}")