## my solution 

```python
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        return str(x) == str(x)[::-1]
```



But if you cannot convert int to string 



```python
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x > 0 and x % 10 == 0):
            return False
        rev_int = 0
        while x > rev_int:
            rev_int = rev_int * 10 + x % 10
            
            x = x // 10
        return x == rev_int or x == rev_int // 10 
```