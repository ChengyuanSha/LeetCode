## My solution 

O(log n)

```python
import math

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        x = 0
        while int(math.pow(2, x)) <= n:
            if int(math.pow(2, x)) == n:
                return True
            x += 1
        return False
```


## improvements

**bit operations**:   
**key idea**: a power of two in binary representation is one 1-bit, followed by some zer
To subtract 1 means to change the rightmost 1-bit to 0 and to set all the lower bits to 1.
Now AND operator: the rightmost 1-bit will be turned off because 1 & 0 = 0, and all the lower bits as well.
```python
class Solution(object):
    def isPowerOfTwo(self, n):
        if n == 0:
            return False
        return n & (n - 1) == 0
```
