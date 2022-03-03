## my solution 

一开始忘记了反过来的情况， 后来加上了

```python
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map1 = {} # s as keys
        map2 = {} # t as keys
        for c, i in enumerate(s):
            if (i in map1 and map1[i] != t[c]) or (t[c] in map2 and map2[t[c]] != i):
                return False
            map1[i] = t[c]
            map2[t[c]] = i
        return True
```