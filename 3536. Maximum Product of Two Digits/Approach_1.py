class Solution(object):
    def maxProduct(self, n):
        """
        :type n: int
        :rtype: int
        """
        lst = []
        while n > 0:
            lst.append(n % 10)
            n //= 10
        lst.sort()
        return lst.pop() * lst.pop()