## My solution 


```python
class Logger:

    def __init__(self):
        self.log_record = {}
        

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if (message in self.log_record) and (timestamp < self.log_record[message]):
            return False
        else:
            self.log_record[message] = timestamp + 10
            return True
```