class Solution(object):
    def getMaximumGenerated(self, n):
        """
        :type n: int
        :rtype: int
        """
        nums = [0,1]
        i = 2
        max = 1
        while i <= n:
            if i % 2 == 0:
                nums.append(nums[i/2])
            else:
                if nums[i//2] + nums[(i//2) +1] > max:
                    max = nums[i//2] + nums[(i//2) +1]
                nums.append(nums[i//2] + nums[(i//2) + 1])
            i+=1
        if n == 0:
            return 0
        return max