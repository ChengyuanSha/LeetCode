一开始没想明白condition
没想到用`flowerbed[i] = 1`
greedy是来做早点停的

```python
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowerable = 0
        
        num_zero = 0
        for i, x in enumerate(flowerbed):
            if x == 0:
                left = (i==0) or (flowerbed[i-1]==0)
                right = (i==len(flowerbed)-1) or (flowerbed[i+1]==0)
                if left and right:
                    flowerbed[i] = 1
                    flowerable += 1
                    if flowerable >= n:
                        return True
        return flowerable >= n
    
```