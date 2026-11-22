class Solution(object):
    def countDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        num_copy = num
        count = 0
        while num_copy > 0:
            if num % (num_copy % 10) == 0:
                count += 1
            num_copy //= 10
        return count