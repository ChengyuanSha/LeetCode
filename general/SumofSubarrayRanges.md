
## My solution

brute force O(n^3)

two loops O(n^2)

```python
class Solution(object):
    def subArrayRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        
        for i in range(len(nums)):
            r, l = nums[i], nums[i]
            for j in range(i, len(nums)):
                l = min(l, nums[j])
                r = max(r, nums[j])
                result += (r - l)
        
        return result
```


There is a O(n) solution, too difficult to understand 

