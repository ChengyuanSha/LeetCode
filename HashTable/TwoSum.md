
自己的解答
```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        record = {}
        for c, i in enumerate(nums):
            if i in record.values():
                return [nums.index(target-i) , c]
            record[i] = target - i
```


不足：
忘记了负数的情况，小修改后通过

