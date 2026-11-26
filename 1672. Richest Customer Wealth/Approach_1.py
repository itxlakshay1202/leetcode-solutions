class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        s = {}
        i = 0
        while i < len(accounts):
            j = 0
            sum = 0
            while j < len(accounts[i]):
                sum += accounts[i][j]
                j += 1
            s[i] = sum
            i+=1
        
        m = max(s.values())
        return m