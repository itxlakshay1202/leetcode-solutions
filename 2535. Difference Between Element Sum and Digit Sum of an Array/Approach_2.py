class Solution(object):
    def differenceOfSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        esum = 0
        dsum = 0
        for i in nums:
            esum += i
            while i > 0:
                dsum += i % 10
                i //= 10
        if esum >= dsum:
            return esum - dsum
        else:
            return dsum - esum