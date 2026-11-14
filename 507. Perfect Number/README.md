# 507. Perfect Number

### Difficulty: Easy

## Description
A perfect number is a positive integer that is equal to the sum of its positive divisors, excluding the number itself. A divisor of an integer x is an integer that can divide x evenly.

Given an integer n, return true if n is a perfect number, otherwise return false.

 
Example 1:


Input: num = 28
Output: true
Explanation: 28 = 1 + 2 + 4 + 7 + 14
1, 2, 4, 7, and 14 are all divisors of 28.


Example 2:


Input: num = 7
Output: false


 
Constraints:


	1 <= num <= 108

## Submission Details
- **Status**: Accepted
- **Runtime**: 6
- **Memory**: 12652000
- **Language**: python

## Code
```python
class Solution(object):
    def checkPerfectNumber(self, num):
        sum = 0
        if num == 1:
            return False
        sq = int(pow(num,0.5))
        for i in range(1,sq+1):
            if num%i==0:
                sum += i
                if i != 1:
                    sum += (num/i)

        if num == sum:
            return True
        else :
            return False
```
