## My solution 
Using stack   
几个点在写的时候遗漏了：1. list是odd的情况， 2.只有单个element的情况
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head.next == None: # len 1 list
            return True
        
        length = 0
        temp = head
        while temp:
            length += 1
            temp = temp.next
        odd = (length % 2 != 0)
        if odd: # odd
            mid = (length - 1) // 2 
        else:
            mid = length // 2
        
        cur = 0
        stack = []
        
        # loop to mid
        while cur < mid:
            stack.append(head.val)
            head = head.next
            cur += 1
            
        if odd != 0: # odd, skip mid
            head = head.next
            cur += 1
            
        # loop to end
        while cur < length:
            if stack[-1] == head.val:
                stack.pop()
            cur += 1
            head = head.next
        
        return stack == []
```




