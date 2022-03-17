
## my solution 

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        
        while low <= high:
            goal = (low + high) // 2
            if nums[goal] < target:
                low = goal + 1
            elif nums[goal] > target:
                high = goal - 1
            else: # equal
                return goal
        return -1 
```




