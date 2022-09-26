
## my solution 


```python
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ans = ListNode(0)
        head = ans
        carry = 0
        while l1 or l2:
            if l1 and l2:
                num = l1.val + l2.val
                l1 = l1.next
                l2 = l2.next
            elif l1 and not l2:
                num = l1.val 
                l1 = l1.next
            elif l2 and not l1:
                num = l2.val
                l2 = l2.next
            if carry == 1:
                num += 1
                carry = 0
            if num >= 10:
                carry = 1
                num -= 10
                
            node = ListNode(num)
            head.next = node
            head = head.next
        
        if carry == 1:
            node = ListNode(1)
            head.next = node
            head = head.next
            
        return ans.next 
```



