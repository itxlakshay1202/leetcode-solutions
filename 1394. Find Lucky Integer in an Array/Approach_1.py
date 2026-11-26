class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        dic = {}
        lst = []
        for i in arr:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
        
        for k in dic:
            if dic[k] == k:
                lst.append(k)

        if len(lst) > 0:
            return max(lst)
        else:
            return -1