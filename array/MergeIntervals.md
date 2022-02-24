## My solution 

思路很接近， 逻辑差一点没写出来 :cry: 
```python
## fail， cannot pass all tests
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        new_intervals = []
        intervals.sort(key=lambda x : x[0])
        if len(intervals) == 1:
            return intervals
        for i in range(1, len(intervals)):
            if intervals[i][0] <= intervals[i-1][1]:
                new_intervals.append([min(intervals[i-1][0], intervals[i][0]) , max(intervals[i][1], intervals[i-1][1]) ])
            elif i == 1:
                new_intervals.append(intervals[0])
                new_intervals.append(intervals[i])
            else:
                new_intervals.append(intervals[i])

        return new_intervals
```

## Improvements
思路一样， 逻辑改一下
```python
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merged = []
        intervals.sort(key=lambda x : x[0])
        for interval in intervals:
            # if empty or does not overlap
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else: # merge the current and previous one
                merged[-1][1] = max(merged[-1][1], interval[1])
        return merged
```

