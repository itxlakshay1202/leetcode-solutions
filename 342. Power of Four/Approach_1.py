class Solution(object):
    def isPowerOfFour(self, n):
        if n == 0:
            return False
        while 1 != n:
            if n%4 == 0:
                n /= 4
            else:
                return False
        return True
        