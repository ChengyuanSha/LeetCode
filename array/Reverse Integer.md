
## my solution

```python
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = 1
        if x < 0:
            sign = -1
            x = abs(x)
        result = sign * int(str(x)[::-1])
        if result < -math.pow(2, 31) or result > math.pow(2, 31):
            return 0
        else:
            return result
```


if cannot use str, then:

```python
//pop operation:
pop = x % 10;
x /= 10;

//push operation:
temp = rev * 10 + pop;
rev = temp;
```

