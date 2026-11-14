# 344. Reverse String

### Difficulty: Easy

## Description
Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.

 
Example 1:
Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:
Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]

 
Constraints:


	1 <= s.length <= 105
	s[i] is a printable ascii character.

## Submission Details
- **Status**: Accepted
- **Runtime**: 5
- **Memory**: 19528000
- **Language**: python

## Code
```python
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
```
