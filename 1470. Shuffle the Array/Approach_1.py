class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        res =[]
        z = len(nums)
        x = nums[0:n]
        y = nums[n:z]
        i = 0
        while i < n:
            res.append(x.pop(0))
            res.append(y.pop(0))
            i += 1
        return res