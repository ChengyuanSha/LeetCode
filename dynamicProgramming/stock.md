## My solution
第一次思路：
```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_index = prices.index(min(prices))
        if min_index == len(prices) - 1:
            return 0
        max_index = prices.index(max(prices[min_index:]))
        return prices[max_index] - prices[min_index]
```
忽略了 [2,4,1] 的情况

第二次思路：
```python
import numpy as np

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sorted_index = np.argsort(prices) # ascending 
        profit = []
        for i in sorted_index:
            if i != len(prices) - 1:
                max_index = prices.index(max(prices[i:]))
                profit.append(prices[max_index] - prices[i])
        if profit != []:
            return max(profit)
        else:
            return 0
```
复杂度太高

## Improvements

### one pass
The points of interest are the peaks and valleys in the given graph. We need to find the largest peak following the smallest valley. 
We can maintain two variables - minprice and maxprofit corresponding to the smallest valley and maximum profit 
(maximum difference between selling price and minprice) obtained so far respectively.

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0
        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            elif prices[i] - min_price > max_profit:
                max_profit = prices[i] - min_price
                
        return max_profit
```

### 用DP：

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_cur, max_so_far = 0, 0
        for i in range(1, len(prices)):
            max_cur = max(0, max_cur + prices[i] - prices[i-1])
            max_so_far = max(max_cur, max_so_far)
        return max_so_far
```



