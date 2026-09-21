class Solution(object):
    def twoSum(self, nums, target):
        PrevMap={}

        for i,n in enumerate(nums):
            diff=target-n
            if diff in PrevMap:
                return [PrevMap[diff],i]
            PrevMap[n]=i


        