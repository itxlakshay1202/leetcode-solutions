class Solution(object):
    def average(self, salary):
        """
        :type salary: List[int]
        :rtype: float
        """
        i = 0
        sum = 0
        min = salary[0]
        max = salary[0]
        while i < len(salary):
            sum+=salary[i]
            if min > salary[i]:
                min = salary[i]
            if max < salary[i]:
                max = salary[i]
            i+=1

        sum -= (min + max)

        return float(sum) / (len(salary) - 2)