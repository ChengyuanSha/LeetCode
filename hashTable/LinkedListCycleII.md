

## My hash set solution

just same as problem version 1:

```python

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        record = set()
        while head:
            if head in record:
                return head
            record.add(head)
            head = head.next
        return None
```



## slow & fast pointers

https://www.youtube.com/watch?v=9YTjXqqJEFE&ab_channel=JomaClass

