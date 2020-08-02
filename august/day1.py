class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word == word.lower() or word == word.upper() or word == word.title():
            return True