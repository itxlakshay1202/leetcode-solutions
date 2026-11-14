class Solution(object):
    def myPow(self, x, n):
        if x == 0:
            return 0
        elif n == 0:
            return 1
        else:
            return x ** n
