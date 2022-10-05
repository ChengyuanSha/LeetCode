

## my solution 

```python
class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        ans = {}
        for domain in cpdomains:
            num, dom = domain.split(' ')
            
            sub_dom = dom.split('.')
        
            for i in range(len(sub_dom)):
                name = ".".join(sub_dom[i:len(sub_dom)])
                if name in ans:
                    ans[name] = ans[name] + int(num)
                else:
                    ans[name] = int(num)
        # convert to list format 
        return [str(val) + " " + key for key, val in ans.items()]
```