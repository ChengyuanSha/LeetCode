

有点不熟练， debug了几次
```python
class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        total_units = 0
        for i in boxTypes:
            if i[0] <= truckSize:
                total_units += i[0] * i[1]
                truckSize -= i[0]
            else:
                total_units = total_units + truckSize * i[1]
                return total_units
        return total_units
```