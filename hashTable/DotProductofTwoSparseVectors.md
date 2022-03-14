
## my solution 

```python
class SparseVector:
    def __init__(self, nums: List[int]):
        self.nums = { i : x for i, x in enumerate(nums) if x != 0}
        
    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        output = 0
        for k in self.nums:
            if k in vec.nums:
                output += self.nums[k] * vec.nums[k]
        return output 
```

## improvement

slightly optimize version, Instead of traversing the hash maps of the first vector, choose the one with minimum length

```python
class SparseVector:
    def __init__(self, nums: List[int]):
        self.nums = { i : x for i, x in enumerate(nums) if x != 0}
        
    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        output = 0
        if len(self.nums) < len(vec.nums):
            min_num = self.nums
            other_num = vec.nums
        else:
            min_num = vec.nums
            other_num = self.nums
            
        for k in min_num:
            if k in other_num:
                output += self.nums[k] * vec.nums[k]
        return output 
```

还有一种Index-Value Pairs 的方法可以看看

https://leetcode.com/problems/dot-product-of-two-sparse-vectors/solution/
