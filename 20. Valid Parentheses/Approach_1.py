class Solution(object):
    def isValid(self, s):
        i = 0
        stack = []
        while i < len(s):
            top = len(stack)-1
            if top < 0:
                stack.append(s[i])
            elif s[i] == '(' or s[i] == '[' or s[i] == '{':
                stack.append(s[i])
            elif s[i] == ')':
                if stack[top] == '(' and top >= 0:
                    stack.pop()
                else :
                    stack.append(s[i])
            elif s[i] == ']':
                if stack[top] == '[' and top >= 0:
                    stack.pop()
                else :
                    stack.append(s[i])
            else:
                if stack[top] == '{' and top >= 0:
                    stack.pop()
                else :
                    stack.append(s[i])
            i += 1

        if len(stack) == 0:
            return True
        else:
            return False