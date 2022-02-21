## My solution:
```python
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        common_prefix = []
        i = 1
        while i <= len(strs[0]):
            j = 0
            prefix = strs[0][0:i]
            i += 1
            for c, s in enumerate(strs[1:]):
                if s.startswith(prefix):
                    j += 1
                if j == len(strs) - 1:
                    common_prefix.append(prefix)
        if common_prefix != []:
            return max(common_prefix, key=len)
        else:
            return ""
```
2种解法， Horizontal scanning 和 vertical scanning, 我的是vertical scanning.
漏掉了漏掉strs长度为1的情况

## Improvement
一样的思路， 代码更短更简洁
```python
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        shortest = min(strs,key=len)
        for i, ch in enumerate(shortest):
            for other in strs:
                if other[i] != ch:
                    return shortest[:i]
        return shortest 
```


