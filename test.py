
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
        return letter_log + digit_log


S = Solution()
S.reorderLogFiles()