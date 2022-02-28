## My failed solution 

有重复的
```python
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        for c1, i in enumerate(nums):
            record = {}
            for c2, j in enumerate(nums[c1+1:]):
                if j in record.values():
                    answer = [i, j, 0-i-j]
                    if output != []: # check duplicates
                        duplicates = False
                        for k in output:
                            if i in k and j in k and 0-i-j in k and answer!=[0,0,0]:
                                duplicates = True
                        if not duplicates:
                            output.append(answer)
                    else: # empty output
                        output.append(answer)
                else:
                    record[j] = 0 - i - j
        return output
```


## Improvements

去除重复

https://leetcode.com/problems/3sum/solution/
