
## my solution 

two pointers 


```python
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        max_area = 0
        while right > left:
            if height[right] < height[left]: # right smaller 
                area = height[right] * (right - left )
                right -= 1
            else: # left smaller 
                area = height[left] * (right - left )
                left += 1
            # update max area 
            if area > max_area:
                max_area = area
        return max_area
```