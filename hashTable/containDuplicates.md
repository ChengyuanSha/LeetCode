## My solution
我的解法， 用hashtable记录， 通过
```python
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        record = {}
        for i in nums:
            if i in record:
                record[i] += 1
                if record[i] >= 2:
                    return True
            record[i] = 1
        return False
```

## Other angle
一行写完， 比较set的长度
```python
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(nums) != len(set(nums))
```
