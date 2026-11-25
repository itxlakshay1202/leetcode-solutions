class Solution(object):
    def xorOperation(self, n, start):
        """
        :type n: int
        :type start: int
        :rtype: int
        """
        i = 0
        nums = []
        result = 0
        while i < n:
            if i == 0:
                result = start + 2 * i
            else:
                result = result ^ (start + 2*i)
            i+=1
        return result
        