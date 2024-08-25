def twoSum(nums, target):
    diffMap = {}
    for i in range(len(nums)):
        diff  = target - nums[i]
        if nums[i] in diffMap:
            return [diffMap[nums[i]], i]
        diffMap[diff] = i
    return False

print(twoSum([2,7,11,15], 18))
        