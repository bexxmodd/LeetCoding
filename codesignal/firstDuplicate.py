# https://app.codesignal.com/interview-practice/task/pMvymcahZ8dY4g75q

def firstDuplicate(a: list) -> int:
    duplicates = set()
    for i in a:
        if i in duplicates:
            return i
        else:
            duplicates.add(i)
    return -1


print(firstDuplicate([2,1,3,4,3,2]))
print(firstDuplicate([2,4,3,5]))
print(firstDuplicate([2,2]))