
## my solution 

O(n) timeout 

```python
class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        
        for i, x in enumerate(gas):
            
            start = i
            cur_gas = gas[start]
            while cur_gas >= cost[start]:
                print(cur_gas)
                cur_gas = cur_gas - cost[start] 
                start += 1   
                start = start % len(gas)
                cur_gas += gas[start] # add gas
                    
                if start % len(gas) == i: # back to original point
                    return start
        return -1
```


## optimal solution 


```python
class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        
        start = 0
        total_tank, curr_tank = 0, 0
        for i in range(len(gas)):
            total_tank += gas[i] - cost[i]
            curr_tank += gas[i] - cost[i]
            
            if curr_tank < 0:
                start = i + 1
                curr_tank = 0
        return start if total_tank >= 0 else -1
```


