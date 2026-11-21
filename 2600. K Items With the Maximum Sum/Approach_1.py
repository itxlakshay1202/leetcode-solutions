class Solution(object):
    def kItemsWithMaximumSum(self, numOnes, numZeros, numNegOnes, k):
        """
        :type numOnes: int
        :type numZeros: int
        :type numNegOnes: int
        :type k: int
        :rtype: int
        """
        sum = 0
        while  (numOnes>0 or numZeros > 0) and k > 0:
            if numOnes > 0:
                sum += 1
                numOnes -= 1
            else :
                numZeros -= 1
            k-=1

        if k == 0:
            return sum
        else:
            return sum + ( k * -1)
                


        