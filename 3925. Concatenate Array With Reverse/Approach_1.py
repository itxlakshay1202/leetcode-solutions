class Solution(object):
    def concatWithReverse(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ei = len(nums)-1
        while ei >= 0:
            nums.append(nums[ei])
            ei -= 1
        return nums