class Solution(object):
    def evalRPN(self, tokens):
        stack = []
        for token in tokens:
            if token not in ("+", "-", "*", "/"):
                stack.append(int(token))
            else:
                op1 = stack.pop()
                op2 = stack.pop()
                if token == "+":
                    stack.append(op2 + op1)
                elif token == "-":
                    stack.append(op2 - op1)
                elif token == "*":
                    stack.append(op2 * op1)
                else:
                    stack.append(int(float(op2) / op1))
        return stack[0]