

## my answer 

after checking ans online


```python
class Solution(object):
    def clumsy(self, n):
        """
        :type n: int
        :rtype: int
        """
        sign = 1
        ans = []
        while n >= 1:
            cur = n
            if n-1 >= 1:
                cur *= (n-1)
            if n-2 >= 1:
                cur /= (n-2)
            cur *= sign
            if n-3 >=1:
                cur += (n-3)
            sign = -1
            n -= 4
            ans.append(cur)
        return sum(ans) 
```

key idea:
divide factorial into 4 groups, treat minus as sign, calculate the result in each group and finally sum together.

