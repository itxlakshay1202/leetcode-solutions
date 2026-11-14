class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        i = 0
        l = len(columnTitle)
        result = 0
        while i < l:
            result = result * 26 + (ord(columnTitle[i])-64)
            i += 1

        return result
