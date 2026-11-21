class Solution(object):
    def encrypt(self , n):
        count = 0
        max = 0
        while n > 0:
            if n % 10 > max:
                max = n % 10
            
            count +=1
            n //= 10

        while count > 0:
            n = n * 10 + max
            count -= 1

        return n

    def sumOfEncryptedInt(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum = 0
        for i in nums:
            sum += self.encrypt(i)

        return sum
        