my solution, time exceed, logic too complicated

```python
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        positive_pointer = None
        for i, x in enumerate(nums): # first positive
            if x >= 0 and not positive_pointer:
                positive_pointer = i
            nums[i] = nums[i] ** 2
            
        move_pointer = 0
        if not positive_pointer: # all negative 
            return nums[::-1]
        else:
            while positive_pointer - move_pointer:
                i = positive_pointer
                while i < len(nums) and nums[i] < nums[move_pointer]:
                    i += 1
                nums.insert(i, nums[move_pointer])
                move_pointer += 1
            return nums[positive_pointer:]
```


Better solution: Two pointers

retry success

```python
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = []
        i = 0 # left
        j = len(nums) - 1 # right
        while i <= j:
            if abs(nums[i]) < abs(nums[j]):
                result.append(nums[j]**2)
                j -= 1
            else: # >=
                result.append(nums[i]**2)
                i += 1
        return result[::-1]
```
