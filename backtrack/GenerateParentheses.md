完全不会

## Solution

```python
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # only add open parenthesis when openN > n
        # only add close parenthesis when closeN < openN
        # valid when openN == closeN == N
        stack = []
        res = []
        
        def generate(openN, closeN):
            if openN == closeN == n:
                res.append("".join(stack))
                return
            if openN < n:
                stack.append("(")
                generate(openN + 1, closeN)
                stack.pop()
            if closeN < openN:
                stack.append(")")
                generate(openN, closeN + 1)
                stack.pop()
            
        generate(0, 0)
        
        return res
```