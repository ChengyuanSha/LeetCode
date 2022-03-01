## My solution

做出来了，就是有点慢

```python
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        min_diff = 9223372036854775807
        ans = []
        for i in range(1, len(arr)):
            if arr[i] - arr[i-1] == min_diff:
                ans.append([arr[i-1], arr[i]])
            if arr[i] - arr[i-1] < min_diff: 
                ans = []
                ans.append([arr[i-1], arr[i]])
                min_diff = arr[i] - arr[i-1]

        return ans
```