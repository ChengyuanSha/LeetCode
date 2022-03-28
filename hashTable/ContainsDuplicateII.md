
一开始超时了，后面看了思路写出：

```python
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        record = set()
        for i, x in enumerate(nums):
            if x in record:
                return True
            record.add(x)
            if len(record) > k:
                record.remove(nums[i-k])
        return False
```


