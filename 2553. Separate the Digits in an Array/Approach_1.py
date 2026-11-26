class Solution(object):
    def separateDigits(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for i in nums:
            temp = []
            while i > 0:
                temp.insert(0,i%10)
                i//=10
            res.extend(temp)

        return res