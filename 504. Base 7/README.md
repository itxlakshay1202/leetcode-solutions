# 504. Base 7

### Difficulty: Easy

## Description
Given an integer num, return a string of its base 7 representation.

 
Example 1:
Input: num = 100
Output: "202"
Example 2:
Input: num = -7
Output: "-10"

 
Constraints:


	-107 <= num <= 107

## Submission Details
- **Status**: Accepted
- **Runtime**: 0 ms
- **Memory**: 12116000
- **Language**: python

## Code
```python
class Solution(object):
    def convertToBase7(self, num):
        if num == 0:
            return "0"
        n = num
        if num < 0:
            num *= -1
        lst = []
        while num > 0:
            lst.insert(0, str(num % 7))
            num //= 7
        res = "".join(lst)
        return res if n > 0 else "-" + res
```
