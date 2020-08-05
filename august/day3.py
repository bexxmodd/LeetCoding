class Solution:

    def isPalindrome(self, s: str) -> bool:
        # Extract only alphanumerics from the string
        alphas = "".join([i.lower() for i in s if i.isalnum())])
        return alphas == alphas[::-1]


S = Solution()
print(S.isPalindrome("A man, a plan, a canal: Panama"))
print(S.isPalindrome("race a car"))
print(S.isPalindrome(""))
print(S.isPalindrome("baab"))
print(S.isPalindrome("0P"))