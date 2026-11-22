class Solution(object):
    def isThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        divisors = []
        i = 1
        while i <= n:
            if len(divisors) > 3:
                return False
            else:
                if n % i == 0:
                    divisors.append(i)
                i+=1

        if len(divisors) == 3:
            return True
        else:
            return False