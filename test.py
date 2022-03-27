
def maxSubArray(nums) -> int:
    max_cur = max_glob = nums[0]
    start_index = end_index = start_index_glob = 0
    for i in range(1, len(nums)):

        if nums[i] > max_cur + nums[i]:
            max_cur = nums[i]
            start_index = i
        if nums[i] < max_cur + nums[i]:
            max_cur = max_cur + nums[i]
        if max_cur > max_glob:
            max_glob = max_cur
            end_index = i
            start_index_glob = start_index
    return nums[start_index_glob:end_index+1] # last index is not included in slicing


print(maxSubArray([5,4,-1,7,8]))