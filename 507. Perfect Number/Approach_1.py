class Solution(object):
    def checkPerfectNumber(self, num):
        sum = 0
        if num == 1:
            return False
        sq = int(pow(num,0.5))
        for i in range(1,sq+1):
            if num%i==0:
                sum += i
                if i != 1:
                    sum += (num/i)

        if num == sum:
            return True
        else :
            return False