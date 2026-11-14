# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        si = 1
        ei = n
        while si < ei:
            mid = si + (ei-si) // 2

            if isBadVersion(mid):
                ei = mid
            else :
                si = mid+1
        if isBadVersion(si):
            return si 
        else:
            return mid