## Sliding window

### Tips of recognizing these problems:
* Things we iterate over sequentially 
  * contiguous sequence of elements
  * Strings, arrays, linked list
* min, max, longest, shortest, contained
  * maybe we need to calculate something 

    
## Common problems:

### Maximum sum subarray of size `K` (**Fixed Length Variants**)

Given an array of integers and a number k, find the maximum sum of a subarray of size k. 

O(n)

```python
# n is optional here
def maxSum(arr, n, k):
    i = 0
    j = i + k
    sum_glob = 0
    while j <= n:
        sum_cur = sum([arr[i] for i in range(i, j)])
        sum_glob = max(sum_cur, sum_glob)
        i += 1
        j += 1
    return sum_glob

arr = [1, 4, 2, 10, 2, 3, 1, 0, 20]
k = 4
n = len(arr)
print(maxSum(arr, n, k))
```


### smallest subarray with given sum >= to some value `S` (**Dynamic Length Variants**)

[Leetcode 209](../array/MinimumSizeSubarraySum.md)

```python
from typing import List

def minSubArrayLen(target: int, nums: List[int]) -> int:
    i = 0 # left
    j = 0 # right
    len_glob = float('inf')
    cur_sum = 0
    while j < len(nums):
        cur_sum += nums[j]
        while cur_sum >= target:
            len_glob = min(len_glob, j - i + 1)
            if len_glob == 1:  # terminate early
                return len_glob
            cur_sum -= nums[i]
            i += 1
        j += 1

    return 0 if len_glob == float('inf') else len_glob
```


### Longest substring length with `k` distinct characters (**Dynamic Length Variants with auxiliary data structure**)

[Leetcode 340](../array/LongestSubstringAtMostKDistinctChar.md)   

```python
def lengthOfLongestSubstringKDistinct(s: str, k: int) -> int:
    i = 0 # left
    j = 0 # right
    count = {}
    longest_substring = 0
    while j < len(s):
        # record unique key count in a hashtable
        if s[j] in count:
            count[s[j]] += 1
        else:
            count[s[j]] = 1
        while len(count) > k: # shrink left when violation
            count[s[i]] -= 1
            if count[s[i]] == 0:
                del count[s[i]]
            i += 1
        longest_substring = max(longest_substring, j - i + 1)
        j += 1
    return longest_substring

s = "eceba"
k = 2
print(lengthOfLongestSubstringKDistinct(s, k))
```


### String Permutations 




### Reference

* https://www.youtube.com/watch?v=MK-NZ4hN7rs&ab_channel=RyanSchachte

