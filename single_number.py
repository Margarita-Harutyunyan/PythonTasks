#find the number that appears once in a given array
def single_number(nums):
    res = 0
    for n in nums:
        res ^= n
    return res
