
## My solution
```python
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        self.helper(root, output)
        return output
        
        
    def helper(self, node, output):
        if node:
            self.helper(node.left, output)
            output.append(node.val)
            self.helper(node.right, output)
```


## Improvement

看一下 iterative

```python
def inorderTraversal(self, root):
    ans = []
    stack = []
    
    while stack or root:
        if root:
            stack.append(root)
            root = root.left
        else:
            tmpNode = stack.pop()
            ans.append(tmpNode.val)
            root = tmpNode.right
        
    return ans
```


