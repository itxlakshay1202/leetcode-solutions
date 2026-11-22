class Solution(object):
    def digitFrequencyScore(self, n):
        """
        :type n: int
        :rtype: int
        """
        lst = []
        while n > 0:
            lst.append(n%10)
            n//=10
        sum = 0
        for i in range(0,10):
            sum += i * lst.count(i)

        return sum