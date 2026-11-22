class Solution(object):
    def validDigit(self, n, x):
        """
        :type n: int
        :type x: int
        :rtype: bool
        """
        if n == 0 :
            return False
        lst = []
        while n > 0:
            lst.insert(0,n % 10)
            n //= 10

        if lst[0] == x :
            return False
        elif lst.count(x) > 0:
            return True
        else:
            return False