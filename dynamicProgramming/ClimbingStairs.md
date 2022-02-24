## My solution 

Time limit exceeded   
only recursion, did not think of memorization  
```python
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 1 
        if n == 1:
            return 1
        return self.climbStairs(n-1) + self.climbStairs(n-2)
```


## Solution

DP with recursion

```python
class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [0] * (n+1)
        return self.climb(0, n, memo)
        
        
    def climb(self, i, n, memo):
        if i > n:
            return 0
        if i == n:
            return 1
        if memo[i] > 0:
            return memo[i]
        memo[i] = self.climb(i+1, n, memo) + self.climb(i+2, n, memo)
        return memo[i]
        
```

DP without recursion, bottom up  

```python
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1: 
            return 1
        dp = [0] * (n+1)
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]
```



