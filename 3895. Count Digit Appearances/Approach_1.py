class Solution(object):
    def countDigitOccurrences(self, nums, digit):
        """
        :type nums: List[int]
        :type digit: int
        :rtype: int
        """
        dic = {1:0 , 2:0 , 3:0 , 4:0 , 5:0 , 6:0 , 7:0 , 8:0 , 9:0 , 0:0}
        for i in nums:
            while i > 0:
                dic[i%10] += 1
                i //= 10
        print(dic)
        return dic[digit]