class Solution(object):
    def d(self , x , z):
        if x == z:
            return 0
        elif x > z:
            return x -z
        else:
            return z - x

    def findClosest(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: int
        """

        if self.d(x,z) > self.d(y,z):
            return 2
        elif self.d(x,z) < self.d(y,z):
            return 1
        else:
            return 0