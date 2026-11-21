class Solution(object):
    def sumOfMultiples(self, n):
        """
        :type n: int
        :rtype: int
        """
        i = 1
        sum = 0
        while i <= n:
            if i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
                sum+=i
            i+=1

        return sum