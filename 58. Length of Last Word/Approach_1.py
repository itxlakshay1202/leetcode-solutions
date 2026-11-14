class Solution(object):
    def lengthOfLastWord(self, s):
        i = len(s)-1
        stack = []
        while i >= 0:
            if s[i] == ' ' and len(stack) == 0:
                i -= 1
            elif s[i] == ' ' and len(stack) != 0:
                return len(stack)
            else :
                stack.append(s[i])
                i -= 1
        return len(stack)
            
            