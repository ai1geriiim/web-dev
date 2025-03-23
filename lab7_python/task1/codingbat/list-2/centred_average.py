def centered_average(nums):
    nums.sort()
    nums = nums[1:-1]
    return sum(nums) // len(nums)
nums=eval(input())
print(centered_average(nums))


