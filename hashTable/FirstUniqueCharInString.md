## my solution 

success! O(n)

```python
class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = {}
        for c, i in enumerate(s):
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
        
        unique_characters = []
        for k, v in count.items():
            if v == 1:
                unique_characters.append(k)
        
        if unique_characters == []:
            return -1
        else:
            return min([s.index(i) for i in unique_characters])
```
