class Solution(object):
    def minimumFlips(self, n):
        """
        :type n: int
        :rtype: int
        """
        lis = []
        while n > 0:
            lis.insert(0,n % 2)
            n //= 2
        
        flip = 0
        si = 0
        ei = len(lis)-1
        while si <= ei:
            if lis[si] != lis[ei]:
                flip += 2
            si += 1
            ei -= 1
            
        return flip