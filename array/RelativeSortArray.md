## my solutions 

```python
class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        
        ans = []
        
        for i in arr2:
            for j in arr1:
                if j == i:
                    ans.append(j)
            
        rest = sorted([x for x in arr1 if x not in arr2])
        
        ans += rest 
        
        return ans
```
O(n^2)

## Improvements

O(n)

use `dictionary` to count occurrence
use `diff` to record difference 

only 1 pass needed

num * occurrence + sorted(other_num)

