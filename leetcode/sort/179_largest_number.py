def largestNumber(nums):  
    nums = list(map(str, nums))
    nums.sort(key = lambda x : x[0],  reverse = True)
    return ''.join(nums)

print(largestNumber([10, 2]))
print(largestNumber([3, 30, 34, 5, 9]))