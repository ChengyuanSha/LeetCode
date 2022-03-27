## My answer 

```python
class Solution:
    def firstBadVersion(self, n: int) -> int:
        low = 0
        high = n - 1
        first_bad = None
        while low <= high:
            mid = (low + high) // 2
            isbad = isBadVersion(mid+1) # here mid is index, actual version should + 1
            if isbad: # higher version all bad
                first_bad = mid + 1
                high = mid - 1
            else:
                low = mid + 1
        return first_bad
```