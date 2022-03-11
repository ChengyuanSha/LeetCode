

## my solution 

```python
from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}
        count_list = [Counter(i) for i in strs]
        
        
        for i, x in enumerate(strs):
            # check the anagram already exist in the result
            exist = False
            for j in result:
                if count_list[j] == count_list[i]:
                    result[j].append(x)
                    exist = True
            if not exist:
                result[i] = [x]
            
        return result.values()
```


## solution

1. 我上面的思路`找exist`这里答案用defaultdict高效实现了.

2. Two strings are anagrams if and only if their sorted strings are equal.
除了比较counter也可以比较sorted strings

```python
from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)
        for s in strs:
            ans[tuple(sorted(Counter(s).items()))].append(s)
        return ans.values()
```

