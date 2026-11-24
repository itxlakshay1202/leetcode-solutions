class Solution(object):
    def convertToBase7(self, num):
        if num == 0:
            return "0"
        n = num
        if num < 0:
            num *= -1
        lst = []
        while num > 0:
            lst.insert(0, str(num % 7))
            num //= 7
        res = "".join(lst)
        return res if n > 0 else "-" + res