class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        l = []
        dic = {}
        for i in grid:
            j = 0
            while j < len(i):
                if i[j] not in dic:
                    dic[i[j]] = 1
                else:
                    dic[i[j]] += 1
                j+=1
        print(dic)
        for p , j in dic.items():
            if j == 2:
                l.append(p)        
        
        j = 1
        for i in dic:
            if i != j:
                l.append(j)
                break
            j += 1

        if len(l) == 1:
            l.append(j)

        return l