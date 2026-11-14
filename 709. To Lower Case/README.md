# 709. To Lower Case

### Difficulty: Easy

## Description
Given a string s, return the string after replacing every uppercase letter with the same lowercase letter.

 
Example 1:


Input: s = "Hello"
Output: "hello"


Example 2:


Input: s = "here"
Output: "here"


Example 3:


Input: s = "LOVELY"
Output: "lovely"


 
Constraints:


	1 <= s.length <= 100
	s consists of printable ASCII characters.

## Submission Details
- **Status**: Accepted
- **Runtime**: 0 ms
- **Memory**: 11984000
- **Language**: python

## Code
```python
class Solution(object):
    def toLowerCase(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s.lower()
```
