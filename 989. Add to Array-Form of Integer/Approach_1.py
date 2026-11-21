class Solution(object):
    def addToArrayForm(self, num, k):
        """
        :type num: List[int]
        :type k: int
        :rtype: List[int]
        """
        number = 0
        while len(num) != 0:
            number = number * 10 + num.pop(0)

        number += k
        while number > 0:
            num.insert(0,number % 10)
            number //= 10

        return num