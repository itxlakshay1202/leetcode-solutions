class Solution(object):
    def generateKey(self, num1, num2, num3):
        """
        :type num1: int
        :type num2: int
        :type num3: int
        :rtype: int
        """
        sol = 0
        i = 0
        while i < 4:
            sol = min(num1%10,num2%10,num3%10) * (10**i) + sol
            num1 //= 10
            num2 //= 10
            num3 //= 10
            i+=1

        return sol
        
        