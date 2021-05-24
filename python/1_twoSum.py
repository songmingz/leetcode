#1264ms memory:14.8MB
def twoSum(nums, target):
        for i,num in enumerate(nums):
            #计算出另一个加数
            add = target - num
            #判断此加数是否在列表里(需要排除num,因为不能重复使用相同元素)
            if add in nums[0:i]:
                return [i, nums[0:i].index(add)]
            if add in nums[i + 1:len(nums)]:
                return [i, nums[i + 1:len(nums)].index(add) + i + 1]

print(twoSum([2,7,11,15], 9))
print(2)