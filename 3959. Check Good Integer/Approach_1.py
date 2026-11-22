class Solution(object):
    def checkGoodInteger(self, n):
        """
        :type n: int
        :rtype: bool
        """
        s = 0
        s_sq = 0

        while n > 0:
            s +=  n % 10
            s_sq += (n % 10) ** 2
            n //= 10

        if s_sq - s >= 50:
            return True
        else:
            return False 