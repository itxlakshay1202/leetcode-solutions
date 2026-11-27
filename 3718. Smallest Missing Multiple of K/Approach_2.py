class Solution(object):
    def missingMultiple(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        x = k
        while True:
            try:
                nums.remove(x)
                x += k   
            except:
                return x