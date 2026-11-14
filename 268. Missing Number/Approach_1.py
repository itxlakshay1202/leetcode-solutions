class Solution(object):
    def missingNumber(self, nums):
        nums.sort()
        n = len(nums)
        i = 0
        if nums[i] != 0:
            return 0
        while i < n-1:
            if i == n-2 and nums[i] == nums[i+1]-1:
                return nums[i+1]+1
            elif i == n-2 and nums[i] != nums[i+1]-1:
                return nums[i]+1
            elif nums[i] != nums[i+1]-1:
                return nums[i]+1
            else:
                i += 1
        return 1


        