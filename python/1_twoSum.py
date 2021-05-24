def twoSum(nums, target):
        for i,num in enumerate(nums):
            add = target - num
            if add in nums[0:i]:
                return [i, nums[0:i].index(add)]
            if add in nums[i + 1:len(nums)]:
                return [i, nums[i + 1:len(nums)].index(add) + i + 1]

print(twoSum([2,7,11,15], 9))
print(2)