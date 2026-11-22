class Solution(object):
    def alternateDigitSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        digit = []
        while n > 0:
            digit.insert(0,n % 10)
            n //= 10 

        n = 0
        sum = 0
        while n < len(digit):
            if n % 2 == 0:
                sum += digit[n]
            else:
                sum -= digit[n]
            n+=1

        return sum