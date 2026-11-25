class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        moves = 0
        max = nums[0]
        i = 1
        while i < len(nums):
            if max < nums[i]:
                moves = moves + (i) * (nums[i] - max)
                max = nums[i]
            else:
                moves += (max - nums[i])
            i+=1
        return moves