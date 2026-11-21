class Solution(object):
    def maximumOddBinaryNumber(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = s.count('1')
        sol = []
        for i in range(0,n-1):
            sol.append('1')
        for i in range(0,len(s)-n) :
            sol.append('0')
        sol.append('1')

        return "".join(sol)