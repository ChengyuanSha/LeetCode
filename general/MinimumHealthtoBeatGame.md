
## my solution 
```python
class Solution(object):
    def minimumHealth(self, damage, armor):
        """
        :type damage: List[int]
        :type armor: int
        :rtype: int
        """
        max_damage_idx = damage.index(max(damage))
        health = 1
        for i, x in enumerate(damage):
            if i == max_damage_idx:
                x = x - armor 
                x = 0 if x < 0 else x
            health += x
        return health
```


## more elegant solution

```python
class Solution:
    def minimumHealth(self, damage: List[int], armor: int) -> int:
        return 1 + sum(damage) - min(max(damage), armor)
```


