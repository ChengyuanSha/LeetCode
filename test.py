import re


def longestCommonPrefix(strs) -> str:
   common_prefix = []
   i = 1
   while i <= len(strs[0]):
      j = 0
      prefix = strs[0][0:i]
      i += 1
      for c, i in enumerate(strs):
         if i.startswith(prefix):
            j += 1
         if j == len(strs) - 1:
            common_prefix.append(prefix)
   if common_prefix != []:
      return max(common_prefix, key=len)
   else:
      return ""

longestCommonPrefix(["flower","flow","flight"])