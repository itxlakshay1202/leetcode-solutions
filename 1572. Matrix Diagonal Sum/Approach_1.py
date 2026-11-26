class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        i = 0 
        sum = 0
        n = len(mat) -1
        m = len(mat[0]) -1
        while i <= n:
            if m-i != i:
                sum += mat[i][i] + mat[i][m-i]
            else:
                sum += mat[i][i]
            i+=1
        return sum
