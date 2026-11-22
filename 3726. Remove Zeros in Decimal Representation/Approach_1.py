class Solution(object):
    def removeZeros(self, n):
        """
        :type n: int
        :rtype: int
        """
        num = 0
        count = 0
        while n > 0:
            if n% 10 != 0:
                num = n % 10 * (10 ** count) + num
                count += 1
            n//= 10
        return num