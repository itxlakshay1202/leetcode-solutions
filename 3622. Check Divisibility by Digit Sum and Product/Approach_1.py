class Solution(object):
    def checkDivisibility(self, n):
        """
        :type n: int
        :rtype: bool
        """
        n_c = n
        sum = 0
        prod = 1
        while n > 0:
            sum += n % 10
            prod *= n % 10
            n//=10

        if n_c % (sum + prod) == 0:
            return True
        else:
            return False