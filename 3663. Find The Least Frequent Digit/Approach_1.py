class Solution(object):
    def getLeastFrequentDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        dic ={}
        while n > 0:
            if n % 10 not in dic:
                dic[n%10] = 1
            else:
                dic[n%10] += 1
            n //= 10
        
        m = min(dic.values())
        print(dic)
        for k in sorted(dic):
            if dic[k] == m:
                return k