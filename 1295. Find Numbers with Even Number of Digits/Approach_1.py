class Solution(object):
    def calculate(self , n):
        lst = []
        while n > 0:
            lst.insert(0,n % 10)
            n = n // 10

        if len(lst) % 2 == 0:
            return True
        else:
            return False

    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        for i in nums:
            if self.calculate(i):
                count += 1

        return count
        