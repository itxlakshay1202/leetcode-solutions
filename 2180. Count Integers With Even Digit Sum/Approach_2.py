class Solution(object):
    def countEven(self, num):
        """
        :type num: int
        :rtype: int
        """
        count = 0
        while num != 0:
            sum = 0
            num_cpy = num
            while num_cpy > 0:
                sum += num_cpy % 10
                num_cpy //= 10
            if sum % 2 == 0:
                count += 1
            num -= 1
        return count