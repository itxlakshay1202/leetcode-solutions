class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        lst = [0,1,1]
        i = 3
        while i <= n:
            lst.append(lst[i-1] + lst[i-2] + lst[i-3])
            i+=1

        return lst[n]