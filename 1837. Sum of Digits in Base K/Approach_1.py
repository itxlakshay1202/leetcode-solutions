class Solution(object):
    def sumBase(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        sum = 0
        while n > 0:
            sum += n % k
            n //= k

        return sum