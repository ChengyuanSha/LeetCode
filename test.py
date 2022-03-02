import re


def validPalindrome( s: str) -> bool:
    for i in s:
        newstr = s.replace(i, "")
        if newstr == newstr[::-1]:
            return True
    return False


print(validPalindrome("pidbliassaqozokmtgahluruufwbjdtayuhbxwoicviygilgzduudzgligyviciowxbhuyatdjbwfuurulhagtmkozoqassailbdip"))