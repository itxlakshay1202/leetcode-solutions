class Solution(object):
    def selfDividing(self,n_copy,n):
        if n_copy == 0:
            return True
        else: 
            temp = n_copy % 10
            if temp == 0:
                return False  
            if n % temp == 0:
                return self.selfDividing(n_copy//10,n)
            else :
                return False

    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        answer = []
        for i in range(left,right+1):
            if self.selfDividing(i,i):
                answer.append(i)
        
        return answer
        