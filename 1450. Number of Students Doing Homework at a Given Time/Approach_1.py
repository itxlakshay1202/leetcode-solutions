class Solution(object):
    def busyStudent(self, startTime, endTime, queryTime):
        """
        :type startTime: List[int]
        :type endTime: List[int]
        :type queryTime: int
        :rtype: int
        """
        i = 0
        count = 0
        while i < len(startTime):
            if startTime[i] <= queryTime and endTime[i] >= queryTime:
                count+=1
            i+=1
        return count