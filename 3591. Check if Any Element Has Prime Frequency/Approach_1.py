class Solution(object):
    def prime(self , n):
        if n != 2 and n % 2 == 0:
            return False
        p = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
        i = 0
        while i < len(p) and p[i] <= n:
            if p[i] == n:
                return True
            i+=1
        return False
    def checkPrimeFrequency(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dic = {}
        for i in nums:
            if i not in dic:
              dic[i] = 1
            else:
                dic[i] += 1

        for i in sorted(dic):
            if self.prime(dic[i]):
                return True

        return False