class Solution(object):
    def maximum69Number (self, num):
        """
        :type num: int
        :rtype: int
        """
        lst = []
        while num > 0:
            lst.insert(0,num % 10)
            num = num // 10

        i = 0
        while i < len(lst):
            if lst[i] == 6:
                lst[i] = 9
                break
            else:
                i += 1

        res = 0
        for i in lst :
            res = res * 10 + i

        return res