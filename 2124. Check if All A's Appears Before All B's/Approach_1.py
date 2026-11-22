class Solution(object):
    def checkString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i = 1
        while i < len(s):
            if s[i-1] == "b" and s[i] == "a":
                return False
            i+=1
        return True