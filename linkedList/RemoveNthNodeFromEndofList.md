
## my solution 

Two pass
```python
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # one pass find length 
        temp = head 
        length = 0
        while temp:
            temp = temp.next
            length += 1
        remove_pos = length - n
        # another pass remove node 
        temp = head 
        count = 0
        if remove_pos == 0: # special case head
            head = head.next 
            return head 
        while temp:
            if count == (remove_pos-1):
                temp.next = temp.next.next
                return head 
            temp = temp.next
            count += 1
```

Improvement:

use two pointers that are `n+1` step apart 



