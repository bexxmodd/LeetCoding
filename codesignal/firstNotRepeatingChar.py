# https://app.codesignal.com/interview-practice/task/uX5iLwhc6L5ckSyNC

def firstNotRepeatingCharacter(s):
    for char in s:
        print(f'char:{char} s.index:{s.index(char)} == s.rindex:{s.rindex(char)}')
        if s.index(char) == s.rindex(char):
            return char
    return '_'


print(firstNotRepeatingCharacter('abacabad')) # c
print(firstNotRepeatingCharacter('abacabaabacaba')) # _