class Solution(object):
    def alternatingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        sum = 0
        while i < len(nums):
            if i % 2 == 0:
                sum += nums[i]
            else:
                sum -= nums[i]
            i+=1
        return sum