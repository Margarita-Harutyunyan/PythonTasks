#return the sum of all unique elements in given integer array 
def unique_sum(nums):
    sum = 0
    for num in nums:
        if nums.count(num) == 1:
            sum += num
    return sum
