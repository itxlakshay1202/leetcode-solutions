class Solution(object):
    def sumofarray(self,nums):
        sum = 0
        i = 0
        while i < len(nums):
            sum+= nums[i]
            i+=1
        return sum
    def minOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        op = 0
        i = 0
        n = self.sumofarray(nums)
        while n % k != 0:
            nums[i] -= 1
            op += 1
            if nums[i] == 0:
                i += 1
            n -= 1

        return op
