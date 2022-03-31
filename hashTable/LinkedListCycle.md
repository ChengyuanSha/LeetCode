

I did not think of head can be stored directly in hashset


## hash set solution

```python
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        is_seen = set()
        while head:
            if head in is_seen:
                return True 
            is_seen.add(head)
            head = head.next
        return False
```

## fast & slow pointer solution 

```python
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head is None:
            return False
        slow = head
        fast = head.next
        while slow != fast:
            if fast is None or fast.next is None:
                return False
            slow = slow.next
            fast = fast.next.next
        return True
```