"""
Design a data structure that supports the following two operations:

void addWord(word)
bool search(word)
search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.
"""

from collections import defaultdict

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.index = {}
        self.words = defaultdict(list)


    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        self.index[word] = True
        self.words[len(word)].append(word)


    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        if word in self.index:
            return True
        if len(word) not in self.words:
            return False
        if word == '.' * len(word):
            return True
        for i in self.words[len(word)]:
            if self._comparison_(word, i):
                return True
        return False

    def _comparison_(self, word, compare):
        for j, k in zip(word, compare):
            if j != k and j != '.':
                return False
        return True


# Your WordDictionary object will be instantiated and called as such:
obj = WordDictionary()
obj.addWord("bad")
obj.addWord("dad")
obj.addWord("dad")
obj.addWord("mad")
print(obj.search("pad")) # false
print(obj.search("bad")) # true
print(obj.search(".at")) # false
obj.addWord('bat')
print(obj.search('.at')) # true
print(obj.search("b..")) # true