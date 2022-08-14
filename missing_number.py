def missing_number(nums):
    for num in range(len(nums) + 1):
        if num not in nums:
            return num
