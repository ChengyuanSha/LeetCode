## My solution 

```python
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 0:
            return False
        while n % 3 == 0:
            n /= 3 
        return n == 1
```


## Improvements 

Integer Limitations  O(1) 

https://leetcode.com/problems/power-of-three/solution/    

Works for any prime number  
```python
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return n > 0 & 1162261467 % n == 0
```
