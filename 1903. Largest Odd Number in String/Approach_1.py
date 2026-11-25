class Solution(object):
    def largestOddNumber(self, num):
        """
        :type num: str
        :rtype: str
        """
        ei = len(num) -1

        while ei >= 0:
            if ord(num[ei]) % 2 == 1:
                return "".join(num[0:ei+1])
            ei -= 1
        return ""