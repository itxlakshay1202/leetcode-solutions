class Solution(object):
    def minCuttingCost(self, n, m, k):
        """
        :type n: int
        :type m: int
        :type k: int
        :rtype: int
        """
        cost = 0
        if n > k:
            cost = k * (n-k)
        if m > k:
            cost += k * (m-k)

        return cost