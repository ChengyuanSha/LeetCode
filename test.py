
from typing import List

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