
双指针滑动窗口的经典写法。右指针不断往右移，移动到不能往右移动为止(具体条件根据题目而定)。当右指针到最右边以后，开始挪动左指针，释放窗口左边界

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        max_length = 0
        record = {}
        for c, i in enumerate(s):
            if i in record and start <= record[i]:
                start = record[i] + 1
            else:
                max_length = max(max_length, c - start + 1)
            record[i] = c 
        return max_length
```