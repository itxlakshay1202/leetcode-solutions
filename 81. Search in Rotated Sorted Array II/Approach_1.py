class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if nums.count(target) > 0:
            return True
        else:
            return False
        