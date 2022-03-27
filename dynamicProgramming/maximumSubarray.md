## First Try

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


## Second Try

```python
max(nums[i], max_current + nums[i])
```

这里写错了，要注意是`nums[i]`和`max_current + nums[i]`比较， 如果是负数cur就会被set成`nums[i]`

## Other Variants

### Produce the maximum subarray:

```python
def maxSubArray(nums) -> int:
    max_cur = max_glob = nums[0]
    start_index = end_index = start_index_glob = 0
    for i in range(1, len(nums)):
        if nums[i] > max_cur + nums[i]:
            max_cur = nums[i]
            start_index = i
        if nums[i] < max_cur + nums[i]:
            max_cur = max_cur + nums[i]
        if max_cur > max_glob:
            max_glob = max_cur
            end_index = i
            start_index_glob = start_index
    return nums[start_index_glob:end_index+1] # last index is not included in slicing
```