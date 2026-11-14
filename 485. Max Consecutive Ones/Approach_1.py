class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0 
        count = 0
        result = []
        while i < len(nums):
            if nums[i] == 1:
                count += 1
                i += 1
            else:
                result.append(count)
                count = 0
                i += 1
        
        if nums[i-1] == 1:
            result.append(count)
        return max(result)
