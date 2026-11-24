class Solution(object):
    def countLargestGroup(self, n):
        """
        :type n: int
        :rtype: int
        """
        i = 1
        dic = {}
        while i <= n :
            icopy = i
            sum = 0
            while icopy > 0:
                sum += icopy % 10
                icopy //= 10
            if sum not in dic.keys():
                dic[sum] = 1
            else:
                dic[sum] += 1
            i+=1

        max_num = max(dic.values())

        count = 0
        for i in dic.values():
            if i == max_num:
                count+=1
        return count   