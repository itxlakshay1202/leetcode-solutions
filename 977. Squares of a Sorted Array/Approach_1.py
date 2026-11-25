class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        si = 0
        ei = len(nums)-1
        lst = []
        while si <= ei:
            if nums[si] * -1 >= nums[ei] :
                lst.insert(0,nums[si] ** 2)
                si += 1
            else:
                lst.insert(0,nums[ei] ** 2)
                ei -= 1

        return lst