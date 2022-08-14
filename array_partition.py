def array_partition(nums):
    nums.sort()
    return sum(nums[::2])
