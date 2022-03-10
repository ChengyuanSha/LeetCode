## my solution 

```python
from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
```



## another approach 

sorting both strings will result in two identical strings