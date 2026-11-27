class Solution(object):
    def sumDivisibleByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        dic = {}
        sum = 0

        for i in nums:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1

        for i in dic:
            if dic[i] % k == 0:
                sum += dic[i] * i

        return sum