## my answer

```python
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = {}
        for i in arr:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
        occurrences = list(count.values())
        
        return len(set(occurrences)) == len(occurrences)
```

