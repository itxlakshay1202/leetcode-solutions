class Solution(object):
    def moveZeroes(self, nums):
        i = 0
        count = 0
        while i < len(nums):
            if nums[i] == 0:
                count += 1
                nums.pop(i)
            else:
                i += 1
        for i in range(0,count):
            nums.append(0)