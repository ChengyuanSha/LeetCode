

## my solution 

不知道给get也算用了一下, 后面看了思路理解透彻后写出：


```python
from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        self.LRU = OrderedDict() 
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.LRU:
            self.LRU.move_to_end(key, last=True) 
            return self.LRU[key]
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.LRU:
            self.LRU[key] = value
            self.LRU.move_to_end(key, last=True)  
        else: 
            if len(self.LRU) == self.capacity: # full
                self.LRU.popitem(last=False) # pop first
            self.LRU[key] = value          
```

