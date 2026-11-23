class Solution(object):
    def checkTwoChessboards(self, coordinate1, coordinate2):
        """
        :type coordinate1: str
        :type coordinate2: str
        :rtype: bool
        """
        a = ord(coordinate1[0])-97 + int(coordinate1[1])-1
        b = ord(coordinate2[0])-97 + int(coordinate2[1])-1
        
        if a % 2 == b % 2:
            return True
        else:
            return False