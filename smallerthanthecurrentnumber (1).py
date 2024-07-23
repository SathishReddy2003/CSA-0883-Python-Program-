def smallerNumbersThanCurrent(nums):
    sorted_nums = sorted((num, idx) for idx, num in enumerate(nums))
    result = [0] * len(nums)
    smaller_count = 0
    for i in range(len(nums)):
        if i == 0 or sorted_nums[i][0] > sorted_nums[i - 1][0]:
            smaller_count = i
        result[sorted_nums[i][1]] = smaller_count
    return result
nums = [8, 1, 2, 2, 3]
print(smallerNumbersThanCurrent(nums)) 

