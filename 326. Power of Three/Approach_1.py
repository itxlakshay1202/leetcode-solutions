class Solution(object):
    def isPowerOfThree(self, n):
        if n == 0:
            return False
        while 1 != n:
            if n%3 == 0:
                n /= 3
            else:
                return False
        return True