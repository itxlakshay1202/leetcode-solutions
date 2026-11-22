class Solution(object):
    def validTriangle(self, nums):
        if nums[0] + nums[1] > nums[2]:
            if nums[2] + nums[1] > nums[0]:
                if nums[2] + nums[0] > nums[1]:
                    return True
        return False
    def triangleType(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        if self.validTriangle(nums):
            if nums[0] == nums[1] == nums[2]:
                return "equilateral"
            elif nums[0] == nums[1]or nums[1] == nums[2] or nums[2] == nums[0]:
                return "isosceles"
            else:
                return "scalene"
        else:
            return "none"