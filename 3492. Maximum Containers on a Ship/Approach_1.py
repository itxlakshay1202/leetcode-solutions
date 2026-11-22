class Solution(object):
    def maxContainers(self, n, w, maxWeight):
        """
        :type n: int
        :type w: int
        :type maxWeight: int
        :rtype: int
        """
        if n * n * w <= maxWeight:
            return n**2
        else :
            return maxWeight / w