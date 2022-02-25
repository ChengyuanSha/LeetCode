## My solution

```python
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = [0] * n
        while n > 0:
            if n % 3 == 0 and n % 5 == 0:
                answer[n-1] = "FizzBuzz"
            elif n % 3 == 0:
                answer[n-1] = "Fizz"
            elif n % 5 == 0:
                answer[n-1] = "Buzz"
            else:
                answer[n-1] = str(n)
            n -= 1
        return answer 
```
