
## solution 

```python
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return None
        right = self.invertTree(root.right)
        left = self.invertTree(root.left)
        root.left = right 
        root.right = left 
        return root 
```