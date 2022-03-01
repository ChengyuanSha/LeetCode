想不出来


## DP

| i   | 0   | 1   | 2   | 3   | 4   | 5   |     |
|-----|-----|-----|-----|-----|-----|-----|-----|
| s   | )   | (   | )   | (   | )   | )   |     |
| dp  | 0   | 0   | 2   | 0   | 4   | 0   |     |



```python
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s: # empty 
            return 0
        
        stack = []
        dp = [0]*len(s)
        
        for i in range(len(s)):
            if s[i]=='(':
                stack.append(i)              
            else:
                if stack:
                    leftIndex = stack.pop()
                    dp[i] = i-leftIndex+1+dp[leftIndex-1]
                
        return max(dp)
        
```


## stack


```python
class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = [0]
        longest = 0
        
        for c in s:
            if c == "(":
                stack.append(0)
            else:
                if len(stack) > 1:
                    val = stack.pop()
                    stack[-1] += val + 2
                    longest = max(longest, stack[-1])
                else:
                    stack = [0]

        return longest
```