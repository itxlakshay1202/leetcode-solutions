class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        return int(-0.5 + pow(2*n+0.25,0.5))
        
        