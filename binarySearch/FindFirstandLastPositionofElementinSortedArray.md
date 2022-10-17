## my solution 


```python
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if nums == []:
            return [-1, -1]
        
        low, high = 0, len(nums)
        target_position = -1
        while low <= high:
            mid = (high + low) / 2
            print(mid)
            if mid < 0 or mid >= len(nums):
                return [-1, -1]
            elif nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                target_position = mid
                break

        if target_position == -1:
            return [-1, -1]
        
        print(target_position)
        position = target_position
        start_idx = position 
        end_idx = position 
        while position - 1 >= 0:
            position -= 1
            if nums[position] == target:
                start_idx = position 
        
        position = target_position
        while position + 1 < len(nums) and nums[position] == target:
            position += 1
            if nums[position] == target:
                end_idx = position 
        
        return [start_idx, end_idx]
```



## Improvement 


```python
def searchRange(self, nums, target):
    def binarySearchLeft(A, x):
        left, right = 0, len(A) - 1
        while left <= right:
            mid = (left + right) / 2
            if x > A[mid]: left = mid + 1
            else: right = mid - 1
        return left

    def binarySearchRight(A, x):
        left, right = 0, len(A) - 1
        while left <= right:
            mid = (left + right) / 2
            if x >= A[mid]: left = mid + 1
            else: right = mid - 1
        return right
        
    left, right = binarySearchLeft(nums, target), binarySearchRight(nums, target)
    return (left, right) if left <= right else [-1, -1]
```


Two binary search