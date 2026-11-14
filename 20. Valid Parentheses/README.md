# 20. Valid Parentheses

### Difficulty: Easy

## Description
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:


	Open brackets must be closed by the same type of brackets.
	Open brackets must be closed in the correct order.
	Every close bracket has a corresponding open bracket of the same type.


 
Example 1:


Input: s = "()"

Output: true


Example 2:


Input: s = "()[]{}"

Output: true


Example 3:


Input: s = "(]"

Output: false


Example 4:


Input: s = "([])"

Output: true


Example 5:


Input: s = "([)]"

Output: false


 
Constraints:


	1 <= s.length <= 104
	s consists of parentheses only '()[]{}'.

## Submission Details
- **Status**: Accepted
- **Runtime**: 6
- **Memory**: 12192000
- **Language**: python

## Code
```python
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
```
