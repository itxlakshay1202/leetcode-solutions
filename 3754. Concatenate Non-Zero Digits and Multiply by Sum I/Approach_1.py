class Solution(object):
    def sumAndMultiply(self, n):
        """
        :type n: int
        :rtype: int
        """
        sum = 0
        num = 0
        count = 0
        while n > 0:
            if n % 10 != 0:
                num = n % 10 * (10 ** count) + num
                sum += n % 10
                count += 1
            n//=10

        return num * sum