class Solution(object):
    def singleNumber(self, nums):
        while True:
            i = nums[0]
            if(nums.count(i) == 1):
                return i
            else:
                nums.remove(i)
                nums.remove(i)