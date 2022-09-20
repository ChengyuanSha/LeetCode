## my solution 

```python
class Solution(object):
    def suggestedProducts(self, products, searchWord):
        """
        :type products: List[str]
        :type searchWord: str
        :rtype: List[List[str]]
        """
        result = []
        products = sorted(products)
        prefix = ""
        for w in searchWord:
            prefix += w
            current_product = [i for i in products if i.startswith(prefix)]
            if len(current_product) > 3:
                result.append(current_product[:3])
            else:
                result.append(current_product)
        return result 
            
```


## Improvement 


can turn the "search for prefix" in the middle into a binary search 


