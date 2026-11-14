class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        i = 0
        n = len(s)
        while i < n//2:
            temp = s[i]
            s[i] = s[n-i-1]
            s[n-i-1] = temp
            i += 1