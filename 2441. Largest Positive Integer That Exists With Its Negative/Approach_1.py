class Solution(object):
    def findMaxK(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        res = {}
        while len(nums) != 0:
            x = nums.pop(0)
            if (x * -1) in nums and x > 0:
                res[x] = 1
                nums.remove(x*-1)
            elif (x * -1) in nums and x < 0:
                res[x*-1] = 1
                nums.remove(x*-1)

        if len(res) != 0:
            return max(res)
        else:
            return -1