nums = [1, 3, 4, 5, 3, 2, 1]

nums.sort()
for i in range(1, len(nums)):
    if nums[i] == nums[i-1]:
        print(nums[i])
