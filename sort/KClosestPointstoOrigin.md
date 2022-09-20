## My solution

```python
import math 
import numpy as np

class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
                
        def euclidean(x1, y1):
            return math.sqrt(math.pow(x1, 2) + math.pow(y1, 2))
        
        distance_list = [euclidean(i[0], i[1]) for i in points]
        sorted_idx = np.argsort(distance_list)
        return np.array(points)[sorted_idx[:k]]
```


