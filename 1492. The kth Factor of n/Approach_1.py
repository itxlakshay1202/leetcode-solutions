class Solution(object):
    def kthFactor(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        fact = []
        i = 1
        while i <= n:
            if len(fact) == k:
                return fact.pop()
            if n % i == 0:
                fact.append(i)
            i+=1
        if len(fact) < k: 
            return -1
        else:
            return fact.pop()