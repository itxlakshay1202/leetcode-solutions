class Solution(object):
    def isMiddleElementUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        si = 0
        ei = len(nums)-1
        mid = si + (ei - si) / 2
        if nums.count(nums[mid]) == 1:
            return True
        else:
            return False