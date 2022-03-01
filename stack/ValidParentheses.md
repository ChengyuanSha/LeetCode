## My solution 

```python
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        complement = {'(':')', '[':']', '{': '}' } 
        for i in s:
            if stack != [] and stack[-1] in complement and complement[stack[-1]] == i:
                stack.pop()
            else:
                stack.append(i)
        return stack==[]
```

通过但是经过几次修改，edge case 注意要检测 `stack[-1] in complement`
