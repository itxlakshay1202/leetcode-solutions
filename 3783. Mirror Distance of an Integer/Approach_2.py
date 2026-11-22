class Solution(object):
    def mirrorDistance(self, n):
        """
        :type n: int
        :rtype: int
        """
        n_c = n
        reverse = 0
        while n_c > 0:
            reverse = reverse * 10 + n_c % 10
            n_c //= 10

        if reverse == n:
            return 0
        elif reverse > n:
            return reverse - n
        else:
            return n - reverse