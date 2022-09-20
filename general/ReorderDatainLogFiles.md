
My solution

very close, original solution missing `letter_log.sort(key = lambda x: x.split()[0]) ` part
```
class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        letter_log = []
        digit_log = []
        for x in logs:
            logs = x.split()
            if "".join(logs[1:]).isalpha(): # letter log
                letter_log.append(x)
            else: # digit log
                digit_log.append(x)
        
        letter_log.sort(key = lambda x: x.split()[0]) # when suffix is tie, sort by identifier   
        letter_log.sort(key = lambda x: x.split()[1:]) # sort by identifier

        return letter_log + digit_log
```