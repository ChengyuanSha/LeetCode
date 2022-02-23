## my solution 

想到了可以先merge再sort但是复杂度太高，要找O(n+m)的算法，想到了用pointer但是具体怎么实现不会  

看了three pointer思路写出来的：
```python
import copy

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if nums2 == []:
            return nums1
        p1, p2, p = 0, 0, 0
        nums1_copy = copy.deepcopy(nums1)
        while p < len(nums1):
            if  p2 >= n or (nums1_copy[p1] < nums2[p2] and p1 < m):
                nums1[p] = nums1_copy[p1] 
                p1 += 1
            else:
                nums1[p] = nums2[p2]
                p2 += 1
            p += 1
```
注意这个`p2 >= n `位置和存在很重要！可以防止例如nums2是空的情况 和 p2走完的情况


