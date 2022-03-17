
## my solution 
brute force 

```python
import numpy as np

class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        win = {'A': np.array(['X','X', 'X']), 'B': np.array(['O', 'O', 'O'])}
        grid = np.zeros((3,3), dtype=str)
        for i, x in enumerate(moves):
            if i % 2 == 0: # A 
                grid[x[0], x[1]] = 'X'
            else:
                grid[x[0], x[1]] = 'O'
        if (np.fliplr(grid).diagonal() == win['A']).all() or (grid.diagonal() == win['A']).all():
            return "A"
        if (np.fliplr(grid).diagonal() == win['B']).all() or (grid.diagonal() == win['B']).all():   
            return "B"
        for r in range(3):
            if (grid[:, r] == win['A']).all() or (grid[r, :] == win['A']).all(): 
                return "A"
            if (grid[:, r] == win['B']).all() or (grid[r, :] == win['B']).all():
                return "B"
        if len(moves) == 9: 
            return "Draw"
        else:
            return "Pending"
```



## improvement 

单独记录row, column, diagonal 

https://leetcode.com/problems/find-winner-on-a-tic-tac-toe-game/solution/

