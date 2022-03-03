## my solution 

```python
class Solution:
    def isHappy(self, n: int) -> bool:
        num_seen = set()
        while True:
            num_sum = 0
            for i in str(n):
                num_sum = num_sum + int(i) ** 2
            if num_sum in num_seen:
                return False
            if num_sum == 1:
                return True
            num_seen.add(num_sum)
            n = num_sum
```


## more elegant solution

```python
def isHappy(self, n):
        seen = set()
        while n not in seen:
            seen.add(n)
            n = sum([int(x) ** 2 for x in str(n)])
        return n == 1
```

