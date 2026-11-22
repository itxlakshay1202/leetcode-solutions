class Solution(object):
    def sum(self , i):
        s = 0
        while i > 0:
            s += i % 10
            i //= 10

        return s

    def smallestIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        while i < len(nums):
            if self.sum(nums[i]) == i:
                return i
            i += 1

        return -1
