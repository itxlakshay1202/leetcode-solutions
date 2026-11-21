class Solution(object):
    def getFinalState(self, nums, k, multiplier):
        """
        :type nums: List[int]
        :type k: int
        :type multiplier: int
        :rtype: List[int]
        """
        i = 0
        while i < k:
            least = 0
            j = 0
            while j < len(nums):
                if nums[j] < nums[least]:
                    least = j
                j+=1
            nums[least] *= multiplier
            i += 1

        return nums
