class Solution(object):
    def majorityElement(self, nums):
        while True:
            i = nums[0]
            c = nums.count(i)
            if(c > len(nums)//2):
                return i
            else:
                for j in range(0,c):
                    nums.remove(i)