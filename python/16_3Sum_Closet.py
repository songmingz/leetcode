# Runtime: 904 ms, faster than 5.04% of Python3 online submissions for 3Sum Closest.
# Memory Usage: 14.1 MB, less than 97.52% of Python3 online submissions for 3Sum Closest.
from typing import List
import time

def threeSumClosest(nums: List[int], target: int) -> int:
    result = [0, 1, 2]
    var = abs(target - nums[0] - nums[1] - nums[2])
    #暴力搜索
    for i in range(len(nums) - 2):
        for j in range(i + 1, len(nums) - 1):
            for k in range(j + 1, len(nums)):
                temp = abs(target - nums[i] - nums[j] - nums[k])
                #若正好等于结果,则直接返回
                if temp == 0:
                    var = temp
                    result[0] = i
                    result[1] = j
                    result[2] = k
                    return nums[result[0]] + nums[result[1]] + nums[result[2]]

                if temp < var:
                    var = temp
                    result[0] = i
                    result[1] = j
                    result[2] = k
    
    print(str((end - start) * 1000) + 'ms')
    return nums[result[0]] + nums[result[1]] + nums[result[2]]

start = time.time()
print(threeSumClosest([-22,85,-21,-4,-19,91,-54,-50,-4,-27,11,-41,99,32,-4,-70,-42,64,1,30,37,59,-89,6,61,-50,57,-85,-10,18,15,6,75,87,-70,-63,-69,-29,29,84,-35,-27,-91,-47,61,13,20,100,-21,3,-35,63,87,-95,-94,-71,10,21,76,100,-100,-44,-98,-47,63,-41,-82,68,-28,49,5,-50,-83,15,5,-93,94,91,-81,8,-19,6,-19,-34,-69,-69,34,-23,56,-74,19,-31,2,-3,-91,-58,-61,42,-72,-94,-91,-81,-13,-74,8,96,79,-73,14,97,-88,-47,86,61,-31,-63,-83,-12,80,30,65,-14,18,57,-29,-2,41,97,4,-15,79,22,-54,-90,-52,-20,78,-93,-54,94,1,-31,11,0,17,16,-60,90,-39,46,30,-40,-67,-2,-80,-35,58,90,93,50,-5,-38,70,-11,38,-99,-90,-76,69,76,6,96,9,65,-42,-78,-12,-45,41,-90,45,-46,92,-91,-99,74,-43,-34,55,54,45,-76,45], 234))
end = time.time()
print(str((end - start) * 1000) + 'ms')