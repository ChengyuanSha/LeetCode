一开始不知道题目目的， 看了思路是Binary search后写
```python
class Solution:
    def mySqrt(self, x: int) -> int:
        low, high = 0, x
        while high >= low:
            mid = int(low + (high - low) / 2)
            power = mid * mid
            if power > x:
                high = mid - 1
            elif power < x:
                low = mid + 1
            else:  #  == x 
                return mid
        # When there is no perfect square, hi is the value on the left
        # of where it would have been (rounding down). If we were rounding up, 
        # we would return lo
        return high

```

python int() cast or "//" is truncation


也有newton数学解法