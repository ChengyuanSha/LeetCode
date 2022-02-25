## My solution 

dictionary + sort, O(nlogn)
```python
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for i in nums:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1

        result = []
        for c, w in enumerate(sorted(count, key=count.get, reverse=True)):
            if c >= k:
                break
            else:
                result.append(w)
        return result
        
```


##  Improvements

O(n logk), 用heapq替代后面的sort
```python
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]: 
        # O(1) time 
        if k == len(nums):
            return nums
        
        # 1. build hash map : character and how often it appears
        # O(N) time
        count = Counter(nums)   
        # 2-3. build heap of top k frequent elements and
        # convert it into an output array
        # O(N log k) time
        return heapq.nlargest(k, count.keys(), key=count.get) 
```




