class Solution(object):
    def squareIsWhite(self, coordinates):
        """
        :type coordinates: str
        :rtype: bool
        """
        coord = ord(coordinates[0]) - 94 + int(coordinates[1])
        if coord % 2 == 0:
            return False
        else:
            return True
        