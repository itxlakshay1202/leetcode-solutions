class Solution(object):
    def binary(self, n):
        lst = []
        while n > 0:
            lst.insert(0,str(n % 2))
            n //= 2
        return lst

    def convertDateToBinary(self, date):
        """
        :type date: str
        :rtype: str
        """
        year = int(date[0:4])
        month = int(date[5:7])
        day = int(date[8:10])

        year_list = self.binary(year)
        month_lst = self.binary(month)
        day_lst = self.binary(day)

        return "".join(year_list)+"-"+"".join(month_lst)+"-"+"".join(day_lst)