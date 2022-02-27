## My solution 

通过，是modify inplace的
```python
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i, j = 0, 1
        cur = nums[0]
        count = 0
        while j < len(nums):
            if cur == nums[j]: # duplicate
                count += 1
                del nums[j]
            else:
                cur = nums[j]
                j += 1
```


## Improvements

更好一点的逻辑：

```python
x = 1
for i in range(len(nums)-1):
	if(nums[i]!=nums[i+1]):
		nums[x] = nums[i+1]
		x+=1
return(x)
```