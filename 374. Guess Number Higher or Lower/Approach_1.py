# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        si = 1
        ei = n
        while si <= ei:
            mid = si + (ei - si) // 2
            new = guess(mid)

            if new == 0:
                return mid
            elif new == 1:
                si = mid+1
            else:
                ei = mid-1
