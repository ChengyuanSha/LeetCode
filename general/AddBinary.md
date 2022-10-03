
## my solution 

```python
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        
        if len(a) < len(b): # b larger
            max_length = len(b)
            len_diff = max_length - len(a)
            a = a.zfill(max_length)
        else: # a larger 
            max_length = len(a)
            len_diff = max_length - len(b)
            b = b.zfill(max_length)
            
        i = max_length - 1
        carry = False
        ans = []

        while i >= 0:
            print(i)
            if carry:
                num_sum = int(a[i]) + int(b[i]) + 1
            else:
                num_sum = int(a[i]) + int(b[i])
            
            if num_sum >= 2:
                carry = True
                num_sum -= 2
            else: 
                carry = False
                
            ans.append(str(num_sum))
                
            i -= 1
            
        if carry:
            ans.append("1")
            
        return "".join(ans[::-1])
            
```