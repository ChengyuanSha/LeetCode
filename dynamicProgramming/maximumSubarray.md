一开始除了找所有的subarray没思路， 后面看了Kadane's Algorithm， O(n)
思路：记录subarray，比如在中间的一个index的时候，前面的max sum已经有了， 需要考虑的只是比较 `前面的max sum`和 `前面的max sum`+`现在的`.
```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_current = max_global = nums[0]
        for i in range(1, len(nums)):
            max_current = max(nums[i], max_current + nums[i])
            if max_current > max_global:
                max_global = max_current
        return max_global
```


