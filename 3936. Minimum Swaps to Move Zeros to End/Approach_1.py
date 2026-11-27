class Solution(object):
    def minimumSwaps(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        si = 0
        ei = len(nums)-1
        count = 0

        while ei >si:
            if nums[ei] == 0:
                ei -= 1
                continue
            if nums[si] == 0:
                temp = nums[si]
                nums[si] = nums[ei]
                nums[ei] = temp
                count +=1
                ei -= 1
            si += 1
        return count