## my solution

The idea is straightforward :

Move a sliding window of length L along the string of length N.

Check if the sequence in the sliding window is in the hashset of already seen sequences.

If yes, the repeated sequence is right here. Update the output.

If not, save the sequence in the sliding window in the hashset.


```python
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        
        seen = {}
        repeated = []

        for c, i in enumerate(s):
            if c + 10 <= len(s):
                DNA = s[c:c+10]
                if DNA in seen and seen[DNA] == 1:
                    seen[DNA] += 1
                    repeated.append(DNA)
                if DNA not in seen:
                    seen[DNA] = 1
                
        return repeated
```

