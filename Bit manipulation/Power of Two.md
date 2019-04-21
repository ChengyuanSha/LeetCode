**231. Power of Two**

Given an integer, write a function to determine if it is a power of two.

Example 1:

Input: 1
Output: true 
Explanation: 20 = 1
Example 2:

Input: 16
Output: true
Explanation: 24 = 16
Example 3:

Input: 218
Output: false

最开始的想法: 用recursion
```python
class Solution:
    def isPowerOfTwo(self, n) -> bool:
        if n != int(n): # not whole number
            return False
        if n == 1 or n == 2:
            return True
        elif n > 2:  # 这里注意很重要
            return self.isPowerOfTwo(n/2)
        else:
            return False  
```
Time complexity = O(log n)

看了discussion, 知道了bit的技巧:
**bit operation**

If n is the power of two:
```
n = 2 ^ 0 = 1 = 0b0000...00000001, and (n - 1) = 0 = 0b0000...0000.
n = 2 ^ 1 = 2 = 0b0000...00000010, and (n - 1) = 1 = 0b0000...0001.
n = 2 ^ 2 = 4 = 0b0000...00000100, and (n - 1) = 3 = 0b0000...0011.
n = 2 ^ 3 = 8 = 0b0000...00001000, and (n - 1) = 7 = 0b0000...0111.
```
we have n & (n-1) == 0b0000...0000 == 0

Otherwise, n & (n-1) != 0.

For example, n =14 = 0b0000...1110, and (n - 1) = 13 = 0b0000...1101.

```python
class Solution:
    def isPowerOfTwo(self, n) -> bool:
        return n > 0 and ((n & (n-1) == 0))   
```
