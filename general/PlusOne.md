## My solution 

```python
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        reversed_list = digits[::-1]

        for c, i in enumerate(reversed_list):
            if i + 1 < 10:
                reversed_list[c] += 1
                carry = False
                break
            else:
                reversed_list[c] = 0
                carry = True
        if carry == True:
            reversed_list.append(1)
        return reversed_list[::-1]
```