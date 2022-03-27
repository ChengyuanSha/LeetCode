
def maxSubArray(nums) -> int:
    max_cur = max_glob = nums[0]
    for i in range(1, len(nums)):
        max_cur = max(nums[i], max_cur + nums[i])
        if max_cur > max_glob:
            max_glob = max_cur
    return max_glob


print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))