class Solution(object):
    def sumOfTheDigitsOfHarshadNumber(self, x):
        """
        :type x: int
        :rtype: int
        """
        i = x
        sum = 0
        while i > 0:
            sum = sum + i % 10
            i //= 10

        if x %  sum == 0:
            return sum
        else:
            return -1