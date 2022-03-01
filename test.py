import re


def longestValidParentheses(s):
    """
    :type s: str
    :rtype: int
    """
    stack = [0]
    longest = 0

    for c in s:
        if c == "(":
            stack.append(0)
        else:
            if len(stack) > 1:
                val = stack.pop()
                stack[-1] += val + 2
                longest = max(longest, stack[-1])
            else:
                stack = [0]

    return longest


print(longestValidParentheses(')()())'))