class Solution(object):
    def averageValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum = 0
        count = 0
        i = 0
        while i < len(nums):
            if nums[i] % 6 == 0:
                sum += nums[i]
                count += 1
            i+= 1
        if count > 0:
            return sum/count 
        else:
            return 0