class Solution(object):
    def check(self, n):
        prime = [2,3,5,7,11,13,17,19]
        count = 0
        while n > 0:
            if n % 2 == 1:
                count += 1
            n //= 2
        
        if count in prime:
            return True 
        else:
            False

    def countPrimeSetBits(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        sum = 0
        while left <= right:
            if self.check(left):
                sum += 1
            left+=1

        return sum