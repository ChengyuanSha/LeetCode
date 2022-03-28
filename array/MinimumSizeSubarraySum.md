
## my solution

did this question as I learned sliding window technique

```python
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i = 0 # left
        j = 0 # right
        len_glob = float('inf')
        cur_sum = 0
        while j < len(nums):
            cur_sum += nums[j]

            while cur_sum >= target:
                len_glob = min(len_glob, j - i + 1)
                if len_glob == 1:  # terminate early
                    return len_glob
                cur_sum -= nums[i]
                i += 1

            j += 1


        return 0 if len_glob == float('inf') else len_glob
```


