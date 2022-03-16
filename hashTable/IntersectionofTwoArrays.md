
## My solution

```python
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return set(nums1).intersection(set(nums2))
```


## More to consider 

**Variation**
if the lists are already sorted and you're told to solve in O(n) time and O(1) space:

```python
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]: 
        nums1.sort()
        nums2.sort()
        result = []

        while nums1 and nums2:
            if nums2[-1] > nums1[-1]:
                nums2.pop()
            elif nums2[-1] < nums1[-1]:
                nums1.pop()
            else:
                # to avoid duplicates
                if not result or nums1[-1] != result[-1]:
                    result.append(nums1[-1])
                nums1.pop()
                nums2.pop()

        return result
```

