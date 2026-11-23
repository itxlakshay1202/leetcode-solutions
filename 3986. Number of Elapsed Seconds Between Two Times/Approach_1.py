class Solution(object):
    def secondsBetweenTimes(self, startTime, endTime):
        """
        :type startTime: str
        :type endTime: str
        :rtype: int
        """
        hours = int(endTime[0:2]) - int(startTime[0:2])
        min =  int(endTime[3:5]) - int(startTime[3:5])
        sec =  int(endTime[6:8]) - int(startTime[6:8])

        return hours * 3600 + min * 60 + sec