# https://leetcode.com/explore/challenge/card/november-leetcoding-challenge/565/week-2-november-8th-november-14th/3526/

class Solution:
    def flipAndInvertImage(self, A: list) -> list:
        result = []
        for row in A:
            row.reverse()
            image = [1 if i == 0 in row else i ==1 for i in row]
            result.append(image)
        return result