class Solution(object):
    def isPowerOfTwo(self, n):
        if n == 0:
            return False
        while 1 != n:
            if n%2 == 0:
                n /= 2
            else:
                return False
        return True