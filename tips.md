- When questions asks to find common elements in words, lists etc. Good strategy is to user `Counter` from collections and `&` the entities you want to compare.


Example for finding common characters in words:

```python
def commonChars(self, A: List[str]) -> List[str]:
        cntr = collections.Counter(A[0]) # count chars of first word
        for a in A:
            cntr &= collections.Counter(a) # & will keep common chars
        return list(cntr.elements())
```

- We can sort `Counter` by first using it's method `most_common()` and then running `.sort()` method after.

Example:
```python
count = Counter(nums).most_common()
count.sort(key = lambda x: x[0])
```

- To convert `Counter` results, which are tuples, into a list of values use following:

```python
res = []
for i in count:
    val, n = i
    res.extend([val] * i)
```