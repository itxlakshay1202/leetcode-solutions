class Solution(object):
    def judgeSquareSum(self, c):
        sq = int(pow(c,0.5)) + 1
        if c == 0:
            return True
        for i in range(0,sq):
            b = pow((c - i*i),0.5)
            if b%1 ==0:
                return True
        return False
        