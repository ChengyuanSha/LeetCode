## my solution

```python
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        count = {}
        for i in nums:
            if i in count:
                count[i] += 1
                if count[i] > len(nums) / 2:
                    return i
            else:
                count[i] = 1
```


## Improvement, Boyer-Moore Voting Algorithm

O(1) space complexity 

核心就是对拼消耗。玩一个诸侯争霸的游戏，假设你方人口超过总人口一半以上，并且能保证每个人口出去干仗都能一对一同归于尽。
最后还有人活下来的国家就是胜利。那就大混战呗，最差所有人都联合起来对付你（对应你每次选择作为计数器的数都是众数），
或者其他国家也会相互攻击（会选择其他数作为计数器的数），但是只要你们不要内斗，最后肯定你赢。最后能剩下的必定是自己人。



https://www.zhihu.com/question/49973163/answer/235921864

```python
class Solution:
    def majorityElement(self, nums):
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate
```