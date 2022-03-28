## My solution

did this question as I learned sliding window technique

```python
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        i = 0 # left
        j = 0 # right
        count = {}
        longest_substring = 0
        while j < len(s):
            if s[j] in count:
                count[s[j]] += 1
            else:
                count[s[j]] = 1
            while len(count) > k: # shrink
                count[s[i]] -= 1
                if count[s[i]] == 0:
                    del count[s[i]]
                i += 1
            longest_substring = max(longest_substring, j - i + 1)
            j += 1
        return longest_substring
```