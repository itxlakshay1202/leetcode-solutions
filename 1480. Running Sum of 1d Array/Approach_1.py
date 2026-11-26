class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        i = 1
        sum = []
        sum.append(nums[0])
        while i < len(nums):
            sum.append(sum[i-1] + nums[i])
            i+=1
        return sum