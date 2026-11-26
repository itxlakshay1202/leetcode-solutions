class Solution(object):
    def distanceTraveled(self, mainTank, additionalTank):
        """
        :type mainTank: int
        :type additionalTank: int
        :rtype: int
        """
        dist = 0
        while mainTank > 0:
            if mainTank >= 5 and additionalTank > 0:
                dist += 50
                additionalTank -= 1
                mainTank -= 4
            else:
                dist += 10 * (mainTank)
                mainTank = 0

        return dist