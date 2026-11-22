class Solution(object):
    def arraySign(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prod = 1
        i = 0
        while i < len(nums):
            prod *= nums[i]
            i += 1

        if prod > 0:
            return 1
        elif prod == 0:
            return 0
        else:
            return -1