## My solution:
```python
import re

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "" :
            return 0
        match = re.search(needle, haystack)
        if match:
            return match.start()
        else:
            return -1
        
```


## Improvements:   
如果不能用re库也很容易，直接每一个 + 查找的长度看
```python
class Solution(object):
    def strStr(self, haystack, needle):
        for i in range(len(haystack) - len(needle)+1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1
```