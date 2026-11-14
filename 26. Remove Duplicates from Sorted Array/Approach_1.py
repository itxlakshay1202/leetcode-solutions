class Solution(object):
    def removeDuplicates(self, nums):
        current = -101
        i = 0
        while i != len(nums):
            if nums[i] > current :
                current = nums[i]
                i += 1
            else:
                nums.pop(i)

        return len(nums)