# 67. Add Binary

### Difficulty: Easy

## Description
Given two binary strings a and b, return their sum as a binary string.

 
Example 1:
Input: a = "11", b = "1"
Output: "100"
Example 2:
Input: a = "1010", b = "1011"
Output: "10101"

 
Constraints:


	1 <= a.length, b.length <= 104
	a and b consist only of '0' or '1' characters.
	Each string does not contain leading zeros except for the zero itself.

## Submission Details
- **Status**: Accepted
- **Runtime**: 9
- **Memory**: 12072000
- **Language**: python

## Code
```python
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        res = []
        i = 0
        num_a = 0
        num_b = 0
        while i < len(a):
            p = len(a)-i-1
            if a[i] == '1':
                num_a += pow(2,p)
            i+=1
         
        i = 0
        while i < len(b):
            p = len(b)-i-1
            if b[i] == '1':
                num_b += pow(2,p)
            i+=1
        print(num_a)
        print(num_b)
        num_sum = num_a+num_b
        if num_sum == 0:
            return "0"
        while num_sum > 0:
            if num_sum % 2 == 0:
                res.insert(0,'0')
            else:
                res.insert(0,'1')

            num_sum //= 2

        return "".join(res)
```
