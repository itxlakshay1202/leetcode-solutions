class Solution(object):
    def digits(self,n,lst):
            while n > 0:
                if n % 10 != 0:
                    if n % 10 not in lst:
                        lst[n%10] = n%10
                        n //= 10
                        print(lst)
                    else:
                        return False
                else:
                    return False
            return True
    def isFascinating(self, n):
        """
        :type n: int
        :rtype: bool
        """
        lst = {}
        if self.digits(n,lst):
            if self.digits(2*n,lst):
                if self.digits(3*n,lst):
                    return True
        return False
        