class Solution(object):
    def decimalRepresentation(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        i = 0
        lst = []
        while n > 0:
            if n % 10 != 0:
                lst.insert(0,(n % 10) * (10 ** i))
            n //= 10
            i += 1
        return lst
            