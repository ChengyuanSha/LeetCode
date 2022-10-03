class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        def helper(h, n, target):
            # if target is too small or if it is out of range
            if target <= 0 or target > (n * k):
                return 0
            if n == 1:
                return 1  # no need to check if target is within reach; already done before
            if (n, target) in h:
                return h[(n, target)]  # directly access from hash table
            res = 0
            for i in range(1, k + 1):
                res += helper(h, n - 1, target - i)  # check all possible combinations
            h[(n, target)] = res
            return h[(n, target)]

        h = {}
        return helper(h, n, target) % (10 ** 9 + 7)