class Solution(object):
    def splitNum(self, num):
        """
        :type num: int
        :rtype: int
        """
        n = []
        while num > 0:
            n.append(num%10)
            num//=10
        n.sort()
        num1 = 0
        num2 = 0
        p1 = 0
        p2 = 0
        i= 1
        while len(n) > 0:
            if i ==1:
                num1 += n.pop() * (10 ** p1)
                i += 1
                p1+=1
            else:
                num2 += n.pop() * (10**p2)
                i-=1
                p2+=1
        return num1 + num2