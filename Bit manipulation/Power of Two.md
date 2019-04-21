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
```
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
