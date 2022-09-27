
## my solution 

```python
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        def isMirror(n1, n2):
            if n1 == None and n2 == None:
                return True
            if n1 == None or n2 == None:
                return False
            return (n1.val == n2.val) and isMirror(n1.right, n2.left) and isMirror(n1.left, n2.right) 
        
        return isMirror(root.left, root.right)
```