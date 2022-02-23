## My solution:

one pass success 
```python
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key = lambda x : x[0])
        for c, i in enumerate(intervals):
            if c+1 < len(intervals) and intervals[c][1] > intervals[c+1][0]:
                return False
        return True
```

