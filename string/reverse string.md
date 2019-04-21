**344.reverse string**

Write a function that reverses a string. The input string is given as an array of characters char[].

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

You may assume all the characters consist of printable ascii characters.

```
Example 1:

Input: ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

Example 2:

Input: ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
```

最开始写的:
```python
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        maxIndex = len(s) - 1
        n = 0
        while (n != maxIndex and maxIndex > n):
            s[n], s[maxIndex] = s[maxIndex], s[n]
            n += 1
            maxIndex -= 1
```
做了一点小的改进, 去掉啰嗦部分:
```python
        n, maxIndex = 0, len(s)-1

        while maxIndex > n:
            s[n], s[maxIndex] = s[maxIndex], s[n]
            n += 1
            maxIndex -= 1
```
