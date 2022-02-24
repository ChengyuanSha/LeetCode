## my solution 

```python
import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub("[\W_]+", "", s.lower())
        return s == s[::-1]
```





