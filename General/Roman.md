
My solution:
```python
class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        i = 0
        num = 0
        while i < len(s):
            special = False
            if (i+1) < len(s):
                if s[i] == "I" and s[i+1] == "V":
                    num += 4
                    special = True
                if s[i] == "I" and s[i+1] == "X":
                    num += 9
                    special = True
                if s[i] == "X" and s[i+1] == "L":
                    num += 40
                    special = True
                if s[i] == "X" and s[i+1] == "C":
                    num += 90
                    special = True
                if s[i] == "C" and s[i+1] == "D":
                    num += 400
                    special = True
                if s[i] == "C" and s[i+1] == "M":
                    num += 900
                    special = True
                if special == True:
                    i += 2
            if i < len(s) and special == False:
                num += dic[s[i]]
                i += 1
        
        return num
```

Could Improve:  

```python
class Solution:
# @param {string} s
# @return {integer}
def romanToInt(self, s):
    roman = {'M': 1000,'D': 500 ,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1}
    z = 0
    for i in range(0, len(s) - 1):
        if roman[s[i]] < roman[s[i+1]]:
            z -= roman[s[i]]
        else:
            z += roman[s[i]]
    return z + roman[s[-1]]
```

找小于的规律就不需要把每一种特殊情况列出来   
The trick is that the last letter is always added. Except the last one, if one letter is less than its latter one, this letter is subtracted.
