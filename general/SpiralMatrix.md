一开始有思路但是implement不出来  

 There are only two movement patterns, `right+down` and `left+up`。 In the first case we increment either the row or column by `1`, and in the latter case we increment either the row or column by `-1`
```python
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        i, j = 0, -1 
        m, n = len(matrix), len(matrix[0])
        direction = 1
        output = []
        while m * n > 0:
            for _ in range(n): # going horizontal 
                j += direction 
                output.append(matrix[i][j])
            m -= 1 # move row boundary 
            for _ in range(m): # going vertical 
                i += direction 
                output.append(matrix[i][j])
            n -= 1 # move col boundary 
            direction *= -1
        return output 
```

