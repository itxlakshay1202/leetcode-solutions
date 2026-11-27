class Solution(object):
    def evenNumberBitwiseORs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        i = 0
        while i < len(nums):
            if nums[i] % 2 == 0 and res == 0:
                res = nums[i]
            elif nums[i] % 2 == 0 and res != 0:
                res = res | nums[i]
            print(res)
            i+=1
        return res