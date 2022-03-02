

## my solution

```python
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        validation_arr = list(range(len(nums)))
        for i in validation_arr:
            if i != nums[i]:
                return i
        return validation_arr[-1] + 1
```

O(nlogn) not optimal


## optimal solution

hashset 


```python
class Solution:
    def missingNumber(self, nums):
        num_set = set(nums)
        n = len(nums) + 1
        for number in range(n):
            if number not in num_set:
                return number
```